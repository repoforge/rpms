# $Id$
# Authority: dag
# Upstream: Gerd Knorr <kraxel$bytesex,org>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name saa7134
%define real_release 1

%define moduledir /kernel/drivers/video/media/saa7134
%define modules ir-common.o msp3400.o saa6752hs.o saa7134.o tda9887.o tuner.o tvaudio.o v4l1-compat.o v4l2-common.o video-buf.o

Summary: Linux saa7130/7134 (TV/capture card) drivers
Name: kernel-module-saa7134
Version: 0.2.9
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://bytesex.org/saa7134/

Source: http://bytesex.org/saa7134/saa7134-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Provides: kernel-modules

%description
Linux saa7130/7134 (TV/capture card) drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-saa7134
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
Summary: Linux saa7130/7134 (TV/capture card) drivers
License: GPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules

%description -n kernel-smp-module-saa7134
Linux saa7130/7134 (TV/capture card) drivers.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -n %{real_name}-%{version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
%{__make} clean
%{__make} %{?_smp_mflags} \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -ps -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} clean
%{__make} %{?_smp_mflags} \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -ps -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Clean up docs
%{__rm} -rf doc/CVS/

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-saa7134
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-saa7134
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-saa7134
%defattr(-, root, root, 0755)
%doc doc/*
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.2.10-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.2.10-0
- Initial package. (using DAR)
