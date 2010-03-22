# $Id$
# Authority: dag

%define real_version 1.8beta5

%define _libdir /%{_lib}

Summary: library to allow transparent SOCKS proxying
Name: tsocks
Version: 1.8
Release: 7.beta5.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tsocks.sourceforge.net/

Source: http://dl.sf.net/tsocks/tsocks-%{real_version}.tar.gz
Patch0: tsocks_remove_static_lib.patch
Patch1: tsocks_fix_lib_path.patch
Patch2: tsocks_script_validation_error.patch
Patch3: tsocks_documentation_update.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tsocks is a library to allow transparent SOCKS proxying. It supports
both SOCKS 4 and SOCKS 5 (only TCP).

tsocks is designed for use in machines which are firewalled from
the internet. It avoids the need to recompile applications like lynx
or telnet so they can use SOCKS to reach the internet. It behaves
much like the SOCKSified TCP/IP stacks seen on other platforms.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__cat} <<'EOF' >tsocks
#!/bin/sh

### A wrapper script for the tsocks(8) transparant socksification library.
### Written by Dag Wieers <dag@wieers.com>.
###
### There are 3 modes of operandi:
###
###  * tsocks <program> <args ...>
###
###    This will socksify the current program only.
###    eg.
###         [user@host ~]# tsocks telnet www.foo.org
###
###  * tsocks [on|off]
###
###    This will socksify the current shell (and childs).
###    eg.
###         [user@host ~]# source /usr/bin/tsocks on
###         (user@host ~)# telnet www.foo.org
###         [user@host ~]# source /usr/bin/tsocks off
###
###  * tsocks
###
###    This will create a new socksified shell.
###    eg.
###         [user@host ~]# tsocks
###         (user@host ~)$ telnet www.foo.org
###         (user@host ~)$ exit
###         [user@host ~]#

PRG="$(basename $0)"
LIB="%{_libdir}/libtsocks.so"

function set_socks {
    if [ -z "$LD_PRELOAD" ]; then
        export LD_PRELOAD="$LIB"
    elif ! echo "$LD_PRELOAD" | grep -q "$LIB"; then
        export LD_PRELOAD="$LIB $LD_PRELOAD"
    fi
}

function unset_socks {
    export LD_PRELOAD="$(echo -n "$LD_PRELOAD" | sed "s|$LIB \?||")"
    if [ -z "$LD_PRELOAD" ]; then
        export -n LD_PRELOAD
    fi
}


case "$1" in
    on) set_socks;;
    off)    unset_socks;;
    show|sh)
        if echo "$LD_PRELOAD" | grep -q "$LIB"; then
            echo "$PRG: This shell is socksified."
        else
            echo "$PRG: This shell is NOT socksified."
        fi
        ;;
    -h|-?)  echo "$PRG: Please see tsocks(1) or read comment at top of $0"
        exit 1
        ;;
    '')
        set_socks
#       PS1="$(echo -n "$PS1" | tr \[\] \(\)) " ${SHELL:-/bin/sh};;
        PS1="(\u@\h \W)\$ " ${SHELL:-/bin/sh}
        ;;
    *)  set_socks
        exec "$@"
        ;;
esac
EOF

# This file is embedded here instead of being another source in order
# to the prefix directory
%{__cat} <<'EOF' >tsocksify.sysv
#!/bin/bash
#
# Startup script to transparantly socksify your system using tsocks.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 89 11
# description: Tsocksify is a means to socksify your system transparantly \
#   (using tsocks) on start-up after the network is up and running.
#
# processname: tsocksify
#
# config: %{_sysconfdir}/tsocks.conf
# config: /etc/ld.so.preload

source %{_initrddir}/functions

[ -r %{_sysconfdir}/tsocks.conf -a -x %{_libdir}/libtsocks.so ] || disable

RETVAL=0
prog="tsocks"

disable() {
    echo "Warning: your installation is faulty."
    stop
    exit 1
}

start() {
    echo -n $"Socksifying system ($prog): "
    grep "%{_libdir}/libtsocks.so" /etc/ld.so.preload &>/dev/null
    ret=$?
    if [ ! -f /etc/ld.so.preload -o $ret -ne 0 ]; then
        echo "%{_libdir}/libtsocks.so" >>/etc/ld.so.preload
        success $"tsocksify startup"
    elif [ $ret -eq 0 ]; then
        passed $"tsocksify startup"
    else
        failure $"tsocksify startup"
    fi
    RETVAL=$?
    echo
    return $RETVAL
}

stop() {
    echo -n "Unsocksifying system ($prog): "
    grep "%{_libdir}/libtsocks.so" /etc/ld.so.preload &>/dev/null
    if [ $? -eq 0 ]; then
        cat /etc/ld.so.preload | grep -v "%{_libdir}/libtsocks.so" >/etc/ld.so.preload.cache
        mv -f /etc/ld.so.preload.cache /etc/ld.so.preload
        success $"tsocksify shutdown"
    else
        failure $"tsocksify shutdown"
    fi
    RETVAL=$?
    if [ ! -s /etc/ld.so.preload ]; then
        rm -f /etc/ld.so.preload
    fi
    echo
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
  *)
    echo $"Usage: $0 {start|stop|restart}"
    exit $RETVAL
esac

exit $RETVAL
EOF

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 tsocks.conf.simple.example %{buildroot}%{_sysconfdir}/tsocks.conf
%{__install} -Dp -m0755 tsocksify.sysv %{buildroot}%{_initrddir}/tsocksify
%{__ln_s} -f tsocks %{buildroot}%{_bindir}/tsocksify

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add tsocksify

%preun
if [ "$1" = 0 ]; then
    /sbin/service tsocksify stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del tsocksify
fi

%postun
/sbin/ldconfig 2>/dev/null
/sbin/service tsocksify condrestart > /dev/null 2>&1 || :

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING FAQ TODO *.example
%doc %{_mandir}/man1/tsocks.1*
%doc %{_mandir}/man5/tsocks.conf.5*
%doc %{_mandir}/man8/tsocks.8*
%config(noreplace) %{_sysconfdir}/tsocks.conf
%config %{_initrddir}/tsocksify
%{_bindir}/tsocks
%{_bindir}/tsocksify
%{_libdir}/libtsocks.so*

%changelog
* Tue Jan 12 2010 Dag Wieers <dag@wieers.com> - 1.8-7.beta5
- Move library to /lib64 on 64bit
- Fix bash script validation to handle the no argument case
- Change patch name to reflect guidelines
- Fix documentation to reflect patch modifications

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.8-6.beta5
- Rewrote tsocks/tsocksify script.
- Don't replace config files.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.8beta5
- Updated tsocksify script and embedded it in SPEC file.

* Fri Jul 12 2002 Dag Wieers <dag@wieers.com> - 1.8beta4
- Added tsocksify SysV script.
- Added pre/post install scripts.
- Omitted INSTALL.

* Tue Jul 09 2002 Dag Wieers <dag@wieers.com> - 1.7
- Initial package.
