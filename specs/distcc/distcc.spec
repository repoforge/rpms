# $Id$
# Authority: dag
# Upstream: Martin Pool <mbp@sourcefrog.net>
# Upstream: <distcc@lists.samba.org>

%define gui 1
%{?rh73:%undefine gui}
%{?rhel21:%undefine gui}
%{?rh62:%undefine gui}

%define gccversion %(rpm -q gcc --qf '%{RPMTAG_VERSION}' | tail -1)

Summary: Distributed C/C++ compilation client program
Name: distcc
Version: 2.14
Release: 1
License: GPL
Group: Development/Tools
URL: http://distcc.samba.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://samba.org/ftp/distcc/distcc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?gui:BuildRequires: gtk2-devel >= 2.0}
Requires: gcc, gcc-c++
%{?rhfc1:Requires: compat-gcc, compat-gcc-c++, gcc32}
%{?rh90:Requires: compat-gcc, compat-gcc-c++}
%{?rh80:Requires: compat-gcc, compat-gcc-c++}

%description
distcc is a distributed compilation front-end.  It sends command lines
and preprocessed files to other machines, that ship the resulting
object file and compiler output back. It gives significant speed ups
with make -jN.

%package server
Summary: distributed C/C++ compilation daemon
Group: Development/Tools

%description server
This package provides the server-side software for distcc. It must be
installed on all the hosts which are to participate in your distcc cluster.

%package gui
Summary: distributed C/C++ compilation GUI frontend
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Obsoletes: distcc-gnome

%description gui
This package provides the GNOME-based monitor for distcc. It is not required
in order to use distcc.

%prep
%setup

%{__cat} <<EOF >distccmon-gnome.desktop
[Desktop Entry]
Name=Distcc Monitor
Comment=View progress of your distributed compile tasks
Exec=distccmon-gnome
Icon=distccmon-gnome.png
Terminal=false
Type=Application
Categories=GNOME;Application;Development;
StartupNotify=true
EOF

%{__cat} <<EOF >distccd.sysconfig
### See distcc(1) manual page for more information on these options.
###

#OPTIONS="--nice 5 --jobs 5 --allow 10.0.0.0/24 --port 1234"
#USER="distcc"

### Set this if don't want distccd to use gcc or g++ by accident.
#DISTCCPATH="/usr/lib/distcc/bin"
EOF

%{__cat} <<'EOF' >distccd.sysv
#!/bin/sh
#
# Init file for Distccd - A distributed compilation front-end.
# WARNING: Don't enable on untrusted networks
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 80 20
# description: Distccd - distributed compilation front-end (daemon)	\
#		WARNING: Don't enable on untrusted networks
#
# processname: distccd
#
# config: %{_sysconfdir}/sysconfig/distccd

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

### Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0

