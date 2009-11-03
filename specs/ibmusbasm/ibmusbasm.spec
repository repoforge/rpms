# $Id$
# Authority: dag
# Upstream: <fwtreas$us,ibm,com>

%define _sbindir /sbin
%define _libdir /%{_lib}

%define real_version 1.10-2

Summary: IBM USB Advanced System Management (ASM II) Device Drivers
Name: ibmusbasm
Version: 1.10.2
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.pc.ibm.com/support/

Source: ftp://ftp.software.ibm.com/pc/pccbbs/pc_servers/ibmusbasm-%{real_version}.i386.rpm
#Source: ftp://ftp.software.ibm.com/pc/pccbbs/pc_servers/ibmusbasm-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: ibmasm, ibmasr, ibmasm-src-redhat, ibmasm-src-suse, ibmasm-utils
BuildRequires: libusb-devel >= 0.1.5, /usr/bin/readlink
Requires: libusb

%description
IBM USB Advanced System Management (ASM II) Device Driver package

%prep
%setup -c -T
rpm2cpio %{SOURCE0} | cpio -idv "*/ibmusbasm-src.tgz"
tar -xvzf usr/local/ibmusbasm/ibmusbasm-src.tgz

### FIXME: Make files writable !
%{__chmod} u+rwx -R .

LIBUSB="$(readlink %{_prefix}/%{_lib}/libusb.so)"
%{__perl} -pi.orig -e "s|libusb.so|$LIBUSB|g" linux/src/ibmasm.c

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
%{__make} %{?_smp_mflags} -C linux/src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 linux/ibmspup %{buildroot}%{_sbindir}/ibmspup
%{__install} -Dp -m0755 linux/ibmspdown %{buildroot}%{_sbindir}/ibmspdown
%{__install} -Dp -m0755 linux/src/ibmasm %{buildroot}%{_sbindir}/ibmasm
%{__install} -Dp -m0755 linux/shlib/libsysSp.so %{buildroot}%{_libdir}/libsysSp.so

%{__install} -Dp -m0755 ibmasm.sysv %{buildroot}%{_initrddir}/ibmasm

%post
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add ibmasm
/sbin/service ibmasm restart &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service ibmasm stop &>/dev/null || :
        /sbin/chkconfig --del ibmasm
fi

%postun
/sbin/ldconfig 2>/dev/null
/sbin/service ibmasm condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc linux/README.TXT linux/ibmasm.initscript
%config %{_initrddir}/ibmasm
%{_sbindir}/ibm*
%{_libdir}/libsysSp.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10.2-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 15 2004 Dag Wieers <dag@wieers.com> - 1.10.2-1
- Initial package. (using DAR)
