# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1


%{?fc1:%define __cc gcc32}

%define _sbindir /sbin
%define _libdir /%{_lib}
%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%{expand: %define _with_smp %(test -f /usr/src/linux-%{kernel}/configs/kernel-%{kversion}-%{_target_cpu}-smp.config && echo 1 || echo 0)}
#%define _with_smp 0

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ibmasm

%define moduledir /kernel/drivers/char/ibmasm
%define modules src/ibmasm.o src/ibmser.o

Summary: IBM Advanced System Management drivers
Name: kernel-module-ibmasm
Version: 2.05
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.pc.ibm.com/support/

#Source: ftp://ftp.software.ibm.com/pc/pccbbs/pc_servers/ibmasm-%{real_version}.src.rpm
Source: ftp://ftp.software.ibm.com/pc/pccbbs/pc_servers/ibmasm-src-redhat-wrp136a.rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-source
#BuildRequires: libusb-devel >= 0.1.5

%description
IBM Advanced System Management drivers.

%package -n kernel-module-ibmasm-%{kernel}
Summary: IBM Advanced System Management drivers
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}
Requires: kernel = %{kernel}
Requires: ibmasm-utils

Provides: kernel-module-ibmasm = %{version}-%{release}
Provides: kernel-modules
Conflicts: ibmasm, ibmasr, ibmasm-src-redhat, ibmasm-src-suse, ibmusbasm

%description -n kernel-module-ibmasm-%{kernel}
IBM Advanced System Management drivers.

These drivers are built for kernel %{kernel}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ibmasm-%{kernel}
Summary: IBM Advanced System Management drivers for SMP
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}smp
Requires: kernel-smp = %{kernel}
Requires: ibmasm-utils

Provides: kernel-module-ibmasm = %{version}-%{release}
Provides: kernel-modules
Conflicts: ibmasm, ibmasr, ibmasm-src-redhat, ibmasm-src-suse, ibmusbasm

%description -n kernel-smp-module-ibmasm-%{kernel}
IBM Advanced System Management drivers for SMP.

These drivers are built for kernel %{kernel}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n ibmasm-utils
Summary: IBM Advanced System Management software
Group: System Environment/Base

Obsoletes: ibmasm-utilities
Conflicts: ibmasm, ibmasr, ibmasm-src-redhat, ibmasm-src-suse, ibmusbasm

%description -n ibmasm-utils
IBM Advanced System Management software.

%prep
%setup -c -T
rpm2cpio %{SOURCE0} | cpio -idv "*/ibmasm-src-redhat.tgz"
tar -xvzf usr/local/ibmasm/ibmasm-src-redhat.tgz

### FIXME: Make files writable !
%{__chmod} u+rwx -R .


cd ibmasm-src

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
echo -e "\nDriver version: %{version}\nKernel version: %{kernel}\n"
cd ibmasm-src

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/\(i.86\|athlon\)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
	&>/dev/null
cd -

### Make UP module.
%{__make} %{?_smp_mflags} -C src clean all \
	CPU="%{_arch}" \
	INC="%{_libmoddir}/%{kernel}/build/include" \
	HASGUI="y" \
	NODRIVER="n" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}

%if %{_with_smp}
### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}smp" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/(i.86|athlon)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
	&>/dev/null
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} -C src clean all \
	CPU="%{_arch}" \
	INC="%{_libmoddir}/%{kernel}/build/include" \
	HASGUI="y" \
	NODRIVER="n" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}
%endif

%install
cd ibmasm-src

### Install binary software.
%{__install} -d -m0755 %{buildroot}%{_sbindir}
#%{__install} -p -m0755 ibmspup ibmspdown ibmspremove exe/ibmsprem exe/ibmsprem2 exe/ibmsphalt %{buildroot}%{_sbindir}
%{__install} -p -m0755 ibmspup ibmspdown exe/ibmsprem exe/ibmsprem2 exe/ibmsphalt %{buildroot}%{_sbindir}
%{__install} -Dp -m0755 shlib/libsysSp.so %{buildroot}%{_libdir}/libsysSp.so
%{__install} -Dp -m0755 ibmasm.sysv %{buildroot}%{_initrddir}/ibmasm
%{__install} -Dp -m0755 ibmspup.xinit %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/ibmspup

### Clean up buildroot
%{__rm} -f %{buildroot}%{_sbindir}/ibmspremove

%post -n kernel-module-ibmasm-%{kernel}
/sbin/depmod -ae %{kernel} || :

%postun -n kernel-module-ibmasm-%{kernel}
/sbin/depmod -ae %{kernel} || :

%post -n kernel-smp-module-ibmasm-%{kernel}
/sbin/depmod -ae %{kernel}smp || :

%postun -n kernel-smp-module-ibmasm-%{kernel}
/sbin/depmod -ae %{kernel}smp || :

%post -n ibmasm-utils
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add ibmasm
/sbin/service ibmasm restart &>/dev/null || :

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

%files -n kernel-module-ibmasm-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kernel}%{moduledir}/

%if %{_with_smp}
%files -n kernel-smp-module-ibmasm-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kernel}smp%{moduledir}/
%endif

%files -n ibmasm-utils
%defattr(-, root, root, 0755)
%doc ibmasm-src/README.TXT ibmasm-src/ibmasm.initscript
%config %{_initrddir}/ibmasm
%config %{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_sbindir}/ibm*
%{_libdir}/libsysSp.so

%changelog
* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 2.05-1
- Moved to new standard naming scheme.
- Updated to release 2.05.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 2.02-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 2.02-0
- Updated to release 2.02.

* Mon Jun 16 2003 Dag Wieers <dag@wieers.com> - 1.19-0
- Initial package. (using DAR)