[ -x "%{_bindir}/distccd" ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/distccd"
OPTIONS=""
USER="distcc"
DISTCCPATH="$PATH"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="distccd"
desc="Distributed Compiler daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	PATH="$DISTCCPATH" daemon --user "$USER" $prog --daemon --log-file="%{_localstatedir}/log/distccd.log" $OPTIONS
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
	echo $"Usage $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%{__cat} <<'EOF' >distccd.xinetd
# default: off
# description: Distccd - distributed compilation front-end (xinetd)	\
#		Please disable the daemon if you enable this.		\
#		WARNING: Don't enable on untrusted networks
service distccd
{
	disable         = yes
	socket_type     = stream        
	protocol        = tcp
	port            = 3632
	type		= UNLISTED
	wait            = no
	user            = distcc
	server          = %{_bindir}/distccd
	server_args     = --inetd --log-file="%{_localstatedir}/log/distccd.log"
	only_from	= 127.0.0.1
}
EOF

%{__cat} <<EOF >distccd.logrotate
%{_localstatedir}/log/distccd.log {
        missingok
        copytruncate
        notifempty
}
EOF

%build
%configure \
	--with-docdir="./doc-rpm" \
%{?gui:	--with-gnome}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	pkgdocdir="./rpm/"
%{__install} -D -m0644 distccd.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/distccd
%{__install} -D -m0755 distccd.sysv %{buildroot}%{_initrddir}/distccd
%{__install} -D -m0644 distccd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/distccd
%{__install} -D -m0644 distccd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/distccd

%{__install} -d -m0755 %{buildroot}%{_libdir}/distcc/bin/
for compiler in cc c++ gcc g++; do
	%{__ln_s} -f %{_bindir}/distcc %{buildroot}%{_libdir}/distcc/bin/$compiler
	%{__ln_s} -f %{_bindir}/distcc %{buildroot}%{_libdir}/distcc/bin/i386-redhat-linux-$compiler-%{gccversion}
done

%{?rhfc1:%define has_gcc296 1}
%{?rh90:%define has_gcc296 1}
%{?rh80:%define has_gcc296 1}
%{?rh73:%define has_gcc296 1}
%{?rhel21:%define has_gcc296 1}

%if %{?has_gcc296:1}%{!?has_gcc296:0}
for compiler in gcc296 g++296; do
	%{__ln_s} -f %{_bindir}/distcc %{buildroot}%{_libdir}/distcc/bin/$compiler
done
%endif

%{?rhfc1:%define has_gcc323 1}
%if %{?has_gcc323:1}%{!?has_gcc323:0}
for compiler in gcc32 gcc323; do
	%{__ln_s} -f %{_bindir}/distcc %{buildroot}%{_libdir}/distcc/bin/$compiler
done
%endif

%if %{?gui:1}%{!?gui:0}
	%{__install} -D -m0644 gnome/distccmon-gnome-icon.png %{buildroot}%{_datadir}/pixmaps/distccmon-gnome.png
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		distccmon-gnome.desktop
%endif

%pre server
/usr/sbin/useradd -M -s /sbin/nologin -r distcc &>/dev/null || :
/usr/sbin/usermod -s /sbin/nologin distcc &>/dev/null || :

%post server
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add distccd
fi

touch /var/log/distccd.log
%{__chown} distcc.distcc /var/log/distccd.log

if ! grep -q "3632/tcp" /etc/services; then
	echo -e "distcc\t\t3632/tcp\t\t\t# Distcc Distributed Compiler" >> /etc/services
fi

if ! grep -q "^distcc:" /etc/hosts.allow; then
	echo -e "distcc:\t127.0.0.1" >> /etc/hosts.allow
fi

/sbin/service distccd condrestart &>/dev/null || :

%preun server
if [ $1 -eq 0 ]; then
	/sbin/service distccd stop &>/dev/null || :
	/sbin/chkconfig --del distccd
fi

%postun server
/sbin/service distccd condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-rpm/*
%doc %{_mandir}/man1/distcc.*
%doc %{_mandir}/man1/distccmon-text.*
%{_bindir}/distcc
%{_bindir}/distccmon-text
%{_libdir}/distcc/

%files server
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/distccd.*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/xinetd.d/*
%config %{_initrddir}/*
%{_bindir}/distccd

%if %{?gui:1}%{!?gui:0}
%files gui
%defattr(-, root, root, 0755)
%{_bindir}/distccmon-gnome
%{_datadir}/distcc/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%endif

%changelog
* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 2.14-1
- Updated to release 2.14.

* Tue Apr 20 2004 Dag Wieers <dag@wieers.com> - 2.13-3
- Fixed a bug in the sysv script introduced in 2.13-1. (Martijn Lievaart)

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 2.13-2
- Added patch to build gui for RH80. (Martin Pool)

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Sun Jan 25 2004 Dag Wieers <dag@wieers.com> - 2.12.1-1
- Made distcc aware of gcc296 and gcc32 packages.
- Now require gcc and compat-gcc packages too.

* Fri Jan 09 2004 Dag Wieers <dag@wieers.com> - 2.12.1-0
- Updated to release 2.12.1.

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 2.12-0
- Updated to release 2.12.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 2.11.2-0
- Updated to release 2.11.2.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 2.11.1-0
- Updated to release 2.11.1.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 2.11-0
- Updated to release 2.11.

* Mon Aug 11 2003 Dag Wieers <dag@wieers.com> - 2.10-0
- Updated to release 2.10.

* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 2.9-1
- Improved the default config files. (Martin Pool)
- Updated to release 2.9.

* Wed Jul 09 2003 Dag Wieers <dag@wieers.com> - 2.8-0
- Updated to release 2.8.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 2.7-0
- Updated to release 2.7.

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> - 2.6-0
- Updated to release 2.6.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 2.5.1-0
- Updated to release 2.5.1.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 2.5-0
- Updated to release 2.5.

* Wed May 21 2003 Dag Wieers <dag@wieers.com> - 2.4-0
- Updated to release 2.4.

* Fri May 16 2003 Dag Wieers <dag@wieers.com> - 2.3-0
- Updated to release 2.3.

* Wed May 14 2003 Dag Wieers <dag@wieers.com> - 2.2-2
- Updated to release 2.2.
- Added seperate logfile and logrotate script.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 2.1-0
- Updated to release 2.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Updated to release 1.2.3.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2.
- Added sysv and xinet scripts.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Updated to release 1.2.

* Fri Feb 14 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
