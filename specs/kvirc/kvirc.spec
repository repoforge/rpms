# $Id$

# Authority: dries
# Screenshot: http://www.kvirc.net/img/awake_spec_windows.jpg
# ScreenshotURL: http://www.kvirc.net/?id=screen


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: IRC client
Name: kvirc
Version: 3.2.0
Release: 3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kvirc.net/

Source: ftp://ftp.kvirc.net/pub/kvirc/%{version}/source/kvirc-%{version}.tar.bz2
Patch: kvirc-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, libvorbis-devel, gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel, arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc, make, gcc-c++, qt-devel >= 3.2
BuildRequires: audiofile-devel, fam-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
Kvirc is an irc client with the following features:
- full GUI based configuration
- MDI floatable windows
- builtin ehlp browser
- extreme themeability
- pseudo transparancy
- proxy support
- ipv6 support
- ssl support
- very modular
- scripting (with OOP)

%prep
%setup -n kvirc-%{version}
%patch -p1

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall \
  applnkdir=%{buildroot}/usr/share/applications \
  iconapps16datadir=%{buildroot}/usr/share/icons/hicolor/16x16/apps \
  iconapps32datadir=%{buildroot}/usr/share/icons/hicolor/32x32/apps \
  iconapps48datadir=%{buildroot}/usr/share/icons/hicolor/48x48/apps \
  iconapps64datadir=%{buildroot}/usr/share/icons/hicolor/64x64/apps \
  iconmime16datadir=%{buildroot}/usr/share/icons/hicolor/16x16/mimetypes \
  iconmime32datadir=%{buildroot}/usr/share/icons/hicolor/32x32/mimetypes \
  iconmime48datadir=%{buildroot}/usr/share/icons/hicolor/48x48/mimetypes \
  iconmime64datadir=%{buildroot}/usr/share/icons/hicolor/64x64/mimetypes \
  mimelnkdir=%{buildroot}/usr/share/mimelnk/text \
  kdeservicesdir=%{buildroot}/usr/share/services
echo "Categories=Application;Network;X-Red-Hat-Extra" >> %{buildroot}/usr/share/applications/kvirc.desktop
%{__rm} -f %{buildroot}%{_datadir}/services/irc.protocol

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog FAQ README TODO
%{_datadir}/applications/kvirc.desktop
%{_datadir}/kvirc
%{_datadir}/icons/hicolor/*/apps/kvirc.png
%{_datadir}/icons/hicolor/*/mimetypes/kvs.png
%{_mandir}/man1/kvirc.*
%{_datadir}/mimelnk/text/x-kvs.desktop
%{_datadir}/services/*.protocol
%{_bindir}/kvi_run_netscape.sh
%{_bindir}/kvirc-config
%{_bindir}/kvi_search_help.sh
%{_bindir}/kvirc
%{_libdir}/libkvilib.*
%{_includedir}/kvirc

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 3.2.0-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun Apr 03 2005 Dries Verachtert <dries@ulyssis.org> 3.2.0-2
- Avoid conflict with kdenetwork (thanks to Spetiam).

* Sun Mar 06 2005 Dries Verachtert <dries@ulyssis.org> 3.2.0-1
- Update to version 3.2.0.

* Wed Jul 21 2004 Dries Verachtert <dries@ulyssis.org> 3.0.1
- Update to version 3.0.1.

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 3.0.0-snap20040317
- Initial package
