# $Id$

# Authority: dries
# Screenshot: http://www.kvirc.net/img/awake_spec_windows.jpg
# ScreenshotURL: http://www.kvirc.net/?id=screen

Summary: An IRC client
Name: kvirc
Version: 3.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.kvirc.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.kvirc.net/pub/kvirc/%{version}/source/kvirc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, libvorbis-devel, gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel, arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
BuildRequires: audiofile-devel, fam-devel
%{?fc2:BuildRequires:libselinux-devel}


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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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
%{_datadir}/kvirc
%{_datadir}/icons/hicolor/*/apps/kvirc.png
%{_datadir}/icons/hicolor/*/mimetypes/kvs.png
%{_mandir}/kvirc.*
%{_datadir}/mimelnk/text/x-kvs.desktop
%{_datadir}/services/*.protocol
%{_bindir}/kvi_run_netscape.sh
%{_bindir}/kvirc-config
%{_bindir}/kvi_search_help.sh
%{_bindir}/kvirc
%{_libdir}/libkvilib.*
%{_includedir}/kvirc

%changelog
* Wed Jul 21 2004 Dries Verachtert <dries@ulyssis.org> 3.0.1
- Update to version 3.0.1.

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 3.0.0-snap20040317
- Initial package
