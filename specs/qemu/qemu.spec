# $Id$
# Authority: dag
# Upstream: Fabrice Bellard <fabrice$bellard,org>


%define audio_drv_list alsa,esd,oss,sdl

%{?el5:%define _with_compat_gcc_version 34}
%{?el4:%define _without_bluez 1}
%{?el3:%define audio_drv_list esd,oss,sdl}
%{?el3:%define _without_bluez 1}
%{?rh9:%define audio_drv_list esd,oss,sdl}
%{?rh9:%define _without_bluez 1}

Summary: CPU emulator
Name: qemu
Version: 0.10.6
Release: 1%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://qemu.org/

Source: http://download.savannah.gnu.org/releases/qemu/qemu-%{version}.tar.gz
Patch0: qemu-0.7.0-build.patch
Patch2: qemu-0.9.1-dhcp.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel
BuildRequires: zlib-devel
%{?_with_compat_gcc_version:BuildRequires: compat-gcc-%{_with_compat_gcc_version}}
#BuildRequires: texi2html

%description
QEMU is a FAST! processor emulator using dynamic translation to achieve good
emulation speed. QEMU has two operating modes:

    Full system emulation. In this mode, QEMU emulates a full system (for
    example a PC), including a processor and various peripherials. It can
    be used to launch different Operating Systems without rebooting the PC
    or to debug system code.

    User mode emulation (Linux host only). In this mode, QEMU can launch
    Linux processes compiled for one CPU on another CPU. It can be used to
    launch the Wine Windows API emulator or to ease cross-compilation and
    cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy to use.
QEMU is a FAST! processor emulator. By using dynamic translation it achieves a
reasonnable speed while being easy to port on new host CPUs.

%prep
%setup
%patch0 -p1
%patch2 -p1

%{__cat} <<'EOF' >qemu.sysv
#!/bin/sh
#
# Init file for configuring Qemu non-native binary formats
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: 2345 35 98
# description: Qemu non-native binary formats

source %{_initrddir}/functions

RETVAL=0
prog="qemu"

start() {
    case "$(uname -m)" in
        (i386|i486|i586|i686|i86pc|BePC)
            cpu="i386";;
        ("Power Macintosh"|ppc|ppc64)
            cpu="ppc";;
        (armv4l|armv5l)
            cpu="arm";;
        (sh4)
            cpu="sh4";;
    esac
    echo -n $"Registering non-native binary handler for Qemu"
    /sbin/modprobe binfmt_misc &>/dev/null
    if [ "$cpu" != "i386" -a -x "%{_bindir}/qemu-i386" -a -d "%{_prefix}/qemu-i386" ]; then
        echo ':qemu-i386:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00:\xff\xff\xff\xff\xff\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-i386:' >/proc/sys/fs/binfmt_misc/register
        echo ':qemu-i486:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00:\xff\xff\xff\xff\xff\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-i386:' >/proc/sys/fs/binfmt_misc/register
    fi
    if [ "$cpu" != "arm" -a -x "%{_bindir}/qemu-arm" -a -d "%{_prefix}/qemu-arm" ]; then
        echo ':qemu-arm:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x28\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-arm:' >/proc/sys/fs/binfmt_misc/register
    fi
    if [ "$cpu" != "ppc" -a -x "%{_bindir}/qemu-ppc" -a -d "%{_prefix}/qemu-ppc" ]; then
        echo ':ppc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x14:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-ppc:' >/proc/sys/fs/binfmt_misc/register
    fi
    if [ "$cpu" != "sparc" -a -x "%{_bindir}/qemu-sparc" -a -d "%{_prefix}/qemu-sparc" ]; then
        echo ':qemu-sparc:M::\x7fELF\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02:\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-sparc:' >/proc/sys/fs/binfmt_misc/register
    fi
    if [ "$cpu" != "sh4" -a -x "%{_bindir}/qemu-sh4" -a -d "%{_prefix}/qemu-sh4" ]; then
        echo ':qemu-sh4:M::\x7fELF\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x2a\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff:%{_bindir}/qemu-sh4:' >/proc/sys/fs/binfmt_misc/register
    fi

    echo
}

