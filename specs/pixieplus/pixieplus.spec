# $Id$
# Authority: dries

Summary: Image and photo viewer, browser, manager and simple editor
Name: pixieplus
Version: 0.5.4
Release: 1
License: GPL (to be checked, site down)
Group: Amusements/Graphics
URL: http://www.mosfet.org

# problem: site seems to be down, mosfet.org doesn't exist anymore
# license is GPL i think

BuildRequires: ImageMagick-devel, ImageMagick-c++-devel, libungif-devel, libtiff-devel, qt-devel, gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: pixieplus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
An image and photo viewer, browser, manager and simple editor.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install-strip \
	DESTDIR="%{buildroot}"
rm -f $RPM_BUILD_ROOT/usr/share/mimelnk/image/x-pcx.desktop
rm -f $RPM_BUILD_ROOT/usr/share/applnk/Graphics/pixie-mini.desktop
rm -f $RPM_BUILD_ROOT/usr/share/applnk/Graphics/pixie.desktop
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
cat >  $RPM_BUILD_ROOT/usr/share/applications/pixieplus.desktop <<EOF
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

%files
%defattr(-,root,root, 0755)
/usr/bin/pixie
/usr/lib/libpixie_misc.la
/usr/lib/libpixie_misc.so.1.0.0
/usr/lib/libpixie_misc.so.1
/usr/lib/libpixie_misc.so
/usr/lib/pixie.la
/usr/lib/pixie.so
/usr/share/apps/konqueror/servicemenus/konqPixie.desktop
/usr/share/apps/pixie/doc/en
/usr/share/apps/pixie/pixielogo.jpg
/usr/share/apps/pixie/toolbar/kwin.png
/usr/share/apps/pixie/toolbar/mini-ray.png
/usr/share/apps/pixie/toolbar/mini-run.png
/usr/share/icons/*/*/actions/backimage.png
/usr/share/icons/*/*/actions/brightness.png
/usr/share/icons/*/*/actions/catagory.png
/usr/share/icons/*/*/actions/contrast+.png
/usr/share/icons/*/*/actions/contrast-.png
/usr/share/icons/*/*/actions/dim.png
/usr/share/icons/*/*/actions/forwardimage.png
/usr/share/icons/*/*/actions/hotlistadd.png
/usr/share/icons/*/*/actions/hotlistdel.png
/usr/share/icons/*/*/actions/nextfilelist.png
/usr/share/icons/*/*/actions/prevfilelist.png
/usr/share/icons/*/*/apps/pixie.png
/usr/share/icons/*/*/actions/thumb.png
/usr/share/icons/*/*/actions/window_new.png
/usr/share/icons/*/*/apps/pixie.png
/usr/share/icons/*/*/apps/ray.png
/usr/share/icons/*/*/apps/run.png
/usr/share/mimelnk/image/x-miff.desktop
/usr/share/mimelnk/image/x-pict.desktop
/usr/share/mimelnk/image/x-tga.desktop
/usr/share/mimelnk/image/x-xwd.desktop
/usr/share/applications/pixieplus.desktop

%changelog
* Mon Feb 2 2004 Dries Verachtert <dries@ulyssis.org> 0.5.4-1
- first packaging for Fedora Core 1
