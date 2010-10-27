# $Id$
# Authority: arrfab

Summary: XenWebManager is a web-based open source clone of Xencenter
Name: xenwebmanager
Version: 0.9.9
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.xensemaking.com/xenwebmanager/

Source: http://downloads.sourceforge.net/project/xenwebmanager/xenwebmanager_beta.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: python >= 2.4
Requires: python-cherrypy >= 3.1
Requires: python-mako >= 0.3.4
Requires: python-simplejson >= 2.0.5
Requires: graphviz

%description
XenWebManager is a web-based open source clone of Xencenter. With XenWebManager you only need a browser for manage your server and virtual machines running on XenServers

%prep
%setup -q -n xenwebmanager

# Defining a default initscript
%{__cat} <<'EOF' >tools/xenwebmanager.init
#!/bin/sh
#
# xenwebmanager:        Start/stop xenwebmanager service
#
# chkconfig:    2345 25 90
# description: XenWebManager is a web-based open source clone of Xencenter.
#


# Source function library.
. /etc/rc.d/init.d/functions

start()
{
        echo -n $"Starting XenWebManager service:"
        daemon --user=xenwm  /usr/bin/xenwebmanager -daemon
        PID=$(/bin/ps -ef|/bin/grep frontend.py|/bin/grep -v grep|/bin/awk '{print $2}')
        echo $PID > /var/run/xenwebmanager.pid
        echo ""
}

stop()
{
        echo -n "Stopping XenWebManager service:"
        killproc -p /var/run/xenwebmanager.pid xenwebmanager 
        echo ""
}

xwmstatus()
{
        status -p /var/run/xenwebmanager.pid xenwebmanager
        echo ""
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart|reload)
        stop
        start
        ;;
  condrestart)
        [ -e /var/lock/subsys/xenwebmanager ] && (stop; start)
        ;;
  status)
        xwmstatus 
        ;;
  *)
        echo $"Usage: $0 {start|stop|status|restart|reload|condrestart}"
        exit 1
        ;;
esac

exit 0
EOF

### Adds a shell wrapper script for xenwebmanager.
%{__cat} <<EOF >xenwebmanager.wrapper
#!/bin/bash
cd %{_datadir}/xenwebmanager
python frontend.py -daemon >/dev/null 2>&1
EOF


%build


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/xenwebmanager
%{__cp} -av * %{buildroot}/usr/share/xenwebmanager
%{__install} -D -m0755 tools/xenwebmanager.init %{buildroot}%{_initrddir}/xenwebmanager
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/xenwebmanager
%{__install} -m0644 cherry.conf %{buildroot}%{_sysconfdir}/xenwebmanager/
%{__install} -m0644 frontend.conf %{buildroot}%{_sysconfdir}/xenwebmanager/
%{__install} -D -d -m0755 %{buildroot}%{_localstatedir}/log/xenwebmanager
%{__install} -D -d -m0755 %{buildroot}%{_localstatedir}/lib/xenwebmanager
%{__install} -D -m0755 xenwebmanager.wrapper %{buildroot}%{_bindir}/xenwebmanager

%pre
if ! /usr/bin/id xenwm &>/dev/null; then
    /usr/sbin/useradd -r -d /usr/share/xenwebmanager -s /sbin/nologin -c "xenwebmanager" xenwm || \
        %logmsg "Unexpected error adding user \"xenwm\". Aborting installation."
fi

%post
/sbin/chkconfig --add xenwebmanager

%preun
if [ $1 = 0 ]; then
        /sbin/service xenwebmanager stop > /dev/null 2>&1
        /sbin/chkconfig --del xenwebmanager
fi

%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel xenwm || %logmsg "User \"xenwm\" could not be deleted."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc LICENSE README
%dir %{_datadir}/xenwebmanager/
%{_datadir}/xenwebmanager/*
%dir %{_sysconfdir}/xenwebmanager/
%{_initrddir}/xenwebmanager
%{_bindir}/xenwebmanager

%defattr(-, xenwm, xenwm, 0755 )
%{_localstatedir}/lib/xenwebmanager/
%{_localstatedir}/log/xenwebmanager/
%config(noreplace) %{_sysconfdir}/xenwebmanager/frontend.conf
%config(noreplace) %{_sysconfdir}/xenwebmanager/cherry.conf


%changelog
* Sun Oct 24 2010 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.9.1-1
- Initial package


