# $Id$

# Authority: dag

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsUser: 0

%{?rhfc1:%define __cc gcc32}

%define _sbindir /sbin
%define _libdir /lib
%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname ibmasm
%define rrelease 1

%define moduledir /kernel/drivers/char/ibmasm
%define modules src/ibmasm.o src/ibmser.o

Summary: IBM Advanced System Management drivers
Name: kernel-module-ibmasm
Version: 2.02
Release: %{rrelease}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://www.pc.ibm.com/support/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.software.ibm.com/pc/pccbbs/pc_servers/ibmasm-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source
%{?rhfc1:BuildRequires: libusb-devel >= 0.1.5}
%{?rhel3:BuildRequires: libusb-devel >= 0.1.5}
%{?rh90:BuildRequires: libusb-devel >= 0.1.5}
%{?rh80:BuildRequires: libusb-devel >= 0.1.5}
%{?rh73:BuildRequires: libusb-devel >= 0.1.5}
%{?rhel21:BuildRequires: libusb-devel >= 0.1.5}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: ibmasm-utils

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description
IBM Advanced System Management drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ibmasm
Summary: IBM Advanced System Management drivers
Group: System Environment/Kernel
Release: %{rrelease}_%{kversion}_%{krelease}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: ibmasm-utils

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description -n kernel-smp-module-ibmasm
IBM Advanced System Management drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n ibmasm-utils
Summary: IBM Advanced System Management software
Release: %{rrelease}
Group: System Environment/Base

Obsoletes: ibmasm-utilities

%description -n ibmasm-utils
IBM Advanced System Management software.

%prep
%setup -n linux

%{__cat} <<'EOF' >>ibmspup.xinit
#!/bin/sh
%{_sbindir}/ibmspup &
EOF

%{__cat} <<'EOF' >ibmasm.sysv
#!/bin/bash
#
# Init file for IBM Advanced System Management drivers.
#
# Written by Dag Wieers <dag_wieers@be.ibm.com>.
#
# chkconfig: 2345 85 15
# description:  The IBM Advanced System Management Device Drivers allow\\
#              software to interact with the Advanced System Management\\
#              Processor or Adapter.
#
# processname: ibmspup

# source function library
. %{_initrddir}/functions

[ -x %{_sbindir}/ibmspup ] || exit 1

RETVAL=0
prog="ibmasm"
desc="IBM ASM drivers"

start() {
	echo -n $"Starting $desc ($prog): "
	%{_sbindir}/ibmspup
	RETVAL=$?
	if [ $RETVAL -eq 0 ]; then
		success
	else
		failure
	fi
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	%{_sbindir}/ibmspdown
	RETVAL=$?
	if [ $RETVAL -eq 0 ]; then
		success
	else
		failure
	fi
	echo
	[ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

restart() {
	stop
	start
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	restart
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/$prog ] && restart
	RETVAL=$?
	;;
  status)
	status $prog
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

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
%{__make} %{?_smp_mflags} -C src clean all \
	CPU="%{_arch}" \
	INC="%{_libmoddir}/%{kversion}-%{krelease}/build/include" \
	HASGUI="y" \
	NODRIVER="n" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

## Make SMP module.
%{__make} %{?_smp_mflags} -C src clean all \
	CPU="%{_arch}" \
	INC="%{_libmoddir}/%{kversion}-%{krelease}/build/include" \
	HASGUI="y" \
	NODRIVER="n" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Install binary software.
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
#%{__install} -m0755 ibmspup ibmspdown ibmspremove exe/ibmsprem exe/ibmsprem2 exe/ibmsphalt %{buildroot}%{_sbindir}
%{__install} -m0755 ibmspup ibmspdown exe/ibmsprem exe/ibmsprem2 exe/ibmsphalt %{buildroot}%{_sbindir}
%{__install} -m0755 shlib/libsysSp.so* %{buildroot}%{_libdir}
%{__install} -m0755 ibmasm.sysv %{buildroot}%{_initrddir}/ibmasm
%{__install} -m0755 ibmspup.xinit %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/ibmspup

### Clean up buildroot
%{__rm} -f %{buildroot}%{_sbindir}/ibmspremove

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

#%post -n kernel-smp-module-ibmasm
#/sbin/depmod -ae %{kversion}-%{krelease}smp || :

#%postun -n kernel-smp-module-ibmasm
#/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%post -n ibmasm-utils
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add ibmasm

### Create devices
rm -f /dev/ibmser /dev/ibmasm
mknod /dev/ibmser c 253 0
mknod /dev/ibmasm c 254 0
chgrp users /dev/ibmser /dev/ibmasm
chmod 666 /dev/ibmser /dev/ibmasm
for i in 1 2 3 4 5 6 7; do
	rm -f /dev/ibmser$i /dev/ibmasm$i
	mknod /dev/ibmser$i c 253 $i
	mknod /dev/ibmasm$i c 254 $i
	chgrp users /dev/ibmser$i /dev/ibmasm$i
	chmod 666 /dev/ibmser$i /dev/ibmasm$i
done

%preun -n ibmasm-utils
if [ $1 -eq 0 ]; then
        /sbin/service ibmasm stop &>/dev/null || :
        /sbin/chkconfig --del ibmasm
fi

%postun -n ibmasm-utils
/sbin/ldconfig 2>/dev/null
/sbin/service ibmasm condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ibmasm
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n ibmasm-utils
%defattr(-, root, root, 0755)
%doc README.TXT
%config %{_initrddir}/ibmasm
%config %{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_sbindir}/*
%{_libdir}/*.so*

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 2.02-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 2.02-0
- Updated to release 2.02.

* Mon Jun 16 2003 Dag Wieers <dag@wieers.com> - 1.19-0
- Initial package. (using DAR)
