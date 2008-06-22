# $Id$
# Authority: dag
# Upstream: Gertjan van Zwieten <gertjanvanzwieten$fastmail,fm>

Summary: Replicating HTTP proxy server
Name: http-replicator
Version: 3.0
Release: 2
License: GPL
Group: Applications/Internet
URL: http://sourceforge.net/projects/http-replicator/

Source: http://dl.sf.net/http-replicator/http-replicator_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
Requires: python

%description
HTTP Replicator is a general purpose, replicating HTTP proxy server.

All downloads through the proxy are checked against a private cache, which is
an exact copy of the remote file structure. If the requested file is in the
cache, replicator sends it out at LAN speeds. If not in the cache, it will
simultaneously download the file and stream it to multiple clients.

No matter how many machines request the same file, only one copy comes down
the Internet pipe. This is very useful for maintaining a cache of Linux
packages.

%prep
%setup -n http-replicator_%{version}

%{__cat} <<EOF >http-replicator.logrotate
%{_localstatedir}/log/http-replicator.* {
    notifempty
    missingok
    copytruncate
    postrotate
        %{_initrddir}/http-replicator restart
    endscript
}
EOF

%{__cat} <<'EOF' >http-replicator.sysconfig
### Port on which the HTTP Replicator proxy should listen on.
PORT="8080"

### Whitespace-separated list of IP addresses of clients or client networks
### that are allowed to connect to the proxy.
ALLOW_IP="127.0.0.1"

### Whitespace-separated list of HTTP mirrors, i.e. hosts serving identical
### content. Useful for caching packages from different mirrors to the same
### directory.
MIRRORS=""

### Enable "static mode": files are known to never change so files that are
### present are served from cache directly without contacting the server
ENABLE_STATIC_MODE=""

### Enable "flat mode" for the cache: all files are saved in a single
### (cache) directory.
ENABLE_FLAT_CACHE=""

### Forward requests to an external proxy server, specified as "host:port"
### or "username:password@host:port" if the server requires authentication.
### Leave empty to disable external proxy server support.
FORWARD_TO_PROXY=""

### User to use to run http-replicator
USER="nobody"

### Cachedir location
CACHE_DIR="%{_localstatedir}/cache/http-replicator"

### Additional options for http-replicator daemon
OPTIONS=""
EOF

%{__cat} <<'EOF' >http-replicator.sysv
#!/bin/bash
#
# Init file for HTTP Replicator Proxy
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: 35 54 46
# description: HTTP Replicator Proxy
#
# processname: http-replicator
# config: %{_sysconfdir}/sysconfig/http-replicator
# pidfile: %{_localstatedir}/run/http-replicator

source %{_initrddir}/functions

[ -x %{_bindir}/http-replicator ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/http-replicator"
USER="nobody"
CACHE_DIR="%{_localstatedir}/cache/http-replicator"
OPTIONS=""

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

LOG_FILE="%{_localstatedir}/log/http-replicator.log"
PID_FILE="%{_localstatedir}/run/http-replicator"

RETVAL=0
prog="http-replicator"
desc="HTTP Replicator Proxy"

start() {
    echo -n $"Starting $desc ($prog): "
    ARGS="--dir $CACHE_DIR"
    [ "$LISTEN_PORT" ] && ARGS="$ARGS --port $LISTEN_PORT"
    if [ "$ALLOW_IP" ]; then
        for ip in $ALLOW_IP; do
            ARGS="$ARGS --ip $ip"
        done
    fi
    if [ "$MIRRORS" ]; then
        for mirror in $MIRRORS; do
            ARGS="$ARGS --alias $mirror"
        done
    fi
    [ "$ENABLE_STATIC_MODE" ] && ARGS="$ARGS --static"
    [ "$ENABLE_FLAT_CACHE" ] && ARGS="$ARGS --flat"
    [ "$FORWARD_TO_PROXY" ] && ARGS="$ARGS --external $FORWARD_TO_PROXY"
    daemon $prog --daemon --log $LOG_FILE --pid $PID_FILE --user $USER $ARGS
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

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 http-replicator %{buildroot}%{_bindir}/http-replicator
%{__install} -Dp -m0755 http-replicator_maintenance %{buildroot}%{_bindir}/http-replicator_maintenance
%{__install} -Dp -m0644 http-replicator.1 %{buildroot}%{_mandir}/man1/http-replicator.1
%{__install} -Dp -m0644 http-replicator_maintenance.1 %{buildroot}%{_mandir}/man1/http-replicator_maintenance.1
%{__install} -Dp -m0755 http-replicator.sysv %{buildroot}%{_initrddir}/http-replicator
%{__install} -Dp -m0755 http-replicator.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/http-replicator
%{__install} -Dp -m0644 http-replicator.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/http-replicator

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cache/http-replicator/

%post
/sbin/chkconfig --add http-replicator

%preun
if [ $1 -eq 0 ]; then
    /sbin/service http-replicator stop &>/dev/null || :
    /sbin/chkconfig --del http-replicator
fi

%postun
/sbin/service http-replicator condrestart &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README examples/
%doc %{_mandir}/man1/http-replicator.1*
%doc %{_mandir}/man1/http-replicator_maintenance.1*
%config(noreplace) %{_sysconfdir}/logrotate.d/http-replicator
%config(noreplace) %{_sysconfdir}/sysconfig/http-replicator
%config %{_initrddir}/http-replicator
%{_bindir}/http-replicator
%{_bindir}/http-replicator_maintenance

%defattr(0775, nobody, root, 0755)
%{_localstatedir}/cache/http-replicator/

%changelog
* Sun Jun 22 2008 Dries Verachtert <dries@ulyssis.org> - 3.0-2
- Fix the default values of the http-replicator.sysconfig, thanks to Izaak Branderhorst.
- URL and source location changed.

* Fri Oct 12 2007 Dag Wieers <dag@wieers.com> - 3.0-1
- Initial package. (based on Pascal Bleser's work)
