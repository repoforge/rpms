# $Id$

# Authority: dries
# Screenshot: http://gwenview.sourceforge.net/screenshots/shots/thumbs/6.png
# ScreenshotURL: http://gwenview.sourceforge.net/screenshots/

Summary: Image viewer for KDE
Name: gwenview
Version: 1.0.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://gwenview.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/gwenview/gwenview-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

%description
Gwenview can load and save all image formats supported by KDE and 
also browse GIMP files (*.xcf). It can also show meta-information and zoom
images to any size. 

%description -l nl
Gwenview is een image viewer die de formaten ondersteund door KDE kan openen
en bewaren. Ook kan het GIMP bestanden (*.xcf) openen. Het kan ook meta
informatie tonen en zoomen.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
make install \
	DESTDIR="%{buildroot}"

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS COPYING CREDITS NEWS TODO
/usr/bin/gwenview
/usr/share/applications/kde/gwenview.desktop
/usr/share/apps/gwenview
/usr/share/apps/konqueror/servicemenus/konqgwenview.desktop
/usr/share/icons/*/*/apps/gwenview.png
/usr/share/locale/*/LC_MESSAGES/gwenview.mo
/usr/share/man/man1/gwenview.1.gz


%changelog
* Tue Jan 27 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- update to version 1.0.1

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-2
- completion of spec file (descriptions)
- added some BuildRequires

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1
