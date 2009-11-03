# $Id$

# Authority: dag

Name: openslp
Summary: OpenSLP implementation of Service Location Protocol V2
Version: 1.2.1
Release: 0.2%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.openslp.org/

Source: http://dl.sf.net/openslp/openslp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Provides: openslp libslp.so libslp.so.0 slpd
Obsoletes: openslp-server

%description
Service Location Protocol is an IETF standards track protocol that
provides a framework to allow networking applications to discover the
existence, location, and configuration of networked services in
enterprise networks.

OpenSLP is an open source implementation of the SLPv2 protocol as defined
by RFC 2608 and RFC 2614.  This package includes the daemon, libraries, header
files and documentation.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

# This file is embedded here instead of being another source in order
# to the prefix directory
%{__cat} <<EOF >slpd.sysv
#!/bin/bash
#
# Start/Stop the OpenSLP SA daemon (slpd).
#
# chkconfig: 345 13 87
# description: slpd - OpenSLP daemon for the Service Location Protocol
#
# processname: slpd
# config: %{_sysconfdir}/slp.conf
# config: %{_sysconfdir}/sysconfig/slpd
# pidfile: %{_localstatedir}/run/sshd.pid

# Source function library.
. %{_initrddir}/functions

[ -f %{_sysconfdir}/sysconfig/slpd ] && . %{_sysconfdir}/sysconfig/slpd

[ -x %{_sbindir}/slpd ] || exit 1

RETVAL=0
prog="slpd"

#///////////// multicast_route_set() //////////////#
#                                                  #
# Does nothing if a route exists that supports     #
# multicast traffic. If no routes supporting       #
# multicast traffic exists, the function tries to  #
# add one.  A 0 is returned on success and a 1     #
# on failure. One parameter must be passed in.     #
# This variable determins verbosity. If parameter  #
# is non-zero debugging will appear                #
#                                                  #
#//////////////////////////////////////////////////#
multicast_route_set()
{
	PING_OPTIONS_1='-c1 -w1'
	PING_OPTIONS_2='-c1 -i1'
	MULTICAST_ADDRESS='239.255.255.253'
	TMP_FILE=/tmp/route.check
	PING_ERROR_NO_ROUTE='unreachable'

	MSG_FAILED_TO_FIND='Failed to Detect Multicast Route'
	MSG_SUCCESS_ON_FIND='Multicast Route Enabled'
	MSG_ADDING_ROUTE='Attempting to Add Multicast Route ...'
	MSG_FAILED_TO_ADD=' FAILED - Route NOT Added.'
	MSG_SUCCES_ON_ADD=' SUCCESS - Route Added.'

	CMD_GET_INTERFACE="netstat -i | awk 'BEGIN{}(NR>2)&&(!/^lo*/){print \$1}'"
	CMD_ADD_ROUTE="route add -net 224.0.0.0 netmask 240.0.0.0"

	ping \$PING_OPTIONS_1 \$MULTICAST_ADDRESS 2> \$TMP_FILE 1> /dev/null

	if [ \$? = 2 ]; then
		ping \$PING_OPTIONS_2 \$MULTICAST_ADDRESS 2> \$TMP_FILE 1> /dev/null
	fi

	grep \$PING_ERROR_NO_ROUTE \$TMP_FILE > /dev/null 2>&1
	err_unreachable_found=\$?

	#If errors, add route. Otherwise, do nothing
	if [ -s \$TMP_FILE ] && [ \$err_unreachable_found = 0 ]; then

		if [ \$1 != 0 ]; then
			echo \$MSG_FAILED_TO_FIND
			echo \$MSG_ADDING_ROUTE
		fi

		\$CMD_ADD_ROUTE `eval \$CMD_GET_INTERFACE` > /dev/null 2>&1
		retval=\$?

		if [ \$1 != 0 ]; then
			if [ \$retval = 0 ]; then
				echo \$MSG_SUCCES_ON_ADD
			else
				echo \$MSG_FAILED_TO_ADD
			fi
		fi
	else
		if [ \$1 != 0 ]; then
			echo -n \$MSG_SUCCESS_ON_FIND
		fi
		retval=0
	fi

	rm -f \$TMP_FILE # Clean up
	return \$retval
}

start() {
	echo -n \$"Starting \$prog: "

	# Attempt to guarantee a multicast route...
	multicast_route_set 1
	multicast_enabled=\$?
	if [ "\$multicast_enabled" != "0" ] ; then
		echo "Failure: No Route Available for Multicast Traffic"
		exit 1
	fi

	daemon %{_sbindir}/slpd \$OPTIONS
	RETVAL=\$?
	echo
        [ \$RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/slpd
        return \$RETVAL
}

stop() {
	echo -n \$"Shutting down \$prog: "
	killproc slpd
	RETVAL=\$?
        [ \$RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/crond
	echo
        return \$RETVAL
}

restart() {
	stop
	start
}

# See how we were called.
case "\$1" in
  start)
	start
	;;
  stop)
	stop
        ;;
  restart)
	restart
	;;
  condrestart)
	[ -f %{_localstatedir}/lock/subsys/crond ] && restart || :
	;;
  status)
	status slpd
	;;
  *)
	echo \$"Usage: \$0 {start|stop|restart|status}"
	exit 1
esac

exit \$?
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0755 slpd.sysv %{buildroot}%{_initrddir}/slpd

%{__rm} -rf %{buildroot}/usr/doc/
%{__rm} -rf $(find doc/ -name "CVS" -type d)

%post
/sbin/chkconfig --add slpd
/sbin/ldconfig 2>/dev/null

%preun
if [ $1 -eq 0 ]; then
        /sbin/chkconfig --del slpd
fi

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%doc doc/html/IntroductionToSLP doc/html/UsersGuide doc/html/faq.html
%config %{_sysconfdir}/*
%config %{_initrddir}/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/ProgrammersGuide doc/rfc/*.html doc/rfc/*.txt
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.1-0.2
- Rebuild for Fedora Core 5.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 1.0.11-0
- Initial package. (using DAR)
