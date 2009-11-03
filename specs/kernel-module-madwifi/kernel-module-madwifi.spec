# $Id$
# Authority: dag
# Upstream: <madwifi-devel$lists,sf,net>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1


%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name madwifi
%define real_version 20040312
%define real_release 0

%define moduledir /kernel/drivers/net/wireless/madwifi
%define modules ath_hal/ath_hal.o wlan/wlan.o driver/ath_pci.o

Summary: Linux driver for the Multiband Atheros Wifi
Name: kernel-module-madwifi
Version: 0.0.%{real_version}
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.mattfoster.clara.co.uk/madwifi-faq.htm

Source: http://dl.sf.net/madwifi/madwifi-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: madwifi-utils

Provides: kernel-modules

%description
Linux driver for the Multiband Atheros Wifi.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-madwifi
Summary: Linux SMP driver for the Multiband Atheros Wifi
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: madwifi-utils

Provides: kernel-modules

%description -n kernel-smp-module-madwifi
Linux SMP driver for the Multiband Atheros Wifi.

These drivers are build for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n madwifi-utils
Summary: Madwifi utilities
Release: %{real_release}%{?dist}
Group: System Environment/Base

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}

%description -n madwifi-utils
Madwifi utilities.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{real_version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_VERSION="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
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
	KERNEL_VERSION="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

### Build utilities
%{__make} %{?_smp_mflags} -C tools


%install
### Install utilities
%{__install} -Dp -m0755 tools/athstats %{buildroot}%{_bindir}/athstats

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-madwifi
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%post -n kernel-smp-module-madwifi
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-madwifi
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n madwifi-utils
%defattr(-, root, root, 0755)
%doc COPYRIGHT README
%{_bindir}/*

%changelog
* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.0.20040312-0
- Updated to new CVS release 20040312.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.0.20040107-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Jan 07 2004 Dag Wieers <dag@wieers.com> - 0.0.20040107-0
- Initial package. (using DAR)
