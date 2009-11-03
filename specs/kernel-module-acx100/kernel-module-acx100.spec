# $Id$
# Authority: dag
# Upstream: <acx100-users$lists,sourceforge,net>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1


%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

#%define _with_smp %(test -f /usr/src/linux-%{kernel}/configs/kernel-%{kversion}-%{_target_cpu}-smp.config && echo 1 || echo 0)
%define _with_smp 0

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name acx100
%define real_version 0.2.0pre8

%define moduledir /kernel/drivers/net/wireless/acx100
%define modules src/acx_pci.o

Summary: Linux driver for the ACX100-based wireless cards
Name: kernel-module-acx100
Version: 0.2.0
Release: 1.pre8%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://acx100.sourceforge.net/

Source: http://dl.sf.net/acx100/acx100-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-source

%description
Linux driver for the ACX100-based wireless cards.


%package -n kernel-module-acx100-%{kernel}
Summary: Linux ACX100 wireless drivers
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}
Requires: kernel = %{kernel}
Requires: acx100-utils

Provides: kernel-module-acx100 = %{version}-%{release}
Provides: kernel-modules

%description -n kernel-module-acx100-%{kernel}
Linux driver for the ACX100-based wireless cards.

These drivers are built for kernel %{kernel}
and architecture %{_target_cpu}.
They might work with newer/older kernels.


%package -n kernel-smp-module-acx100-%{kernel}
Summary: Linux ACX100 wireless drivers for SMP
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}smp
Requires: kernel-smp = %{kernel}
Requires: acx100-utils

Provides: kernel-module-acx100 = %{version}-%{release}
Provides: kernel-modules

%description -n kernel-smp-module-acx100-%{kernel}
Linux SMP driver for the ACX100-based wireless cards.

These drivers are built for kernel %{kernel}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.


%package -n acx100-utils
Summary: ACX100 wireless driver add-ons
Group: System Environment/Base

Obsoletes: acx100
Provides: acx100

%description -n acx100-utils
ACX100 wireless driver utilities.

%prep
%setup -n %{real_name}-%{real_version}

####FIXME: Fix for defining own kernel version and get rid of Configure/config.mk (Please fix upstream)
%{__ln_s} -f /bin/true Configure
echo -n >config.mk

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{real_version}\nKernel version: %{kernel}\n"

export VERSION_CODE="$(grep LINUX_VERSION_CODE %{_libmoddir}/%{kernel}/build/include/linux/version.h | sed -e 's|[^0-9]\+$||g')"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/\(i.86\|athlon\)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
#	&>/dev/null
cd -

### Make UP module.
%{__make} clean
echo -n >config.mk
%{__make} %{?_smp_mflags} all V=1 \
	KERNEL_BUILD="%{_libmoddir}/%{kernel}/build" \
	KERNEL_OUTPUT="%{_libmoddir}/%{kernel}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}

%if %{_with_smp}
### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}smp" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/(i.86|athlon)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
	&>/dev/null
cd -

### Make SMP module.
%{__make} clean
echo -n >config.mk
%{__make} %{?_smp_mflags} all \
	KERNELRELEASE="%{kernel}"
	KERNEL_BUILD="%{_libmoddir}/%{kernel}/build" \
	KERNEL_OUTPUT="%{_libmoddir}/%{kernel}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}
%endif

### Build utilities.
%{__make} -C firmware extract \
	CFLAGS="%{optflags}"


%install
### Install utilities.
%{__install} -Dp -m0755 firmware/extract %{buildroot}%{_bindir}/acx100-extract
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/acx100/


%post -n kernel-module-acx100-%{kernel}
/sbin/depmod -ae %{kernel} || :

%postun -n kernel-module-acx100-%{kernel}
/sbin/depmod -ae %{kernel} || :


%post -n kernel-smp-module-acx100-%{kernel}
/sbin/depmod -ae %{kernel}smp || :

%postun -n kernel-smp-module-acx100-%{kernel}
/sbin/depmod -ae %{kernel}smp || :


%clean
%{__rm} -rf %{buildroot}


%files -n kernel-module-acx100-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kernel}%{moduledir}/


%if %{_with_smp}
%files -n kernel-smp-module-acx100-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kernel}smp%{moduledir}/
%endif


%files -n acx100-utils
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README TODO doc/ scripts/
%dir %{_sysconfdir}/acx100/
%{_bindir}/*


%changelog
* Sat Jun 26 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1.pre6
- Moved to new standard naming scheme.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1.pre6
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0.pre6
- Updated to release 0.2.0pre6.

* Wed Nov 05 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0.pre4
- Initial package. (using DAR)
