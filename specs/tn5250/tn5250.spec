# $Id$
# Authority: dag
# Upstream: <linux5250$midrange,com>

### EL6 ships with tn5250-0.17.4-3.2.el6
### EL5 ships with tn5250-0.17.3-6
### EL4 ships with tn5250-0.16.5-2
%{?el4:# Tag: rfx}
### EL3 ships with tn5250-0.16.5-1
%{?el3:# Tag: rfx}
# ExclusiveDist: el2 el3 el4

%{?el5:%define _without_slang 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: 5250 Telnet protocol and terminal program
Name: tn5250
Version: 0.17.3
Release: 2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://tn5250.sourceforge.net/

Source: http://dl.sf.net/tn5250/tn5250-%{version}.tar.gz
Patch0: tn5250-0.16.5-bhc.patch
Patch1: tn5250-0.17.3-multilib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses, slang-devel, openssl-devel, krb5-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
tn5250 is an implementation of the 5250 Telnet protocol.
It provide 5250 library and 5250 terminal emulation.

%package devel
Summary: header files and libraries needed for lib5250 development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package includes the header files and libraries needed for
developing programs using lib5250.

%prep
%setup
%patch0 -p1
%patch1 -p1

%{__cat} <<EOF >xt5250.desktop
[Desktop Entry]
Encoding=UTF-8
Name=tn5250 terminal emulation
Comment=tn5250 emulates IBM 5250 compatible terminals to connect over TCP/IP to an IBM AS/400
Exec=xt5250
Icon=tn5250.png
Type=Application
Categories=Application;Network;X-Red-Hat-Base;
Terminal=false
EOF

%build
#{?fc1:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
#{?el3:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
#{?rh9:perl -pi.orig -e 's|^INCLUDES = |INCLUDES = -I/usr/kerberos/include |' src/Makefile.in}
touch -r aclocal.m4 configure configure.in
%configure \
    CPPFLAGS="-I/usr/kerberos/include" \
    CFLAGS="%{optflags}" \
    --disable-static \
%{!?_without_slang:--with-slang} \
    --with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 linux/5250.tcap %{buildroot}%{_datadir}/tn5250/5250.tcap
%{__install} -Dp -m0644 linux/5250.terminfo %{buildroot}%{_datadir}/tn5250/5250.terminfo
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -p -m0644 *.png *.xpm %{buildroot}%{_datadir}/pixmaps/
%{__install} -Dp -m0644 tn5250-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tn5250.png
%{__install} -Dp -m0644 tn5250-48x48.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tn5250.xpm
%{__install} -Dp -m0644 tn5250-62x48.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/tn5250.png
%{__install} -Dp -m0644 tn5250-62x48.xpm %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/tn5250.xpm

%if %{?_without_freedesktop:1}0
    %{__install} -D -m0644 xt5250.desktop %{buildroot}/etc/X11/applnk/Utilities/xt5250.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}  \
        --dir %{buildroot}%{_datadir}/applications/  \
        xt5250.desktop
%endif

export TERMINFO="%{buildroot}%{_datadir}/terminfo/"
/usr/bin/tic linux/5250.terminfo
#/usr/bin/tic -o%{buildroot}%{_datadir}/terminfo/ linux/5250.terminfo

### Clean up docs
%{__rm} -f doc/Makefile*

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor ||:
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor ||:

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor ||:
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor ||:

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO doc/* linux/*.map
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man5/tn5250rc.5*
%{_bindir}/lp5250d
%{_bindir}/scs2*
#%{_bindir}/tn3270d
%{_bindir}/tn5250
#%{_bindir}/tn5250d
%{_bindir}/xt5250
%{_datadir}/tn5250/
%{_datadir}/icons/hicolor/*/apps/tn5250.*
%{_datadir}/pixmaps/tn5250-*
%dir %{_datadir}/terminfo/
%dir %{_datadir}/terminfo/5/
%{_datadir}/terminfo/5/5250
%dir %{_datadir}/terminfo/x/
%{_datadir}/terminfo/x/xterm-5250
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xt5250.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Utilities/xt5250.desktop}
%{_libdir}/lib5250.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/tn5250-config
%{_datadir}/aclocal/tn5250.m4
%{_includedir}/tn5250/
%{_includedir}/tn5250.h
%{_libdir}/lib5250.so
%{_libdir}/pkgconfig/tn5250.pc
%exclude %{_libdir}/lib5250.la

%changelog
* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 0.17.3-2
- Added patches to build on RHEL5.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.17.3-1
- Updated to release 0.17.3.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.16.5-0
- Updated to release 0.16.5.

* Wed Feb  9 2000 Dag Wieers <dag@wieers.com> - 0.15.6-0
- Updated to release 0.15.6.

* Mon Nov 15 1999 Dag Wieers <dag@wieers.com> - 0.14.0-0
- Initial package.
