# $Id$

# Authority: dag

Summary: Sendmail milter for spamassassin
Name: spamass-milter
Version: 0.2.0
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://savannah.gnu.org/projects/spamass-milt/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/spamass-milt/spamass-milter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: spamassassin, sendmail-devel
Requires: spamassassin, sendmail

%description
A Sendmail milter (Mail Filter) library that pipes all incoming mail
(including things received by rmail/UUCP) through the SpamAssassin,
a highly customizable SpamFilter.

%prep
%setup

%{__cat} <<EOF >spamass-milter.sysconfig
### Override for your different local config
#SM_SOCKET=/var/run/spamass.sock

### Default parameter for spamass-milter is -f (work in the background)
### you may add another parameters here, see spamass-milter(1)
#SM_EXTRA_FLAGS="-m -r 15"
EOF

%{__cat} <<'EOF' >spamass-milter.sysv
#!/bin/bash
#
# Init file for Spamassassin sendmail milter.
#
# chkconfig: - 80 20
# description: spamass-milter is a daemon which hooks into sendmail and routes \
#              email messages to spamassassin
#
# processname: spamass-milter
# config: %{_sysconfdir}/sysconfig/spamass-milter
# pidfile: %{_localstatedir}/run/spamass-milter

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

[ -x %{_sbindir}/spamass-milter ] || exit 1

### Default variables
SOCKET="%{_localstatedir}/run/spamass.sock"
EXTRA_FLAGS="-m -r 15"
SYSCONFIG="%{_sysconfdir}/sysconfig/spamass-milter"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="spamass-milter"
desc="Spamassassin sendmail milter"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -p $SOCKET -f $EXTRA_FLAGS
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	killproc $prog
	RETVAL=$?
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/sysconfig/
%{__install} -m0755 spamass-milter.sysv %{buildroot}%{_initrddir}/spamass-milter
%{__install} -m0644 spamass-milter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/spamass-milter

%post
/sbin/chkconfig --add spamass-milter

%preun
if [ $1 -eq 0 ]; then
    /sbin/service spamass-milter stop &>/dev/null || :
    /sbin/chkconfig --del spamass-milter
fi

%postun
/sbin/service spamass-milter condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config %{_initrddir}/spamass-milter
%{_sbindir}/*

%changelog
* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package. (using DAR)
