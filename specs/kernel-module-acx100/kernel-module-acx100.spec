# $Id$
# Authority: dag
# Upstream: <acx100-users@lists.sourceforge.net>

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%{?dist: %{expand %%define %dist 1}}

%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name acx100
%define real_version 0.2.0pre6
%define real_release 1.pre6

%define moduledir /kernel/drivers/net/wireless/acx100
%define modules src/acx100_pci.o

Summary: Linux driver for the ACX100-based wireless cards
Name: kernel-module-acx100
Version: 0.2.0
Release: %{real_release}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://acx100.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/acx100/acx100-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: acx100-utils

Obsoletes: kernel-%{real_name}
Provides: kernel-%{real_name}
Provides: kernel-modules

%description
Linux driver for the ACX100-based wireless cards.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-acx100
Release: %{real_release}_%{kversion}_%{krelease}
Summary: Linux ACX100 wireless drivers for SMP
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: acx100-utils

Obsoletes: kernel-%{real_name}
Provides: kernel-%{real_name}
Provides: kernel-modules

%description -n kernel-smp-module-acx100
Linux SMP driver for the ACX100-based wireless cards.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n acx100-utils
Summary: ACX100 wireless driver add-ons
Release: %{real_release}
Group: System Environment/Base

Obsoletes: acx100
Provides: acx100

%description -n acx100-utils
ACX100 wireless driver utilities.

%prep
%setup -n %{real_name}-%{real_version}

### FIXME: Fix for defining own kernel version and get rid of Configure/config.mk (Please fix upstream)
%{__ln_s} -f /bin/true Configure
echo -n >config.mk

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{real_version}\nKernel version: %{kversion}-%{krelease}\n"

export VERSION_CODE="$(grep LINUX_VERSION_CODE %{_libmoddir}/%{kversion}-%{krelease}/build/include/linux/version.h | sed -e 's|[^0-9]\+$||g')"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_BUILD="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_BUILD="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

### Build utilities.
%{__make} -C firmware extract \
	CFLAGS="%{optflags}"

%install
### Install utilities.
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sysconfdir}/acx100/
%{__install} -m0755 firmware/extract %{buildroot}%{_bindir}/acx100-extract

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-acx100
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-acx100
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-acx100
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n acx100-utils
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README TODO doc/ scripts/
%dir %{_sysconfdir}/acx100/
%{_bindir}/*

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1.pre6
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0.pre6
- Updated to release 0.2.0pre6.

* Wed Nov 05 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0.pre4
- Initial package. (using DAR)
