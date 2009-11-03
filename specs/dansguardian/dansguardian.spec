# $Id$
# Authority: dag
# Upstream: Daniel Barron <author$dansguardian,org>

%define real_name DansGuardian

Summary: Content filtering web proxy
Name: dansguardian
Version: 2.8.0.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.dansguardian.org/

Source: http://dansguardian.org/downloads/2/Stable/dansguardian-%{version}.source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel, which

%description
DansGuardian is a web filtering engine that checks the content within
the page itself in addition to the more traditional URL filtering.

DansGuardian is a content filtering proxy. It filters using multiple methods,
including URL and domain filtering, content phrase filtering, PICS filtering,
MIME filtering, file extension filtering, POST filtering.

%prep
%setup

### FIXME: Add a default dansguardian.httpd for Apache. (Please fix upstream)
%{__cat} <<EOF >dansguardian.httpd
### You may need to include conf.d/dansguardian.conf to make it work.
ScriptAlias /dansguardian/ %{_localstatedir}/www/dansguardian/

<Directory %{_localstatedir}/www/dansguardian/>
        DirectoryIndex dansguardian.pl
        Options ExecCGI
        order deny,allow
        deny from all
        allow from 127.0.0.1
</Directory>
EOF

%{__cat} <<'EOF' >dansguardian.init
#!/bin/bash
#
# Init file for DansGuardian content filter.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 92 8
# description: DansGuardian content filter.
#
# processname: dansguardian
# config: %{_sysconfdir}/dansguardian/dansguardian.conf
# pidfile: %{_localstatedir}/run/dansguardian

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

### Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0

[ -x "%{_sbindir}/dansguardian" ] || exit 1
[ -r "%{_sysconfdir}/dansguardian/dansguardian.conf" ] || exit 1

RETVAL=0
prog="dansguardian"
desc="Web Content Filter"

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
	echo $"Usage: $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
### FIXME: Makefiles don't follow proper autotools directory standard. (Please fix upstream)
./configure \
	--bindir="%{_sbindir}/" \
	--cgidir="%{_localstatedir}/www/dansguardian/" \
	--installprefix="%{buildroot}" \
	--logdir="%{_localstatedir}/log/dansguardian/" \
	--logrotatedir="%{_sysconfdir}/logrotate.d/" \
	--mandir="%{_mandir}/" \
	--sysconfdir="%{_sysconfdir}/dansguardian/" \
	--sysvdir="%{_initrddir}/" \
	--runas_usr="nobody" \
	--runas_grp="nobody"

%{__perl} -pi.orig -e '
		s|^(CHKCONFIG) =.*$|$1 = :|;
                s|^\tchown|#\tchown|;
		s|/usr/lib|%{_libdir}|g;
        ' Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Directory not created prior installation. (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/logrotate.d/

%makeinstall
%{__install} -Dp -m0644 dansguardian.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/dansguardian.conf
%{__install} -Dp -m0755 dansguardian.init %{buildroot}%{_initrddir}/dansguardian

%post
/sbin/chkconfig --add dansguardian

%preun
if [ $1 -eq 0 ]; then
        /sbin/service dansguardian stop &>/dev/null || :
        /sbin/chkconfig --del dansguardian
fi

%postun
/sbin/service dansguardian condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE README
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/dansguardian/
%config(noreplace) %{_sysconfdir}/dansguardian/dansguardian.conf
%config(noreplace) %{_sysconfdir}/dansguardian/dansguardianf1.conf
#%config(noreplace) %{_sysconfdir}/dansguardian/template.html
%config %{_sysconfdir}/dansguardian/*list
%config %{_sysconfdir}/dansguardian/phraselists/
#%config %{_sysconfdir}/dansguardian/messages
%config %{_sysconfdir}/dansguardian/languages/
%config %{_sysconfdir}/dansguardian/logrotation/
%config %{_sysconfdir}/dansguardian/pics/
%config %{_sysconfdir}/dansguardian/transparent1x1.gif
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config %{_initrddir}/*
%config %{_sysconfdir}/logrotate.d/*
%{_sbindir}/*
%{_localstatedir}/www/dansguardian/

%defattr(0700, nobody, nobody, 0755)
%{_localstatedir}/log/dansguardian/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.8.0.6-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 2.8.0.6-1
- Updated to release 2.8.0.6.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 2.8.0.4-1
- Updated to release 2.8.0.4.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 2.8.0.2-1
- Updated to release 2.8.0.2.

* Wed Jul 21 2004 Dag Wieers <dag@wieers.com> - 2.8.0-1
- Updated to release 2.8.0-0.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 2.6.1.13-1
- Updated to release 2.6.1-13.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 2.6.1.12-1
- Initial package. (using DAR)
