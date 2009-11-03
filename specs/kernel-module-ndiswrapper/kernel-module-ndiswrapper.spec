# $Id$
# Authority: dag
# Upstream: <ndiswrapper-general$lists,sourceforge,net>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules
%define _sbindir /sbin

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ndiswrapper
%define real_release 1

%define moduledir /kernel/drivers/net/ndiswrapper
%define modules ndiswrapper.o

Summary: Linux NDIS wrapper drivers
Name: kernel-module-ndiswrapper
Version: 0.7
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://ndiswrapper.sourceforge.net/

Source: http://dl.sf.net/ndiswrapper/ndiswrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: ndiswrapper-utils

Provides: kernel-modules

%description
Linux NDIS wrapper drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n ndiswrapper-utils
Summary: NDIS wrapper utilities
Release: %{real_release}%{?dist}
License: GPL
Group: System Environment/Base

Obsoletes: ndiswrapper
Provides: ndiswrapper

%description -n ndiswrapper-utils
NDIS wrapper utilities.

%prep
%setup -n %{real_name}-%{version}

### Enable DEBUG
#%{__perl} -pi.orig -e 's|#DEBUG=1|DEBUG=1|' driver/Makefile

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
cd driver
%{__make} %{?_smp_mflags} \
	KSRC="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	KVERS="24"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Make utilities.
%{__make} %{?_smp_mflags} -C utils \
	CFLAGS="%{optflags}"

%install
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -p -m0755 utils/loadndisdriver utils/ndiswrapper utils/wlan_radio_averatec_5110hx %{buildroot}%{_sbindir}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/ndiswrapper/

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n ndiswrapper-utils
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README
%config(noreplace) %{_sysconfdir}/ndiswrapper/
%{_sbindir}/*

%changelog
* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 0.6-3
- Moved loadndisdriver to /sbin. (Tim Verhoeven)

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.6-2
- Added missing ndiswrapper to ndiswrapper-utils. (Mathias Schulze)

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Mon Mar 08 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
