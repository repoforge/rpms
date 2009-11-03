# $Id$
# Authority: dag

Summary: Remotely administer the file systems of multiple unix machines
Name: radmind
Version: 1.11.1
Release: 1%{?dist}
License: BSD-like
Group: System Environment/Base
URL: http://rsug.itd.umich.edu/software/radmind/

Source: http://dl.sf.net/radmind/radmind-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel, openssl-devel, libsnet-devel >= 0.0-20060320.1
Requires: diffutils, openssl

%description
A suite of Unix command-line tools and a server designed to
remotely administer the file systems of multiple Unix machines.

At its core, radmind operates as a tripwire. It is able to detect
changes to any managed filesystem object, e.g. files, directories,
links, etc. However, radmind goes further than just integrity
checking: once a change is detected, radmind can optionally
reverse the change.

Each managed machine may have its own loadset composed of multiple,
layered overloads. This allows, for example, the operating system
to be described separately from applications.

Loadsets are stored on a remote server. By updating a loadset on
the server, changes can be pushed to managed machines.

%prep
%setup

%{__cat} <<'EOF' >radmind.sysv
#!/bin/bash
#
# Startup script for the radmind daemon
# 
# chkconfig: 2345 80 30
# description: radmind is a suite of Unix command-line \
# tools and a server designed to remotely administer the \
# file systems of multiple Unix machines.
# processname: radmind
# pidfile: /var/run/radmind.pid
# config: /etc/sysconfig/radmind

# Source function library.
source /etc/rc.d/init.d/functions

# Source networking configuration.
source /etc/sysconfig/network

[ ${NETWORKING} = "no" ] && exit 0

[ -x /usr/sbin/radmind ] || exit 0

# Source  radmind config
[ -f /etc/sysconfig/radmind ] && . /etc/sysconfig/radmind

# See how we were called.
case "$1" in
  start)
    echo -n "Starting radmind: "
        daemon radmind \
        ${_RADMIND_BIND_ADDRESS:-"-a 0"} \
        ${_RADMIND_BACKLOG:-"-b 5"} \
        ${_RADMIND_PATH:-"-D /var/lib/radmind"} \
        ${_RADMIND_SYSLOG_FACILITY:-"-L local7"} \
        ${_RADMIND_MAXCONNECTIONS:-"-m 0"} \
        ${_RADMIND_PORT:-"-p 6662"} \
        ${_RADMIND_UMASK:-"-u 022"} \
        ${_RADMIND_PAM:-""} \
        ${_RADMIND_AUTHLEVEL:-"-w 0"} \
        ${_RADMIND_TLS_CA:-"-x /etc/ssl/radmind/ca.pem"} \
        ${_RADMIND_TLS_PUBLIC_CERT:-"-y /etc/ssl/radmind/cert.pem"} \
        ${_RADMIND_TLS_PRIVATE_CERT:-"-z /etc/ssl/radmind/cert.pem"}
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/radmind
    ;;
  stop)
    echo -n "Stopping radmind: "
    killproc radmind
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/radmind
    ;;
  debug)
    echo -n "Starting radmind in debug mode: "
        daemon radmind -d \
        ${_RADMIND_BIND_ADDRESS:-"-a 0"} \
        ${_RADMIND_BACKLOG:-"-b 5"} \
        ${_RADMIND_PATH:-"-D /var/lib/radmind"} \
        ${_RADMIND_SYSLOG_FACILITY:-"-L local7"} \
        ${_RADMIND_MAXCONNECTIONS:-"-m 0"} \
        ${_RADMIND_PORT:-"-p 6662"} \
        ${_RADMIND_UMASK:-"-u 022"} \
        ${_RADMIND_PAM:-""} \
        ${_RADMIND_AUTHLEVEL:-"-w 0"} \
        ${_RADMIND_TLS_CA:-"-x /etc/ssl/radmind/ca.pem"} \
        ${_RADMIND_TLS_PUBLIC_CERT:-"-y /etc/ssl/radmind/cert.pem"} \
        ${_RADMIND_TLS_PRIVATE_CERT:-"-z /etc/ssl/radmind/cert.pem"}
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/radmind
    ;;
  status)
    status radmind
    RETVAL=$?
    ;;
  restart|reload)
    $0 stop
    $0 start
    RETVAL=$?
    ;;
  *)
    echo "Usage: radmind {start|stop|status|restart|reload|debug}"
    exit 1
esac

exit $RETVAL
EOF

%{__cat} <<'EOF' >radmind.sysconfig
# specifies the address on which the server should listen, e.g.
# 127.0.0.1. By default the server listens on all available
# interfaces (wildcard address).
_RADMIND_BIND_ADDRESS="-a 0"

# Defines the maximum queue of pending connections to
# listen, by default five.
_RADMIND_BACKLOG="-b 5"

# specifies the radmind working directory, by default
# _RADMIND_PATH
_RADMIND_PATH="-D /var/lib/radmind"

# specifies which syslog-facilty to log messages to.
_RADMIND_SYSLOG_FACILITY="-L local7"

