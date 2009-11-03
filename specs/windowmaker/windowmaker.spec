# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define real_name WindowMaker

Summary: Fast, feature rich Window manager
Name: windowmaker
Version: 0.92.0
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.windowmaker.info/

Source: ftp://windowmaker.info/pub/source/release/WindowMaker-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libjpeg-devel, libungif-devel
BuildRequires: libtiff-devel, zlib-devel, gettext, gcc-c++
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Provides: WindowMaker = %{version}-%{release}
Provides: WindowMaker-libs = %{version}-%{release}
Provides: windowmanager
Obsoletes: WindowMaker <= %{version}, WindowMaker-libs <= %{version}

%description
Window Maker is an X11 window manager designed to give additional
integration support to the GNUstep Desktop Environment. In every way
possible, it reproduces the elegant look and feel of the NeXTSTEP[tm]
GUI. It is fast, feature rich, easy to configure, and easy to use. In
addition, Window Maker works with GNOME and KDE, making it one of the
most useful and universal window managers available.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Replace fixed /usr/lib by $(libdir). (Please fix upstream)
%{__perl} -pi.orig -e 's|/usr/lib\b|\$(libdir)|g' WPrefs.app/Makefile.in

%{__cat} <<EOF >windowmaker.xsession
#!/bin/sh
exec /etc/X11/xdm/Xsession wmaker
EOF

%{__cat} <<EOF >windowmaker.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Window Maker
Comment=Start Window Maker
Exec=wmaker
# no icon yet, only the top three are currently used
Icon=
Type=Application
EOF

%build
export LINGUAS="$(cd po; echo *.po | sed -e 's|zh_TW.Big5.po||g; s|.po||g')"
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	--with-appspath="%{_libdir}/GNUstep" \
	--with-nlsdir="%{_datadir}/locale" \
	--enable-gnome \
	--enable-kde \
	--enable-modelock \
	--enable-openlook \
	--enable-usermenu \
	--enable-xinerama \
	--enable-vdesktop
### Does not build with -j X and X > 1
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{real_name}
%find_lang WPrefs
%find_lang WINGs
%{__cat} WINGs.lang WPrefs.lang >> %{real_name}.lang

%{__install} -Dp -m0755 windowmaker.xsession "%{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Window Maker"
%{__install} -Dp -m0644 windowmaker.desktop %{buildroot}%{_sysconfdir}/X11/dm/Sessions/windowmaker.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGFORM BUGS ChangeLog COPYING* FAQ* NEWS README* TODO
%doc %{_mandir}/man1/*.1x*
%doc %{_mandir}/sk/man1/*.1x*
%config %{_sysconfdir}/X11/gdm/Sessions/*
%config %{_sysconfdir}/X11/dm/Sessions/windowmaker.desktop
%config %{_sysconfdir}/WindowMaker/
%{_bindir}/*
%{_libdir}/libwraster.so.*
%{_libdir}/GNUstep/
%{_datadir}/WindowMaker/
%{_datadir}/WINGs/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_includedir}/WINGs/
%{_libdir}/lib*.a
%exclude %{_libdir}/libwraster.la
%{_libdir}/libwraster.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.92.0-1
- Updated to release 0.92.0.

* Thu Nov 25 2004 Juergen Moellenhoff <jm@tp1.rub.de> - 0.91.0-1
- New package for version 0.91.0.
- Fixed $(libdir) for correct wprefspath. (Vamsi K Kambhampati)
- Remove %%{?_smp_mflags} for %%{__make}. (Vamsi K Kambhampati)

* Sun Oct 24 2004 Chris Gordon <chris-rpm@linux-dr.net> - 0.90.0-1
- New package for version 0.90.0.
- Enabled xinerama support.
- Enabled virtual desktop support.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 0.80.2-5
- Added desktop file for GDM menu. (Chris Gordon)
- Fix for x86_64.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.80.2-4
- Fixed the location of WPrefs from /etc/WindowMaker/WMState. (Hasan)

* Mon May 12 2003 Dag Wieers <dag@wieers.com> - 0.80.2-3
- Added "Window Maker" GDM Xsession entry. (Bert de Bruijn)

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.80.2-1
- Provide 'windowmanager'.
- Initial package. (using DAR)