stop() {
    echo -n $"Unregistering non-native binary handler for Qemu"
    for cpu in i386 i486 ppc arm sparc sh4; do
        if [ -r "/proc/sys/fs/binfmt_misc/qemu-$cpu" ]; then
            echo "-1" >/proc/sys/fs/binfmt_misc/qemu-$cpu
        fi
    done
    echo
}

restart() {
    stop
    start
}

status() {
    if ls /proc/sys/fs/binfmt_misc/qemu-* &>/dev/null; then
        echo $"Qemu non-native binary format handlers registered."
        return 0
    else
        echo $"Qemu non-native binary format handlers not registered."
        return 1
    fi
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
    if status &>/dev/null; then
        restart
    fi
    ;;
  status)
    status
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $prog {start|stop|restart|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
./configure \
    --prefix="%{_prefix}" \
    --cc="gcc%{?_with_compat_gcc_version}" \
    --interp-prefix="%{_prefix}/qemu-%%M" \
    --audio-drv-list="%{audio_drv_list}" \
    --audio-card-list="ac97,adlib,cs4231a,es1370,gus,sb16" \
%{?_without_bluez:--disable-bluez}
#   --disable-gcc-check
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
    prefix="%{buildroot}%{_prefix}" \
    bindir="%{buildroot}%{_bindir}" \
    sharedir="%{buildroot}%{_datadir}/qemu" \
    mandir="%{buildroot}%{_mandir}" \
    datadir="%{buildroot}%{_datadir}/qemu" \
    docdir="./rpm-doc"

%{__install} -Dp -m0755 qemu.sysv %{buildroot}%{_initrddir}/qemu

%post
/sbin/chkconfig --add qemu
/sbin/service qemu start &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/service qemu stop &>/dev/null || :
    /sbin/chkconfig --del qemu
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING* LICENSE README* TODO *.html
%doc %{_mandir}/man1/qemu.1*
%doc %{_mandir}/man1/qemu-img.1*
%doc %{_mandir}/man8/qemu-nbd.8*
%config %{_initrddir}/qemu
%{_bindir}/qemu*
%{_datadir}/qemu/

%changelog
* Thu Oct 22 2009 Dag Wieers <dag@wieers.com> - 0.10.6-1
- Updated to release 0.10.6.

* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 0.10.5-1
- Updated to release 0.10.5.

* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 0.10.4-1
- Updated to release 0.10.4.

* Sat May 02 2009 Dag Wieers <dag@wieers.com> - 0.10.3-1
- Updated to release 0.10.3.

* Tue Apr 14 2009 Dag Wieers <dag@wieers.com> - 0.10.2-1
- Updated to release 0.10.2.

* Mon Mar 23 2009 Dag Wieers <dag@wieers.com> - 0.10.1-1
- Updated to release 0.10.1.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Thu May 10 2007 Dag Wieers <dag@wieers.com> - 0.9.0-2
- Added patches from Fedora.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Tue Dec 19 2006 Marc Abramowitz <marc@abramowitz.info> - 0.8.2-1
- Updated to release 0.8.2.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Thu Dec 29 2005 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Sun May 01 2005 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Mar 23 2005 Dag Wieers <dag@wieers.com> - 0.6.1-3
- Removed erroneous dovecot reference. (Zoltán Vörösbaranyi)

* Mon Feb 28 2005 Dag Wieers <dag@wieers.com> - 0.6.1-2
- Added SDL-devel buildrequirement. (Matthias Saou)
- Fix for build problem on FC2.

* Wed Nov 17 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.5.5-3
- Fixed SDL relocation error on fc2. (David Woodhouse)

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.5.5-2
- Fixed libc.so.6(GLIBC_PRIVATE) dependency for fc2. (Christopher Stone)

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (using DAR)
