# $Id$

# Authority: dag
# Upstream: Timo Sirainen <tss@iki.fi>

Summary: Dovecot secure IMAP server
Name: dovecot
Version: 0.99.10.4
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://dovecot.procontrol.fi/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dovecot.procontrol.fi/dovecot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Prereq: /usr/sbin/useradd, /usr/sbin/usermod
BuildRequires: openssl-devel
BuildRequires: openldap-devel, postgresql-devel, cyrus-sasl-devel
%{!?rh62:BuildRequires: pam-devel}
%{?rh62:BuildRequires: pam}

%description
Dovecot is an IMAP and POP3 server for Linux/UNIX-like systems,
written with security primarily in mind. Although it's written
with C, it uses several coding techniques to avoid most of the
common pitfalls.

Dovecot can work with standard mbox and maildir formats and it's fully
compatible with UW-IMAP and Courier IMAP servers as well as mail
clients accessing the mailboxes directly.

%prep
%setup

%{__cat} <<EOF >dovecot.pam
#%PAM-1.0
auth       required     pam_stack.so service=system-auth
account    required     pam_stack.so service=system-auth
EOF

%{__cat} <<'EOF' >dovecot.sysv
#!/bin/bash
#
# Init file for Dovecot IMAP daemon
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 54 46
# description: Dovecot IMAP Daemon
#
# processname: dovecot
# config: %{_sysconfdir}/dovecot.conf
# pidfile: %{_localstatedir}/run/dovecot

source %{_initrddir}/functions

[ -x %{_sbindir}/dovecot ] || exit 1
[ -r %{_sysconfdir}/dovecot.conf ] || exit 1

RETVAL=0
prog="dovecot"
desc="IMAP daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog
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

reload() {
	echo -n $"Reloading $desc ($prog): "
	killproc $prog -HUP
	RETVAL=$?
	echo
	return $RETVAL
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	restart
	;;
  reload)
	reload
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
export CPPFLAGS="-I/usr/kerberos/include"
%configure \
	--with-ssl="openssl" \
	--with-ssldir="%{_datadir}/ssl" \
	--with-ldap \
	--with-pgsql \
	--with-cyrus-sasl2
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/pam.d/
%{__install} -m0755 dovecot.sysv %{buildroot}%{_initrddir}/dovecot
%{__install} -m0644 dovecot.pam %{buildroot}%{_sysconfdir}/pam.d/dovecot
%{__mv} -f %{buildroot}%{_sysconfdir}/dovecot-example.conf %{buildroot}%{_sysconfdir}/dovecot.conf

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/dovecot/

%pre
/usr/sbin/useradd -M -d "%{_libexecdir}/dovecot/" -c "Dovecot daemon" -r dovecot &>/dev/null || :
/usr/sbin/usermod -s /sbin/nologin dovecot &>/dev/null || :

%post
/sbin/chkconfig --add dovecot

%preun
if [ $1 -eq 0 ]; then
	/sbin/service dovecot stop &>/dev/null || :
	/sbin/chkconfig --del dovecot
fi

%postun
/sbin/service dovecot condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README TODO
%doc doc/*.cnf doc/*.conf doc/*.sh doc/*.txt
%config(noreplace) %{_sysconfdir}/dovecot.conf
%config(noreplace) %{_sysconfdir}/pam.d/dovecot
%config %{_initrddir}/dovecot
%{_sbindir}/*
%{_libexecdir}/dovecot/

%changelog
* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.99.10.4-0
- Updated to release 0.99.10.4.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 0.99.10-4
- Fix for kernel 2.6. (Koenraad Heijlen)

* Tue Aug 26 2003 Dag Wieers <dag@wieers.com> - 0.99.10-3
- Added missing dovecot-openssl.cnf. (Steven Op De Beeck)

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.99.10-2
- Replaced /etc/ssl with /usr/share/ssl. (Matthias Saou)
- Changed config files to (noreplace). (Matthias Saou)
- Added ldap and pgsql build options. (Matthias Saou)
- Replaced EOF with 'EOF' to unescape all shell variables. (Matthias Saou)
- Added reload capability to the init script. (Matthias Saou)
- Added sasl build option.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.99.10-1
- Added dovecot.pam. (Koenraad Heijlen)

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.99.10-0
- Updated to release 0.99.10.

* Tue May 03 2003 Dag Wieers <dag@wieers.com> - 0.99.9.1-0
- Updated to release 0.99.9.1.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.99.9-0
- Updated to release 0.99.9.

* Mon Apr 14 2003 Dag Wieers <dag@wieers.com> - 0.99.8.1-1
- Improved dovecot.sysv script.

* Thu Mar 13 2003 Dag Wieers <dag@wieers.com> - 0.99.8.1-0
- Updated to release 0.99.8.1.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.99.8-0
- Initial package. (using DAR)
