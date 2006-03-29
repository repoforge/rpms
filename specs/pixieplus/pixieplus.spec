# $Id$
# Authority: dries

%define real_version 0.5.4-2

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Image and photo viewer, browser, manager and simple editor
Name: pixieplus
Version: 0.5.4.2
Release: 1
License: BSD
Group: Amusements/Graphics
URL: http://www.mosfet.org

BuildRequires: ImageMagick-devel, ImageMagick-c++-devel
BuildRequires: libungif-devel, libtiff-devel, qt-devel
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel
BuildRequires: libpng-devel, arts-devel, zlib-devel
BuildRequires: kdelibs-devel, make, gcc-c++
%{?fc3:BuildRequires:libselinux-devel, libexif-devel, libexif}
%{?fc2:BuildRequires:libselinux-devel, libexif-devel, libexif}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

Source: http://http.us.debian.org/debian/pool/main/p/pixieplus/pixieplus_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
An image and photo viewer, browser, manager and simple editor.

%prep
%setup -n pixieplus-0.5.4

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install-strip \
	DESTDIR="%{buildroot}"
%{__rm} -f %{buildroot}/usr/share/mimelnk/image/x-pcx.desktop
%{__rm} -f %{buildroot}/usr/share/applnk/Graphics/pixie-mini.desktop
%{__rm} -f %{buildroot}/usr/share/applnk/Graphics/pixie.desktop
%{__mkdir_p} %{buildroot}/usr/share/applications/
%{__cat} >  %{buildroot}/usr/share/applications/pixieplus.desktop <<EOF
[Desktop Entry]
Type=Application
Comment=PixiePlus Image Manager and Editor
Icon=pixie
Name=PixiePlus Image Manager
Exec=pixie %f
MapNotify=true
MimeType=image/gif;image/x-xpm;image/x-xbm;image/jpeg;image/x-bmp;image/png;image/x-jng;image/x-pcx;image/x-miff;image/x-pict;image/x-tga;image/x-xwd
InitialPreference=5
DocPath=pixie/index.html
Encoding=UTF-8
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/pixie
%{_libdir}/libpixie_misc.*
%{_libdir}/pixie.*
%{_datadir}/apps/konqueror/servicemenus/konqPixie.desktop
%{_datadir}/apps/pixie/doc/en
%{_datadir}/apps/pixie/pixielogo.jpg
%{_datadir}/apps/pixie/toolbar/*.png
%{_datadir}/icons/*/*/actions/*.png
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/mimelnk/image/x-miff.desktop
%{_datadir}/mimelnk/image/x-pict.desktop
%{_datadir}/mimelnk/image/x-tga.desktop
%{_datadir}/mimelnk/image/x-xwd.desktop
%{_datadir}/applications/pixieplus.desktop

%changelog
* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> 0.5.4.2-1
- update to version 0.5.4.2

* Mon Feb 2 2004 Dries Verachtert <dries@ulyssis.org> 0.5.4-1
- first packaging for Fedora Core 1
