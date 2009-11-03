# $Id$
# Authority: dries

%define real_version 1.0a2

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Image and photo viewer, browser, manager and simple editor
Name: pixieplus
Version: 1.0
Release: 0.a2.1%{?dist}
License: BSD
Group: Amusements/Graphics
URL: http://www.mosfet.org

BuildRequires: ImageMagick-devel, ImageMagick-c++-devel
BuildRequires: libungif-devel, libtiff-devel, qt-devel
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel
BuildRequires: libpng-devel, arts-devel, zlib-devel
BuildRequires: kdelibs-devel, make, gcc-c++, automake, autoconf
%{?fc3:BuildRequires:libselinux-devel, libexif-devel, libexif}
%{?fc2:BuildRequires:libselinux-devel, libexif-devel, libexif}

Source: http://www.mosfet.org/pixie/Pixie-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
An image and photo viewer, browser, manager and simple editor.

%prep
%setup -n pixie

%build
source /etc/profile.d/qt.sh
%{__make} -f Makefile.cvs
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
* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.0a2
- Updated to release 1.0a2.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4.2-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> 0.5.4.2-1
- update to version 0.5.4.2

* Mon Feb 2 2004 Dries Verachtert <dries@ulyssis.org> 0.5.4-1
- first packaging for Fedora Core 1
