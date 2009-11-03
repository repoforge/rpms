# $Id$
# Authority: dag
# Upstream: <atmelwlandriver-devel>

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

%define real_name atmelwlandriver
%define real_release 1

%define moduledir /kernel/drivers/net/wireless/airo_mpi
%define modules airo_mpi.o

Summary: Linux driver for the Atmel Wireless devices
Name: kernel-module-atmel-wlan
Version: 3.2.4.4
Release: %{real_release}.%{real_version}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://atmelwlandriver.sourceforge.net/

Source: http://dl.sf.net/atmelwlandriver/atmelwlandriver-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description
Linux driver for the Atmel Wireless devices.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-atmel-wlan
Summary: Linux SMP driver for the Cisco 350 miniPCI series
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description -n kernel-smp-module-atmel-wlan
Linux SMP driver for the Atmel Wireless devices.

These drivers are build for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -n %{real_name}-%{real_version}

### FIXME: Fix Makefile to override KERNEL_VERSION
%{__perl} -pi.orig -e 's|^#(KERNEL_VERSION)=.*$|$1 = %{kversion}-%{krelease}|' Makefile

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

%install
### Install utilities

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-atmel-wlan
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-atmel-wlan
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc airo_mpi.HOWTO.txt
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-atmel-wlan
%defattr(-, root, root, 0755)
%doc airo_mpi.HOWTO.txt
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 3.2.4.4-1
- Initial package. (using DAR)
