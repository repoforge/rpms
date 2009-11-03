# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name linux-wlan-ng
%define real_version 0.2.1-pre20
%define real_release 0.pre20

%define moduledir /kernel/drivers/net/wireless/prism2
%define modules prism2_cs.o prism2_pci.o prism2_plx.o prism2_usb.o

Summary: Linux Prism II Wireless 802.11b drivers
Name: kernel-module-prism2
Version: 0.2.1
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: Dual MPL/GPL
Group: System Environment/Kernel
URL: http://www.linux-wlan.com/

Source: ftp://ftp.linux-wlan.org/pub/linux-wlan-ng/linux-wlan-ng-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Provides: kernel-modules
Provides: kernel-module-wlan-ng

%description
Linux Prism II Wireless 802.11b drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-prism2
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
Summary: Linux Prism II Wireless 802.11b drivers
License: Dual MPL/GPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules
Provides: kernel-smp-module-wlan-ng

%description -n kernel-smp-module-prism2
Linux Prism II Wireless 802.11b drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n prism2-utils
Summary: Prism II Wireless 802.11b utilities
Release: %{real_release}%{?dist}
License: Dual MPL/GPL
Group: System Environment/Base
Provides: wlan-ng-utils

%description -n prism2-utils
Prism II Wireless 802.11b utilities.

%prep
%setup -n %{real_name}-%{real_version}

%{__perl} -pi.orig -e '
		s|^(PRISM2_.+)=.+$|$1=y|;
		s|^(LINUX_SRC)=.+$|$1=%{_usrsrc}/linux-%{kversion}-%{krelease}/|;
		s|^(TARGET_ROOT_ON_HOST)=.+$|%{buildroot}|;
	' config.in

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
./Configure -d
%{__make} all
cd src/prism2/driver/
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
./Configure -d
%{__make} all
cd src/prism2/driver/
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
cd -

%install
#makeinstall
%{__install} -Dp -m0644 etc/pcmcia/wlan-ng %{buildroot}%{_sysconfdir}/pcmcia/wlan-ng
%{__install} -Dp -m0644 etc/pcmcia/wlan-ng.conf %{buildroot}%{_sysconfdir}/pcmcia/wlan-ng.conf
%{__install} -Dp -m0644 etc/wlan/wlan.conf %{buildroot}%{_sysconfdir}/wlan/wlan.conf

%{__install} -Dp -m0644 man/nwepgen.man %{buildroot}%{_mandir}/man1/nwepgen.1
%{__install} -Dp -m0644 man/wlancfg.man %{buildroot}%{_mandir}/man1/wlancfg.1
%{__install} -Dp -m0644 man/wlanctl-ng.man %{buildroot}%{_mandir}/man1/wlanctl-ng.1
%{__install} -Dp -m0644 man/wland.man %{buildroot}%{_mandir}/man1/wland.1

%{__install} -Dp -m0755 src/wlancfg/wlancfg %{buildroot}%{_bindir}/wlancfg
%{__install} -Dp -m0755 src/nwepgen/nwepgen %{buildroot}%{_bindir}/nwepgen
%{__install} -Dp -m0755 src/wland/wland %{buildroot}%{_bindir}/wland
%{__install} -Dp -m0755 src/wlanctl/wlanctl %{buildroot}%{_bindir}/wlanctl

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-prism2
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-prism2
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-prism2
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n prism2-utils
%defattr(-, root, root, 0755)
%doc CHANGES COPYING FAQ LICENSE README THANKS TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/wlan/
%config %{_sysconfdir}/pcmcia/*
%{_bindir}/*

%changelog
* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
