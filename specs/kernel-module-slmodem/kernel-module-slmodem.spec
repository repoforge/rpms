# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

####FIXME: Only 2.7.10 works properly, 2.7.14 (and others) are broken.

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/char/slmdm
%define modules drivers/slamr.o drivers/slusb.o
#define modules slamrmo.o slfax.o slmdm.o slusb.o

%define real_name slmodem
%define real_release 0

Summary: Linux Smartlink Linmodem drivers
Name: kernel-module-slmodem
Version: 2.9.6
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: Proprietary
Group: System Environment/Kernel
URL: http://linmodems.technion.ac.il/packages/smartlink/

Source: ftp://ftp.smlink.com/linux/unsupported/slmodem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source, pciutils
Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: slmodem-utils

Obsoletes: kernel-module-slmdm
Provides: kernel-modules

%description
Linux Smartlink Linmodem drivers.

HW drivers for:
  + HAMR5600 based AMR/CNR/MDC/ACR modem cards
  + SmartPCI56, SmartPCI561 based PCI modem cards
  + SmartUSB56 based USB modem

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

#%package -n kernel-smp-module-slmodem
#Release: %{real_release}_%{kversion}_%{krelease}
#Summary: Linux Smartlink Linmodem drivers.
#Group: System Environment/Kernel
#
#Requires: kernel = %{kversion}-%{krelease}, %{real_name}
#Obsoletes: kernel-smp-module-slmdm
#Provides: kernel-modules
#
#%description -n kernel-smp-module-slmodem
#Linux Smartlink Linmodem drivers for SMP.
#
#HW drivers for:
#  + HAMR5600 based AMR/CNR/MDC/ACR modem cards
#  + SmartPCI56, SmartPCI561 based PCI modem cards
#  + SmartUSB56 based USB modem
#
#These drivers are built for kernel %{kversion}-%{krelease}smp.
#They might work with newer/older kernels.

%package -n slmodem-utils
Summary: Linux Smartlink Linmodem utilities
Release: %{real_release}%{?dist}
Group: System Environment/Base

Obsoletes: %{real_name}, slmdm, slmdm-utils
Provides: %{real_name}, slmdm, slmdm-utils

%description -n slmodem-utils
Linux Smartlink Linmodem utilities.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Patch amrmo_init.c to make the driver load. (Fix upstream please)
#%{__perl} -pi.orig -e 's|^(#define PCI_DEVICE_ID_ICH3\s+)0x2486$|${1}0x24C6|' amrmo_init.c

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/var/lib|\$(localstatedir)/lib|;
		s|/usr/sbin|\$(sbindir)|;
	' Makefile

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
%{__make} %{?_smp_mflags} clean all \
	EXTFLAGS="%{optflags}" \
	KERNEL_DIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

#### Prepare SMP kernel.
#cd %{_usrsrc}/linux-%{kversion}-%{krelease}
#%{__make} -s distclean &>/dev/null
#%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
#%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
#cd -

#### Make SMP module.
#%{__make} %{?_smp_mflags} clean all \
#	EXTFLAGS="%{optflags}" \
#	KERNEL_DIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
#%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
#%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Install utilities
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/slmodem/ \
			%{buildroot}/dev/
%{__install} -Dp -m0755 modem/slmodemd %{buildroot}%{_sbindir}/slmodemd
for i in 0 1 2 3; do
	touch %{buildroot}/dev/slamr$i %{buildroot}/dev/slusb$i
done

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :
for i in 0 1 2 3; do
	rm -f /dev/slamr$i /dev/slusb$i /dev/ttySL$i
	mknod -m660 /dev/slamr$i c 212 $i
	mknod -m660 /dev/slusb$i c 213 $i
	chown root:uucp /dev/slamr$i /dev/slusb$i
done

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

#%post -n kernel-smp-module-slmodem
#/sbin/depmod -ae %{kversion}-%{krelease}smp || :
#for i in 0 1 2 3; do
#	rm -f /dev/slamr$i /dev/slusb$i
#	mknod -m660 /dev/slamr$i c 212 $i
#	mknod -m660 /dev/slusb$i c 213 $i
#	chown root:uucp /dev/slamr$i /dev/slusb$i
#done
#
#%postun -n kernel-smp-module-slmodem
#/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
%ghost /dev/slamr*
%ghost /dev/slusb*

#%files -n kernel-smp-module-slmodem
#%defattr(-, root, root, 0755)
#%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/
#%ghost /dev/slamr*
#%ghost /dev/slusb*

%files -n slmodem-utils
%defattr(-, root, root, 0755)
%doc Changes README*
#%{_sysconfdir}/country.dat
%{_sbindir}/*

%changelog
* Fri Feb 20 2004 Dag Wieers <dag@wieers.com> - 2.9.6-0
- Updated to release 2.9.6.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 2.9.5-0
- Updated to release 2.9.5.

* Thu Jan 01 2004 Dag Wieers <dag@wieers.com> - 2.9.4-0
- Renamed base-package to kernel-module-slmodem.

* Tue Dec 09 2003 Dag Wieers <dag@wieers.com> - 2.9.3-0
- Updated to release 2.9.3.

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 2.9.2-0
- Updated to release 2.9.2.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 2.7.10-0
- Fixed the problem with 2.7.14.
- Renamed slmdm to slmdm-utils.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 2.7.14-0
- Initial package. (using DAR)
