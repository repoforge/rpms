# $Id: $

# Authority: dries

Summary: An IRC client
Name: kvirc
Version: 3.0.0_snap20040317
%define rversion 3.0.0-snap20040317
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.kvirc.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.kvirc.net/pub/kvirc/snapshots/source/kvirc-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: openssl-devel, libvorbis-devel, gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel, audiofile-devel
%{?fc2:BuildRequires:libselinux-devel}

# Screenshot: http://www.kvirc.net/img/trex_shot1.jpg
# ScreenshotURL: http://www.kvirc.net/?id=screen

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
%setup -n kvirc-3.0.0-beta3

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
  applnkdir=%{buildroot}/usr/share/applications \
  iconapps32datadir=%{buildroot}/usr/share/icons/hicolor/32x32/apps \
  iconapps48datadir=%{buildroot}/usr/share/icons/hicolor/48x48/apps \
  iconmime32datadir=%{buildroot}/usr/share/icons/hicolor/32x32/mimetypes \
  iconmime48datadir=%{buildroot}/usr/share/icons/hicolor/48x48/mimetypes \
  mimelnkdir=%{buildroot}/usr/share/mimelnk/text \
  kdeservicesdir=%{buildroot}/usr/share/services
echo "Categories=Application;Network;X-Red-Hat-Extra" >> %{buildroot}/usr/share/applications/kvirc.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README FAQ TODO ChangeLog
%{_datadir}/applications/kvirc.desktop
%{_datadir}/kvirc/3.0.0-beta3
%{_datadir}/icons/hicolor/*/apps/kvirc.png
%{_datadir}/icons/hicolor/*/mimetypes/kvs.png
%{_datadir}/man/kvirc.1
%{_datadir}/mimelnk/text/x-kvs.desktop
%{_datadir}/services/*.protocol
%{_bindir}/kvi_run_netscape.sh
%{_bindir}/kvirc-config
%{_bindir}/kvi_search_help.sh
%{_bindir}/kvirc
%{_libdir}/libkvilib.so.3.0.0
%{_libdir}/libkvilib.so.3
%{_libdir}/libkvilib.so
%{_libdir}/libkvilib.la
%{_includedir}/kvirc/3.0.0-beta3

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 3.0.0-snap20040317
- Initial package
