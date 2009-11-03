# $Id$
# Authority: dag
# Upstream: <modem,support$linuxant,com>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name hsfmodem
%define real_version 6.03.00lnxt04011900full
%define real_release 1.lnxt04011900full

%define moduledir /kernel/drivers/char/hsfmodem
%define modules hsfengine.o hsfmc97ali.o hsfmc97ich.o hsfmc97via.o hsfosspec.o hsfpcibasic2.o hsfserial.o hsfsoar.o

Summary: Linux Conexant HSF Softmodem drivers
Name: kernel-module-hsfmodem
Version: 6.03.00
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: Copyright (c) 2003 Linuxant inc. All rights reserved.
Group: System Environment/Kernel
URL: http://www.linuxant.com/drivers/hsf/

Source: http://www.linuxant.com/drivers/hsf/free/archive/hsfmodem-%{real_version}/hsfmodem-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


ExclusiveArch: athlon i686 i586 i386
BuildRequires: kernel-source, pciutils

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: hsfmodem-utils

Provides: kernel-modules

%description
Linux Conexant HSF Softmodem drivers.

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

%package -n kernel-smp-module-hsfmodem
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
Summary: Linux Conexant HSF Softmodem drivers for SMP
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: hsfmodem-utils
Provides: kernel-modules

%description -n kernel-smp-module-hsfmodem
Linux Conexant HSF Softmodem drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp.
They might work with newer/older kernels.

%package -n hsfmodem-utils
Summary: Linux Conexant HSF Softmodem utilities
Release: %{real_release}%{?dist}
Group: System Environment/Kernel

Obsoletes: hsflinmodem, %{real_name}
Provides: %{real_name}

%description -n hsfmodem-utils
Linux Conexant HSF Softmodem utilities.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\nArchitecture: %{_target_cpu}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
#%{__make} %{?_smp_mflags} clean all \
#	EXTFLAGS="%{optflags}" \
#	KERNEL_INCLUDES="%{_libmoddir}/%{kversion}-%{krelease}/build/include"
%{__make} %{?_smp_mflags} -C modules clean all modules_install \
	KERNELSRC="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	DISTRO_CFLAGS="-D__BOOT_KERNEL_H_ -D__BOOT_KERNEL_UP=1 -D__MODULE_KERNEL_%{_target_cpu}=1" \
	CNXT_MODS_DIR="../%{real_name}-up/"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{real_name}-up/*.o %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
#%{__make} %{?_smp_mflags} clean all \
#	EXTFLAGS="%{optflags}" \
#	KERNEL_INCLUDES="%{_libmoddir}/%{kversion}-%{krelease}/build/include"
%{__make} %{?_smp_mflags} -C modules clean all modules_install \
	KERNELSRC="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	DISTRO_CFLAGS="-D__BOOT_KERNEL_H_ -D__BOOT_KERNEL_SMP=1 -D__MODULE_KERNEL_%{_target_cpu}=1" \
	CNXT_MODS_DIR="../%{real_name}-smp/"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{real_name}-smp/*.o %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

### Make utilities.
%{__make} %{?_smp_mflags} clean all

%install
### Install utilities.
%makeinstall \
	ROOT="%{buildroot}"
%{__install} -d -m0755 %{buildroot}/dev/
touch %{buildroot}/dev/ttySHSF0 %{buildroot}/dev/hsfdiag0

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :
if [ ! -e /dev/ttySHSF0 ]; then
	mknod -m660 /dev/ttySHSF0 c 240 64
	mknod -m660 /dev/hsfdiag0 c 243 0
	chown root:uucp /dev/ttySHSF0 /dev/hsfdiag0
	if [ ! -e /dev/modem ]; then
		ln -s /dev/ttySHSF0 /dev/modem
	fi
fi

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-hsfmodem
/sbin/depmod -ae %{kversion}-%{krelease}smp || :
if [ ! -e /dev/ttySHSF0 ]; then
	mknod -m660 /dev/ttySHSF0 c 240 64
	mknod -m660 /dev/hsfdiag0 c 243 0
	chown root:uucp /dev/ttySHSF0 /dev/hsfdiag0
	if [ ! -e /dev/modem ]; then
		ln -s /dev/ttySHSF0 /dev/modem
	fi
fi

%postun -n kernel-smp-module-hsfmodem
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%preun -n hsfmodem-utils
%{_sbindir}/hsfstop
if [ $1 -eq 0 ]; then
	%{_sbindir}/hsfconfig --remove
fi

%post -n hsfmodem-utils
%{_sbindir}/hsfconfig --auto

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
%ghost /dev/ttySHSF0
%ghost /dev/hsfdiag0

%files -n kernel-smp-module-hsfmodem
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/
%ghost /dev/ttySHSF0
%ghost /dev/hsfdiag0

%files -n hsfmodem-utils
%defattr(-, root, root, 0755)
%doc BUGS CHANGES CREDITS FAQ INSTALL LICENSE README
%config %{_sysconfdir}/hsfmodem/
%{_sbindir}/*

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 6.03.00-1.lnxt04011900full
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Fri Feb 20 2004 Dag Wieers <dag@wieers.com> - 6.03.00-0.lnxt04011900full
- Updated to release 6.03.00.lnxt04011900full.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 6.03.00-0.lnxt03091800free
- Initial package. (using DAR)
