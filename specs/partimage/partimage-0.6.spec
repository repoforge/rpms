# Authority: dag

# Upstream: François Dupoux <fdupoux@partimage.org>

Summary: A partition imaging utility, much like Ghost.
Name: partimage
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/System
URL: http://www.partimage.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sourceforge/partimage/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: parted-devel, newt-devel, libmcrypt-devel

%description
Partition Image is a Linux/UNIX partition imaging utility: it saves all used
blocks in a partition to an image file. This image file can be compressed
using gzip or bzip2 compression to save space, and even split into multiple
files to be copied to movable media such as Zip disks or CD-R.

Partition Images supports the following filesystems:

	ext2fs, ext3fs, fat16, fat32, hfs, hpfs, jfs, ntfs, reiserfs, ufs, xfs

Partition Image allows you to back up a full Linux/Windows system with a single
operation. When problems such as viruses, crashes, or other errors occur, you
just have to restore, and after several minutes your system can be restored
(boot record and all your files) and fully working.

%package static
Summary: A partition imaging utility, much like Ghost.
Group: Applications/System

%description static
Partition Image is a Linux/UNIX partition imaging utility: it saves all used
blocks in a partition to an image file. This image file can be compressed
using gzip or bzip2 compression to save space, and even split into multiple
files to be copied to movable media such as Zip disks or CD-R.

This package contains a static compiled binary.

%package server
Summary: The server part of a partition imaging utility, much like Ghost.
Group: System Environment/Daemons

%description server
Partition Image is a Linux/UNIX partition imaging utility: it saves all used
blocks in a partition to an image file. This image file can be compressed
using gzip or bzip2 compression to save space, and even split into multiple
files to be copied to movable media such as Zip disks or CD-R.

This package contains the server daemon for remote imaging.

%prep
%setup

### FIXME: Disable chowning of files
%{__perl} -pi.orig -e 's|^\tchown partimag\.root.*$|\\|' Makefile.in

%{__cat} <<EOF >partimaged.sysconfig
### See partimaged --help for more information on these options.
###

#OPTIONS="--port=1234 --chroot %{_localstatedir}/partimaged --nologin"
EOF

%{__cat} <<'EOF' >partimaged.sysv
#!/bin/bash
#
# Init file for partimage daemon
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 80 20
# description: partimaged is a partition imaging daemon.
#
# processname: partimaged
# config: %{_sysconfdir}/sysconfig/partimaged
# pidfile: %{_localstatedir}/lock/subsys/partimaged

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

### Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0

[ -x %{_sbindir}/partimaged ] || exit 1
[ -r %{_sysconfdir}/sysconfig/partimaged ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/partimaged"
OPTIONS=""

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"
  
RETVAL=0
prog="partimaged"
desc="Partition imaging daemon"

start() {
        echo -n $"Starting $desc ($prog): "
	cd %{_localstatedir}/partimaged
        daemon %{_sbindir}/$prog --daemon $OPTIONS
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

%{__cat} <<EOF >partimaged.logrotate
%{_localstatedir}/log/partimaged.log {
        missingok
        copytruncate
        notifempty
}
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--with-log-dir="%{_localstatedir}/log" \
	--disable-dependency-tracking \
	--disable-ssl \
	--enable-gui-text \
	--enable-gui-newt \
	--enable-all-static 
%{__make} %{?_smp_mflags}
%{__mv} -f src/client/partimage partimage-static
%{__rm} -f src/server/partimaged

%configure \
	--program-prefix="%{?_program_prefix}" \
	--with-log-dir="%{_localstatedir}/log" \
	--disable-dependency-tracking \
	--disable-ssl \
	--with-xinerama \
	--enable-gui-text \
	--enable-gui-newt \
	--enable-gui-qt
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -m0755 partimage-static %{buildroot}%{_sbindir}

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/logrotate.d/ \
			%{buildroot}%{_sysconfdir}/sysconfig/ \
			%{buildroot}%{_localstatedir}/partimaged/ \
			%{buildroot}%{_localstatedir}/log/
%{__install} -m0755 partimaged.sysv %{buildroot}%{_initrddir}/partimaged
%{__install} -m0644 partimaged.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/partimaged
%{__install} -m0644 partimaged.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/partimaged

touch %{buildroot}%{_localstatedir}/log/partimaged.log

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/info/

%pre server
/usr/sbin/useradd -M -r -s "/sbin/nologin" -d "%{_localstatedir}/partimaged" partimag &>/dev/null || :
/usr/sbin/usermod -s "/sbin/nologin" -d "%{_localstatedir}/partimaged" partimag &>/dev/null || :

%post server
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add partimaged
fi
/sbin/service partimaged condrestart &>/dev/null || :

%preun server
if [ $1 -eq 0 ]; then
        /sbin/service partimaged stop &>/dev/null || :
        /sbin/chkconfig --del partimaged
fi

%postun server
/sbin/service partimaged condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BOOT* BUGS ChangeLog COPYING FUTURE README SURVEY THANKS TODO
%{_sbindir}/partimage

%files server
%defattr(-, root, root, 0755)
%doc README.partimaged
%config(noreplace) %{_initrddir}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_sbindir}/partimaged
%defattr(-, partimag, partimag, 0755)
%config(noreplace) %{_sysconfdir}/partimaged/
%dir %{_localstatedir}/partimaged/
%ghost %{_localstatedir}/log/partimaged.log

%files static
%defattr(-, root, root, 0755)
%{_sbindir}/partimage-static

%changelog
* Tue Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Added seperate server package.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
