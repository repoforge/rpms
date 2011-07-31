# $Id$
# Authority: dag
# Upstream: Fabrice Bellard <fabrice$bellard,org>
#
# ExclusiveDist: el5 el6
#
# AIO, KVM & Spice are only enabled on EL6 
#

### EL6 ships with qemu-img-2:0.12.1-2.113
%{?el6:# Tag: rfx}
### EL5 ships with qemu-img-83-164.el5_5.23
%{?el5:# Tag: rfx}

%define audio_drv_list alsa,esd,oss,sdl

Summary: CPU emulator
Name: qemu
Version: 0.14.1
Release: 2%{?dist}
# Epoch because upstream pushed qemu-1.0 package
Epoch: 2
License: GPLv2+ and LGPLv2+ and BSD
Group: Applications/Emulators
URL: http://qemu.org/

Source0: http://download.savannah.gnu.org/releases/qemu/qemu-%{version}.tar.gz
Source1: qemu.init

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel
BuildRequires: bluez-libs-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: esound-devel
BuildRequires: gnutls-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: ncurses-devel
BuildRequires: pciutils-devel
BuildRequires: rsync
BuildRequires: texi2html
BuildRequires: texinfo
BuildRequires: which
BuildRequires: zlib-devel

%ifarch x86_64
%{?el6:BuildRequires: spice-protocol >= 0.6.0 spice-server-devel >= 0.6.0}
%endif

%{?el6:BuildRequires: libcurl-devel}
%{?el5:BuildRequires: curl-devel}

%{?el6:BuildRequires: libuuid-devel}
%{?el6:BuildRequires: pulseaudio-libs-devel}

Requires: %{name}-img

Requires(post): /usr/bin/getent
Requires(post): /usr/sbin/groupadd
Requires(post): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(post): /sbin/service
Requires(preun): /sbin/service /sbin/chkconfig
Requires(postun): /sbin/service

Provides: %{name}-common
Provides: %{name}-user

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

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Development/Tools

%description img
This package provides a command line tool for manipulating disk images

%prep
%setup

%build

%if 0%{?el6}
    # --build-id option is used fedora 8 onwards for giving info to the debug packages.
    extraldflags="-Wl,--build-id";
    buildldflags="VL_LDFLAGS=-Wl,--build-id"
%endif

./configure \
    --prefix="%{_prefix}" \
    --sysconfdir=%{_sysconfdir} \
    --interp-prefix="%{_prefix}/qemu-%%M" \
    --audio-drv-list="%{?el6:pa,}%{audio_drv_list}" \
    --audio-card-list="ac97,adlib,cs4231a,es1370,gus,sb16" \
    --extra-ldflags=$extraldflags \
    --extra-cflags="%{optflags}" \
    --enable-attr \
    --enable-bluez \
    --enable-curl \
    --enable-docs \
    --enable-vnc-sasl \
    --enable-vnc-tls \
    --enable-uuid \
%if 0%{?el6}
    --enable-linux-aio \
    --enable-kvm \
%endif
%ifarch x86_64
    %{?el6:--enable-spice} \
%endif
    --disable-check-utests \
    --disable-debug-tcg \
    --disable-sparse \
    --disable-strip \
    --disable-werror \
    --disable-xen

echo "config-host.mak contents:"
echo "==="
cat config-host.mak
echo "==="

make V=1 %{?_smp_mflags} $buildldflags

%install
%{__rm} -rf %{buildroot}

%{__make} install \
    prefix="%{buildroot}%{_prefix}" \
    bindir="%{buildroot}%{_bindir}" \
    sharedir="%{buildroot}%{_datadir}/%{name}" \
    sysconfdir="%{buildroot}%{_sysconfdir}" \
    confdir="%{buildroot}%{_sysconfdir}/%{name}" \
    mandir="%{buildroot}%{_mandir}" \
    datadir="%{buildroot}%{_datadir}/%{name}" \
    docdir="./rpm-doc"

chmod -x ${RPM_BUILD_ROOT}%{_mandir}/man1/*

install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/qemu
install -D -p -m 0644 qemu.sasl $RPM_BUILD_ROOT%{_sysconfdir}/sasl2/qemu.conf

%post
if [ $1 -eq 1 ]; then
    getent group kvm >/dev/null || groupadd -g 36 -r kvm
    getent group qemu >/dev/null || groupadd -g 107 -r qemu
    getent passwd qemu >/dev/null || \
      useradd -r -u 107 -g qemu -G kvm -d / -s /sbin/nologin \
        -c "qemu user" qemu
    /sbin/chkconfig --add %{name}
    /sbin/service %{name} start &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop &>/dev/null || :
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING* LICENSE README* TODO
%config(noreplace) %{_sysconfdir}/qemu/target-x86_64.conf
%config %{_initrddir}/qemu
%{_bindir}/qemu*
%{_datadir}/qemu/
%config(noreplace) %{_sysconfdir}/sasl2/qemu.conf
%{_mandir}/man1/qemu.1*
%{_mandir}/man8/qemu-nbd.8*
%exclude %{_bindir}/qemu-img
%exclude %{_bindir}/qemu-io

%files img
%defattr(-, root, root, 0755)
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_mandir}/man1/qemu-img.1*

%changelog
* Sun Jul 31 2011 Yury V. Zaytsev <yury@shurup.com> - 0.14.1-2
- Dropped support for RHEL4-, glibc is too old.
- Synced features with RHEL / Fedora packages.

* Fri Jul 29 2011 Arnoud Vermeer <a.vermeer@freshway.biz> - 0.14.1-1
- Updated to release 0.14.1.

* Mon Mar 21 2011 Dag Wieers <dag@wieers.com> - 0.14.0-1
- Updated to release 0.14.0.
- Split off qemu-img package.

* Sat Nov 13 2010 Dag Wieers <dag@wieers.com> - 0.13.0-1
- Updated to release 0.13.0.

* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 0.12.4-1
- Updated to release 0.12.4.

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
