# $Id$
# Authority: dag
# Upstream: Timo Sirainen <tss$iki,fi>
# Upstream: <dovecot$dovecot,org>

##ExcludeDist: fc3 el4

%define logmsg logger -t %{name}/rpm

Summary: Secure IMAP server
Name: dovecot
Version: 1.0.12
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://dovecot.org/

Source: http://dovecot.org/releases/1.0/dovecot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, cyrus-sasl-devel, pam-devel
BuildRequires: openldap-devel, postgresql-devel, mysql-devel
BuildRequires: gcc-c++, zlib-devel
Requires: /usr/sbin/useradd, /usr/sbin/usermod, /sbin/chkconfig

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

%{__perl} -pi.orig -e '
        s|/etc/ssl|%{_datadir}/ssl|;
        s|^#(logindir) = |$1 = |;
        s|^(mbox_locks) = .*|$1 = fcntl|;
        s|^(auth_passdb) = |$1 = pam\n#$1 = |;
    ' dovecot-example.conf

%{__cat} <<EOF >dovecot.pam
#%PAM-1.0
auth       required     pam_nologin.so
auth       required     pam_stack.so service=system-auth
account    required     pam_stack.so service=system-auth
session    required     pam_stack.so service=system-auth
EOF

%{__cat} <<'EOF' >dovecot.sysv
#!/bin/bash
#
# Init file for Dovecot IMAP daemon
#
# Written by Dag Wieers <dag@wieers.com>
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
export CPPFLAGS="-I%{_prefix}/kerberos/include -I %{_includedir}/mysql"
export LDFLAGS="-L%{_libdir}/mysql"
%configure \
    --with-ldap \
    --with-mysql \
    --with-pgsql \
    --with-rawlog \
    --with-ssl="openssl" \
    --with-ssldir="%{_datadir}/ssl"
### Causes crashes when used with ldap
#   --with-cyrus-sasl2
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 dovecot.sysv %{buildroot}%{_initrddir}/dovecot
%{__install} -Dp -m0644 dovecot.pam %{buildroot}%{_sysconfdir}/pam.d/dovecot
%{__mv} -f %{buildroot}%{_sysconfdir}/dovecot-example.conf %{buildroot}%{_sysconfdir}/dovecot.conf

# generate ghost .pem file
%{__install} -d -m0755 %{buildroot}%{_datadir}/ssl/{certs,private}/
touch %{buildroot}%{_datadir}/ssl/{certs,private}/dovecot.pem

%{__install} -d -m0700 %{buildroot}%{_localstatedir}/run/dovecot/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/dovecot-login/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_sysconfdir}/dovecot-{ldap,sql}-example.conf

%pre
if ! /usr/bin/id dovecot &>/dev/null; then
    /usr/sbin/useradd -c dovecot -u 97 -r -d "%{_libexecdir}/dovecot/" dovecot &>/dev/null || \
        %logmsg "Unexpected error adding user \"dovecot\". Aborting installation."
fi
/usr/sbin/usermod -s /sbin/nologin dovecot &>/dev/null || :

%post
/sbin/chkconfig --add dovecot

# create a ssl cert
if [ ! -f %{_datadir}/ssl/certs/dovecot.pem ]; then
    umask 077
    %{__cat} << EOF | openssl req -new -x509 -days 365 -nodes -out %{_datadir}/ssl/certs/dovecot.pem -keyout %{_datadir}/ssl/private/dovecot.pem &>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
localhost.localdomain
root@localhost.localdomain
EOF
    %{__chown} root:root %{_datadir}/ssl/private/dovecot.pem %{_datadir}/ssl/certs/dovecot.pem
    %{__chmod} 600 %{_datadir}/ssl/private/dovecot.pem %{_datadir}/ssl/certs/dovecot.pem
fi

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
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README TODO
%doc doc/*.cnf doc/*.conf doc/*.sh doc/*.txt
%config(noreplace) %{_sysconfdir}/dovecot.conf
%config(noreplace) %{_sysconfdir}/pam.d/dovecot
%config %{_initrddir}/dovecot
%{_libdir}/dovecot/
%{_libexecdir}/dovecot/
%exclude %{_docdir}/dovecot/
%{_localstatedir}/run/dovecot-login/
%{_sbindir}/dovecot
%{_sbindir}/dovecotpw

%defattr(0600, root, root, 0755)
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_datadir}/ssl/certs/dovecot.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_datadir}/ssl/private/dovecot.pem

%defattr(0700, root, root, 0755)
%{_localstatedir}/run/dovecot/

%defattr(0750, root, dovecot, 0755)
%{_localstatedir}/run/dovecot-login/

%exclude %{_libdir}/dovecot/*.a
%exclude %{_libdir}/dovecot/*.la
%exclude %{_libdir}/dovecot/*/*.a
%exclude %{_libdir}/dovecot/*/*.la

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.0.12-1
- Updated to release 1.0.12.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sat Jun 16 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sun Jan 09 2005 Dag Wieers <dag@wieers.com> - 0.99.13-1
- Updated to release 0.99.13.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 0.99.12-2
- Build without cyrus-sasl support. (Roger Bystrom)

* Sun Dec 05 2004 Dag Wieers <dag@wieers.com> - 0.99.12-1
- Updated to release 0.99.12.

* Wed Sep 29 2004 Dag Wieers <dag@wieers.com> - 0.99.11-1
- Updated to release 0.99.11.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 0.99.10.9-2
- Bring in line with newly introduced dovecot in FC2. (Morten Kjeldgaard)

* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.99.10.9-1
- Updated to release 0.99.10.9.

* Fri Jul 16 2004 Dag Wieers <dag@wieers.com> - 0.99.10.7-1
- Updated to release 0.99.10.7.

* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 0.99.10.6-1
- Updated to release 0.99.10.6.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.99.10.5-1
- Updated to release 0.99.10.5.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.99.10.4-0
- Updated to release 0.99.10.4.
- Added rh-postgresql for RHEL3.

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
