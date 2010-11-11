# $Id$
# Authority: dag
# Upstream: <ebtables-devel$lists,sourceforge,net>

### EL6 ships with ebtables-2.0.9-5.el6
# ExclusiveDist: el2 el3 el4 el5

%define _sbindir /sbin

Summary: Ethernet Bridge frame table administration tool
Name: ebtables
%define real_version 2.0.8-2
Version: 2.0.8.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://ebtables.sourceforge.net/

Source: http://dl.sf.net/ebtables/ebtables-v%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ethernet bridge tables is a firewalling tool to transparantly filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no incompatibility issues.

%prep
%setup -n %{name}-v%{real_version}

%{__perl} -pi.orig -e 's|__EXEC_PATH__|%{_sbindir}|g' ebtables-save

%{__cat} <<'EOF' >ebtables.sysv
#!/bin/bash
#
# init script for the Ethernet Bridge filter tables
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 15 85
# description: Ethernet Bridge filtering tables
#
# config: /etc/sysconfig/ebtables.filter
# config: /etc/sysconfig/ebtables.nat
# config: /etc/sysconfig/ebtables.route

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

[ -x %{_sbindir}/ebtables ] || exit 1

[ -r %{_sysconfdir}/sysconfig/ebtables.filter ] || exit 1
[ -r %{_sysconfdir}/sysconfig/ebtables.nat ] || exit 1
[ -r %{_sysconfdir}/sysconfig/ebtables.broute ] || exit 1

RETVAL=0
prog="ebtables"
desc="Ethernet bridge filtering"

start() {
    echo -n $"Starting $desc ($prog): "
    %{_sbindir}/ebtables -t filter --atomic-file %{_sysconfdir}/sysconfig/ebtables.filter --atomic-commit || RETVAL=1
    %{_sbindir}/ebtables -t nat --atomic-file %{_sysconfdir}/sysconfig/ebtables.nat --atomic-commit | RETVAL=1
    %{_sbindir}/ebtables -t broute --atomic-file %{_sysconfdir}/sysconfig/ebtables.broute --atomic-commit || RETVAL=1

    if [ $RETVAL -eq 0 ]; then
        success "$prog startup"
        rm -f %{_localstatedir}/lock/subsys/$prog
    else
        failure "$prog startup"
    fi

    echo
    return $RETVAL
}

stop() {
    echo -n $"Starting $desc ($prog): "
    %{_sbindir}/ebtables -t filter --init-table || RETVAL=1
    %{_sbindir}/ebtables -t nat --init-table || RETVAL=1
    %{_sbindir}/ebtables -t broute --init-table || RETVAL=1

    for mod in $(grep -E '^(ebt|ebtable)_' /proc/modules | cut -f1 -d' ') ebtables; do
        rmmod $mod || RETVAL=1
    done

    if [ $RETVAL -eq 0 ]; then
        success "$prog shutdown"
        rm -f %{_localstatedir}/lock/subsys/$prog
    else
        failure "$prog shutdown"
    fi

    echo
    return $RETVAL
}

restart() {
    stop
    start
}

save() {
    echo -n $"Saving $desc ($prog): "
    %{_sbindir}/ebtables -t filter --atomic-file %{_sysconfdir}/sysconfig/ebtables.filter --atomic-save || RETVAL=1
    %{_sbindir}/ebtables -t nat --atomic-file %{_sysconfdir}/sysconfig/ebtables.nat --atomic-save || RETVAL=1
    %{_sbindir}/ebtables -t broute --atomic-file %{_sysconfdir}/sysconfig/ebtables.broute --atomic-save || RETVAL=1

    if [ $RETVAL -eq 0 ]; then
        success "$prog saved"
    else
        failure "$prog saved"
    fi
    echo
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
  save)
    save
    ;;
  status)
    status $prog
    RETVAL=$?
    ;;
  *)
    echo $"Usage $0 {start|stop|restart|condrestart|save|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
%{__make} %{?_smp_mflags} CFLAGS="$(echo %{optflags} -fPIC | sed -e 's|-fstack-protector||g')"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ebtables %{buildroot}%{_sbindir}/ebtables
%{__install} -Dp -m0755 ebtables-restore %{buildroot}%{_sbindir}/ebtables-restore
%{__install} -Dp -m0755 ebtables-save %{buildroot}%{_sbindir}/ebtables-save
%{__install} -Dp -m0755 ebtables.sysv %{buildroot}%{_initrddir}/ebtables
%{__install} -Dp -m0644 ethertypes %{buildroot}%{_sysconfdir}/ethertypes
%{__install} -Dp -m0644 ebtables.8 %{buildroot}%{_mandir}/man8/ebtables.8

%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__install} -Dp -m0755 *.so extensions/*.so %{buildroot}%{_libdir}

touch %{buildroot}%{_sysconfdir}/ebtables.filter
touch %{buildroot}%{_sysconfdir}/ebtables.nat
touch %{buildroot}%{_sysconfdir}/ebtables.broute

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add ebtables
/sbin/ldconfig

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ebtables stop &>/dev/null || :
    /sbin/chkconfig --del ebtables
fi

%postun
/sbin/service ebtables condrestart &>/dev/null || :
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL THANKS
%doc %{_mandir}/man8/ebtables.8*
%config %{_sysconfdir}/ethertypes
%config %{_initrddir}/ebtables
%{_libdir}/libebt*.so
%{_sbindir}/ebtables
%{_sbindir}/ebtables-restore
%{_sbindir}/ebtables-save
%ghost %{_sysconfdir}/ebtables.filter
%ghost %{_sysconfdir}/ebtables.nat
%ghost %{_sysconfdir}/ebtables.broute

%changelog
* Wed Jan 30 2008 Jon Peatfield <J.S.Peatfield@damtp.cam.ac.uk> - 2.0.8.2-1
- Updated to release 2.0.8-2.
- Added ebtables-restore and ebtables-save.

* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 2.0.8-1
- Updated to release 2.0.8.

* Mon Dec 19 2005 Dag Wieers <dag@wieers.com> - 2.0.6-3
- Fixed typo in sysv script that prevented saving ruleset. (Neil McCalden)

* Thu Dec 02 2004 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Added patch for gcc 3.4. (Nigel Smith)

* Tue Apr 27 2004 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Cosmetic changes.

* Tue Apr 27 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Initial package. (using DAR)
