# Authority: dag

# Upstream: Mark Hessling <M.Hessling@qut.edu.au>

%define rname Regina

Summary: Regina Rexx interpreter.
Name: regina-rexx
Version: 3.2
Release: 0
License: LGPL
Group: Development/Languages
URL: http://regina-rexx.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/%{name}/%{rname}-REXX-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Obsoletes: Regina-REXX
Provides: Regina-REXX

%description
Regina is an implementation of a Rexx interpreter, compliant with the
ANSI Standard for Rexx (1996). It is also available on several other
operating systems. 

%package devel
Summary: Development files for Regina Rexx interpreter.
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description devel
Development files for Regina Rexx interpreter.

%prep
%setup -n %{rname}-%{version}
%{__perl} -pi.orig -e 's|\@sharedir\@|\@datadir\@|g; \
			s|\$\(sharedir\)|\$(datadir)/regina|g; \
			s|\@STARTUPDIR\@|\@sysconfdir\@/rc.d/init.d|g; \
			s|\$\(STARTUPDIR\)|\$(sysconfdir)/rc.d/init.d|g; \
			s|regina.\$\(OBJ\) \$\(LINKREG\)|regina.\$(OBJ) \$(EXECISER_DEP)|g;' \
	Makefile.in

%{__cat} <<EOF >rxstack.sysv
#!/bin/bash
#
# Init file for Regina REXX stack daemon
#
# chkconfig: - 80 20
# description: Regina REXX stack daemon
#
# processname: rxstack
# pidfile: %{_localstatedir}/run/rxstack.pid

# source function library
. %{_initrddir}/functions

[ -x %{_bindir}/rxstack ] || exit 1

RETVAL=0
prog="rxstack"
desc="Regina REXX Stack daemon"

start() {
	echo -n \$"Starting \$desc: "
	daemon \$prog -d
	RETVAL=\$?
	echo
	[ \$RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/\$prog
	return \$RETVAL
}

stop() {
	echo -n \$"Shutting down \$desc: "
	killproc \$prog -2
	RETVAL=\$?
	echo
	[ \$RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/\$prog
	return \$RETVAL
}

restart(){
	stop
	start
}

case "\$1" in
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
	[ -e %{_localstatedir}/lock/subsys/\$prog ] && restart
	RETVAL=\$?
	;;
  status)
	status \$prog
	RETVAL=\$?
	;;
  *)
	echo \$"Usage: \$0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit \$RETVAL
EOF

%build
%configure \
	--enable-posix-threads
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -m0755 rxstack.sysv %{buildroot}%{_initrddir}/rxstack

### FIXME: Fix broken REXX scripts
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}%{_datadir}/regina/*.rexx

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libtest?.so

%post 
/sbin/chkconfig --add rxstack
/sbin/ldconfig 2>/dev/null

%preun 
if [ "$1" -eq 0 ]; then
	/sbin/service rxstack stop &>/dev/null || :
	/sbin/chkconfig --del rxstack
fi
%postun 
/sbin/service rxstack condrestart &>/dev/null || :
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING-LIB HACKERS.txt README.Unix README_SAFE TODO trip/
%doc %{_mandir}/man1/*
%config %{_initrddir}/rxstack
%{_bindir}/regina
%{_bindir}/rexx
%{_bindir}/rxqueue
%{_bindir}/rxstack
%{_libdir}/*.so.*
%{_datadir}/regina/

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/regina-config
%{_libdir}/*.a
%{_includedir}/rexxsaa.h

%changelog
* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 3.2-0
- Updated to release 3.2.
- Added rxstack.sysv script.
- Fixed broken REXX scripts (containing buildroot)

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 3.1-0
- Updated to release 3.1.

* Thu Mar 20 2003 Dag Wieers <dag@wieers.com> - 3.0-0
- Initial package. (using DAR)
