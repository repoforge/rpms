# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsUser: 0

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname saa7134

%define moduledir /kernel/drivers/video/media/saa7134
%define modules ir-common.o msp3400.o saa6752hs.o saa7134.o tda9887.o tuner.o tvaudio.o v4l1-compat.o v4l2-common.o video-buf.o

%define rrelease 1

Summary: Linux saa7130/7134 (TV/capture card) drivers.
Name: kernel-module-saa7134
Version: 0.2.9
Release: %{rrelease}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://bytesex.org/saa7134/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bytesex.org/saa7134/saa7134-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Provides: kernel-modules

%description
Linux saa7130/7134 (TV/capture card) drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-saa7134
Release: %{rrelease}_%{kversion}_%{krelease}
Summary: Linux saa7130/7134 (TV/capture card) drivers.
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
%setup -n %{rname}-%{version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
%{__make} clean
%{__make} %{?_smp_mflags} \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -s -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make SMP module.
%{__make} clean
%{__make} %{_smp_mflags} \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -s -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Clean up docs
%{__rm} -rf doc/CVS/

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-saa7134
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-saa7134
/sbin/depmod -ae %{kversion}-%{krelease} || :

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
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.2.10-0
- Initial package. (using DAR)
