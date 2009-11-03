# $Id$
# Authority: dag
# Upstream: Oliver Kurth <oku$masqmail,cx>

Summary: Offline mail server with pop3 client support
Name: masqmail
Version: 0.2.20
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://innominate.org/kurth/masqmail/

Source: http://innominate.org/kurth/masqmail/download/masqmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: /usr/bin/mailq, /usr/sbin/sendmail, MTA, smtpd, smtpdaemon
BuildRequires: glib-devel, glib2-devel

%description
MasqMail is a mail server designed for hosts that do not have a
permanent internet connection eg. a home network or a single host at
home. It has special support for connections to different ISPs. It
replaces sendmail or other MTAs such as qmail or exim.

%prep
%setup

### Don't change ownerships
%{__perl} -pi.orig -e '
		s| -o \S+ -g \S+ | |;
		s|\@with_confdir\@|\$(sysconfdir)/masqmail|;
		s|\@with_logdir\@|\$(localstatedir)/log/masqmail|;
		s|\@with_spooldir\@|\$(localstatedir)/spool/masqmail|;
	' Makefile.in

### Change incorrect sample config files
%{__perl} -pi.orig -e 's|^(remote_port)|#$1|' examples/masqmail.conf

%{__cat} <<EOF >masqmail.sysconfig
### Options for masqmail
### See the masqmail(8) manpage

OPTIONS="-bd -q30m"
EOF

%{__cat} <<'EOF' >masqmail.sysv
#!/bin/bash
#
# Init file for Masqmail Offline mail server
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 54 46
# description: Masqmail
#
# processname: masqmail
# config: %{_sysconfdir}/masqmail.conf
# pidfile: %{_localstatedir}/run/masqmail

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

### Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0

[ -x %{_sbindir}/masqmail ] || exit 1
[ -r %{_sysconfdir}/masqmail/masqmail.conf ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/masqmail"
OPTIONS="-bd -q30m"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="masqmail"
desc="Offline mail server"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon %{_sbindir}/$prog $OPTIONS
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
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF


%build
%configure \
	--enable-auth \
	--enable-ident \
	--enable-maildir \
	--enable-mserver \
	--with-libcrypto \
	--with-user="mail" \
	--with-group="mail"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

#makeinstall
%{__install} -Dp -m0755 src/mservdetect %{buildroot}%{_bindir}/mservdetect
%{__install} -Dp -m0755 src/masqmail %{buildroot}%{_sbindir}/masqmail
%{__ln_s} -f masqmail %{buildroot}%{_sbindir}/sendmail.masqmail
%{__ln_s} -f ../sbin/masqmail %{buildroot}%{_bindir}/mailq.masqmail

%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__ln_s} -f ../sbin/masqmail %{buildroot}%{_libdir}/sendmail.masqmail

%{__install} -Dp -m0755 masqmail.sysv %{buildroot}%{_initrddir}/masqmail

%{__install} -d -m0755 %{buildroot}%{_mandir}/man{5,8}/
%{__install} -p  -m0644 docs/man/*.5 %{buildroot}%{_mandir}/man5/
%{__install} -p -m0644 docs/man/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -Dp -m0644 masqmail.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/masqmail
%{__install} -Dp -m0644 examples/masqmail.conf %{buildroot}%{_sysconfdir}/masqmail/masqmail.conf
%{__install} -Dp -m0644 examples/example.route %{buildroot}%{_sysconfdir}/masqmail/example.route
%{__install} -Dp -m0644 examples/example.get %{buildroot}%{_sysconfdir}/masqmail/example.get

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/masqmail/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/spool/masqmail/{input,popuidl}/

%post
/sbin/chkconfig --add masqmail

/usr/sbin/alternatives --install /usr/sbin/sendmail mta /usr/sbin/sendmail.masqmail 40 \
	--slave /usr/bin/mailq mta-mailq /usr/bin/mailq.masqmail \
	--slave /usr/lib/sendmail mta-sendmail /usr/lib/sendmail.masqmail \
	--initscript masqmail

%preun
if [ $1 -eq 0 ]; then
	/sbin/service masqmail stop &>/dev/null
	/sbin/chkconfig --del masqmail
	/usr/sbin/alternatives --remove mta /usr/sbin/sendmail.masqmail
fi

%postun
/sbin/service postfix condrestart &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL* NEWS README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/masqmail/
%config(noreplace) %{_sysconfdir}/sysconfig/masqmail
%config %{_initrddir}/*
%{_sbindir}/sendmail.masqmail
%{_bindir}/mailq.masqmail
%{_bindir}/mservdetect
%{_libdir}/sendmail.masqmail

%defattr(4755, root, root, 0755)
%{_sbindir}/masqmail

%defattr(-, mail, mail, 0755)
%{_localstatedir}/log/masqmail/
%{_localstatedir}/spool/masqmail/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.20-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.2.20-1
- Initial package. (using DAR)
