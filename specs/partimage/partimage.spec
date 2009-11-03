# $Id$
# Authority: dag
# Upstream: François Dupoux <fdupoux$partimage,org>

Summary: partition imaging utility, much like Ghost
Name: partimage
Version: 0.6.7
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.partimage.org/

Source: http://dl.sf.net/partimage/partimage-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: parted-devel, newt-devel, libmcrypt-devel, gcc-c++, autoconf, bzip2-devel

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
Summary: partition imaging utility, much like Ghost
Group: Applications/System

%description static
Partition Image is a Linux/UNIX partition imaging utility: it saves all used
blocks in a partition to an image file. This image file can be compressed
using gzip or bzip2 compression to save space, and even split into multiple
files to be copied to movable media such as Zip disks or CD-R.

This package contains a static compiled binary.

%package server
Summary: The server part of a partition imaging utility, much like Ghost
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
%{__perl} -pi.orig -e 's|^\tchown partimag:root.*$|\\|' Makefile.in

### FIXME: Fix mkinstalldirs during 'make install' in po/
%{__perl} -pi.orig -e 's|^(mkinstalldirs) = .+$|$1 = %{__mkdir_p}|' po/Makefile.in.in

%{__cat} <<EOF >partimaged.sysconfig
### See partimaged --help for more information on these options.
###

#OPTIONS="--port=1234 --chroot %{_localstatedir}/partimaged --nologin"
EOF

%{__cat} <<EOF >partimaged.pam
auth     required        pam_unix.so
auth     required        pam.warn.so
auth     required        pam_listfile.so onerr=fail item=user sense=allow file=/etc/partimaged/partimagedusers
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
#configure \
#   --program-prefix="%{?_program_prefix}" \
#   --with-log-dir="%{_localstatedir}/log" \
#   --enable-pam \
#   --disable-ssl \
#   --enable-gui-text \
#   --enable-gui-newt \
#   --enable-all-static
#%{__make} %{?_smp_mflags}
#%{__mv} -f src/client/partimage partimage-static
#%{__rm} -f src/server/partimaged

%configure \
    --program-prefix="%{?_program_prefix}" \
    --with-log-dir="%{_localstatedir}/log" \
    --disable-ssl \
    --with-xinerama \
    --enable-gui-text \
    --enable-gui-newt \
    --enable-gui-qt
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

#%{__install} -Dp -m0755 partimage-static %{buildroot}%{_sbindir}/partimage-static

%{__install} -Dp -m0755 partimaged.sysv %{buildroot}%{_initrddir}/partimaged
%{__install} -Dp -m0644 partimaged.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/partimaged
%{__install} -Dp -m0644 partimaged.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/partimaged
%{__install} -Dp -m0644 partimaged.pam %{buildroot}%{_sysconfdir}/pam.d/partimaged

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/partimaged.log

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/partimaged/

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
%doc AUTHORS BOOT* BUGS ChangeLog COPYING FUTURE README* THANKS TODO
%{_sbindir}/partimage
%exclude %{_docdir}/partimage/

%files server
%defattr(-, root, root, 0755)
%doc AUTHORS BOOT* BUGS ChangeLog COPYING FUTURE README* THANKS TODO
%config(noreplace) %{_initrddir}/partimaged
%config(noreplace) %{_sysconfdir}/logrotate.d/partimaged
%config(noreplace) %{_sysconfdir}/sysconfig/partimaged
%config(noreplace) %{_sysconfdir}/pam.d/partimaged
%{_sbindir}/partimaged

%defattr(-, partimag, partimag, 0755)
%config(noreplace) %{_sysconfdir}/partimaged/
%dir %{_localstatedir}/partimaged/
%ghost %{_localstatedir}/log/partimaged.log

#%files static
#%defattr(-, root, root, 0755)
#%doc AUTHORS BOOT* BUGS ChangeLog COPYING FUTURE README* THANKS TODO
#%{_sbindir}/partimage-static

%changelog
* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Updated to release 0.6.7.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 0.6.6-1
- Updated to release 0.6.6.

* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Tue Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Added seperate server package.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
