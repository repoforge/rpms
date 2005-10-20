# $Id$
# Authority: dag
# Upstream: Brad Fitzpatrick <brad$danga,com>

Summary: Distributed memory object caching system
Name: memcached
Version: 1.1.11
Release: 1
License: BSD
Group: System Environment/Daemons
URL: http://www.danga.com/memcached/

Source: http://www.danga.com/memcached/dist/memcached-%{version}.tar.gz
Patch: memcached-1.1.11-segfault.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel
Requires: /sbin/chkconfig

%description
memcached is a high-performance, distributed memory object caching system, 
generic in nature, but intended for use in speeding up dynamic web 
applications by alleviating database load.

%prep
%setup
%patch -p0

%{__cat} <<EOF >memcached.sysconfig
PORT="11211"
USER="nobody"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS=""
EOF

%{__cat} <<'EOF' >memcached.sysv
#!/bin/bash
#
# Init file for memcached
#
# Written by Dag Wieërs <dag@wieers.com>
#
# chkconfig: - 80 12
# description: Distributed memory caching daemon
#
# processname: memcached
# config: /etc/sysconfig/memcached
# config: /etc/memcached.conf
# pidfile: /var/run/memcached.pid

source %{_initrddir}/functions

### Default variables
PORT="11211"
USER="nobody"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS=""
SYSCONFIG="%{_sysconfdir}/sysconfig/memcached"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="memcached"
desc="Distributed memory caching"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -d -p $PORT -u $USER -c $MAXCONN -m $CACHESIZE $OPTIONS
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
%configure \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Problems installing manpage (Please fix upstream)
#%{__make} install \
#	DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 memcached %{buildroot}%{_bindir}/memcached
%{__install} -Dp -m0644 doc/memcached.1 %{buildroot}%{_mandir}/man1/memcached.1
%{__install} -Dp -m0755 memcached.sysv %{buildroot}%{_initrddir}/memcached
%{__install} -Dp -m0644 memcached.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/memcached

%post
/sbin/chkconfig --add memcached

%preun
if [ $1 -eq 0 ]; then
	/sbin/service memcached stop &> /dev/null || :
	/sbin/chkconfig --del memcached
fi

%postun
/sbin/service memcached condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/*.txt INSTALL NEWS README TODO
%doc %{_mandir}/man1/memcached.1*
%config(noreplace) %{_sysconfdir}/sysconfig/memcached
%config %{_initrddir}/memcached
%{_bindir}/memcached
#exclude %{_bindir}/nal_test
#exclude %{_bindir}/piper

%changelog
* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 1.1.11-1
- Cosmetic changes.

* Thu Feb 24 2005 Rob Starkey <falcon@rasterburn.com> - 1.1.11-1
- Initial package.
