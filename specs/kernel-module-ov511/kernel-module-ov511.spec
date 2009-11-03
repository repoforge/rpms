# $Id$
# Authority: dag
# Upstream: Mark McClelland <mark$alpha,dyndns,org>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ov511
%define real_release 1

%define moduledir /kernel/drivers/usb/ov511
%define modules ov511.o ovfx2.o ovcamchip.o saa7111-new.o tda7313.o tuner.o

Summary: Linux OVCam Drivers
Name: kernel-module-ov511
Version: 2.27
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://alpha.dyndns.org/ov511/

Source: http://alpha.dyndns.org/ov511/download/2.xx/distros/ov511-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: ov511, kernel-ov511
Provides: ov511, kernel-ov511
Provides: kernel-modules

%description
Linux OVCam drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ov511
Summary: Linux OVCam Drivers
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Obsoletes: ov511, kernel-ov511
Provides: ov511, kernel-ov511
Provides: kernel-modules

%description -n kernel-smp-module-ov511
Linux OVCam drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi.orig -e 's|^ifeq \(.+,2\.4\)$|ifeq (0,0)|' Makefile

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
%{__make} %{?_smp_mflags} clean all \
	INCLUDEDIR="%{_libmoddir}/%{kversion}-%{krelease}/build/include"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} clean all \
	INCLUDEDIR="%{_libmoddir}/%{kversion}-%{krelease}/build/include"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-ov511
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-ov511
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README ov511.txt
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ov511
%defattr(-, root, root, 0755)
%doc COPYING README ov511.txt
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 2.27-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 2.27-0
- Updated to release 2.27.

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 2.26-0
- Updated to release 2.26.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 2.25-0
- Updated to release 2.25.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 1.65-0
- Updated to release 1.65.

* Thu Jan 23 2003 Dag Wieers <dag@wieers.com> - 1.64-0
- Added smp modules for i586 (but they don't build yet?).

* Wed Jan 22 2003 Dag Wieers <dag@wieers.com> - 1.64-0
- Initial package. (using DAR)