# specifies the maximum number of simultaneous connections, by
# default _RADMIND_MAXCONNECTIONS. Value must be greater than or
# equal to 0 with 0 indicating no limit.
_RADMIND_MAXCONNECTIONS="-m 0"

# specifies the port of the radmind server, by default 6662.
_RADMIND_PORT="-p 6662"

# specifies the umask the server uses to write files to the disk,
# defaulting to the user's umask.
_RADMIND_UMASK="-u 022"

# Turn on PAM user authentication. radmind uses the PAM service
# name radmind. Unset to disable.
_RADMIND_PAM="-U"

# TLS authorization level, by default _RADMIND_AUTHLEVEL. 0 = no
# TLS, 1 = server verification, 2 = server and client
# verification.
_RADMIND_AUTHLEVEL="-w 0"

# Certificate authority's public certificate, by default
# _RADMIND_TLS_CA.
_RADMIND_TLS_CA="-x /etc/ssl/radmind/ca.pem"

# Server's public certificate, by default _RADMIND_TLS_CERT.
_RADMIND_TLS_PUBLIC_CERT="-y /etc/ssl/radmind/cert.pem"

# Server's private key, by default _RADMIND_TLS_CERT.
_RADMIND_TLS_PRIVATE_CERT="-z /etc/ssl/radmind/cert.pem"
EOF

%{__cat} <<'EOF' >radmind.config
#
# Client	command file
#
127.0.0.1	localhost.K
EOF

%{__cat} <<'EOF' >radmind.pam
#%PAM-1.0
auth       required     pam_nologin.so
auth       required     pam_stack.so service=system-auth
account    required     pam_stack.so service=system-auth
session    required     pam_stack.so service=system-auth
EOF

%build
export CPPFLAGS="-I/usr/kerberos/include"
%configure \
    --with-server="localhost" \
    --with-radminddir="%{_localstatedir}/radmind" \
    --with-ssl="%{_prefix}"

%{__perl} -pi.orig \
    -e "s|^GNU_DIFF.*|GNU_DIFF=%{_bindir}/diff|g;" \
    -e "s|^CERTDIR.*|CERTDIR=%{_sysconfdir}/pki/radmind|g;" \
    -e "s|^RADMINDSYSLOG.*|RADMINDSYSLOG=LOG_LOCAL7|g;" \
    Makefile

%{__make} %{_smp_mflags} \
    OPTOPTS="%{optflags}" \
    VERSION="%{version}-%{release}"

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 radmind.sysv %{buildroot}%{_initrddir}/radmind
%{__install} -Dp -m0644 radmind.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/radmind
%{__install} -Dp -m0644 radmind.config %{buildroot}%{_localstatedir}/radmind/config
%{__install} -Dp -m0644 radmind.pam %{buildroot}%{_sysconfdir}/pam.d/radmind
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/radmind/{command,file,special,transcript}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/radmind/tmp/{file,transcript}

%post
/sbin/chkconfig --add radmind

%postun
/sbin/service radmind condrestart &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service radmind stop &>/dev/null || :
        /sbin/chkconfig --del radmind
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT README SPEC
%doc %{_mandir}/man1/fsdiff.1*
%doc %{_mandir}/man1/ktcheck.1*
%doc %{_mandir}/man1/lapply.1*
%doc %{_mandir}/man1/lcksum.1*
%doc %{_mandir}/man1/lcreate.1*
%doc %{_mandir}/man1/lfdiff.1*
%doc %{_mandir}/man1/lmerge.1*
%doc %{_mandir}/man1/lsort.1*
%doc %{_mandir}/man1/rash.1*
%doc %{_mandir}/man1/repo.1*
%doc %{_mandir}/man1/twhich.1*
%doc %{_mandir}/man5/applefile.5*
%doc %{_mandir}/man8/radmind.8*
%config(noreplace) %{_sysconfdir}/sysconfig/radmind
%config(noreplace) %{_sysconfdir}/pam.d/radmind
%config(noreplace) %{_localstatedir}/radmind/config
%config %{_initrddir}/radmind
%dir %{_sysconfdir}/pki/radmind/
%{_bindir}/fsdiff
%{_bindir}/ktcheck
%{_bindir}/lapply
%{_bindir}/lcksum
%{_bindir}/lcreate
%{_bindir}/lfdiff
%{_bindir}/lmerge
%{_bindir}/lsort
%{_bindir}/ra.sh
%{_bindir}/repo
%{_bindir}/twhich
%{_sbindir}/radmind
%dir %{_localstatedir}/radmind/
%dir %{_localstatedir}/radmind/command/
%dir %{_localstatedir}/radmind/file/
%dir %{_localstatedir}/radmind/special/
%dir %{_localstatedir}/radmind/tmp/
%dir %{_localstatedir}/radmind/tmp/file/
%dir %{_localstatedir}/radmind/tmp/transcript/
%dir %{_localstatedir}/radmind/transcript/

%changelog
* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 1.11.1-1
- Updated to release 1.11.1.

* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.11.0-1
- Updated to release 1.11.0.

* Wed May 23 2007 Dag Wieers <dag@wieers.com> - 1.8.1-1
- Updated to release 1.8.1.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Initial package based on Mandrake package.
