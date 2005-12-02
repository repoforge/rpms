# $Id$
# Authority: dries
# Screenshot: http://gwenview.sourceforge.net/screenshots/shots/thumbs/6.png
# ScreenshotURL: http://gwenview.sourceforge.net/screenshots/

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

### Temporary exclude as it loops endlessly in configure on x86_64
# ExcludeDist: el4

Summary: Image viewer for KDE
Name: gwenview
Version: 1.3.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://gwenview.sourceforge.net/

Source: http://dl.sf.net/gwenview/gwenview-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel
BuildRequires: libpng-devel, arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc, make, gcc-c++
BuildRequires: qt-devel, libexif-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Gwenview can load and save all image formats supported by KDE and 
also browse GIMP files (*.xcf). It can also show meta-information and zoom
images to any size. 

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS NEWS README TODO
%{_bindir}/gwenview
%{_libdir}/kde3/libgv*
%{_libdir}/kde3/gwenview.*
%{_libdir}/libgwenview*
%{_libdir}/libkdeinit_gwenview.*
%{_datadir}/doc/HTML/en/gwenview
%{_datadir}/apps/gv*
%{_datadir}/applications/kde/gwenview.desktop
%{_datadir}/apps/gwenview
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_datadir}/icons/*/*/apps/gwenview.png
#%{_datadir}/icons/*/*/apps/imagegallery.png
%{_datadir}/services/gv*.desktop
%{_datadir}/man/man1/gwenview*

%changelog
* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Updated to release 1.3.0.

* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> 1.2.0-1
- Updated to release 1.2.0.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> 1.1.8-1
- Updated to release 1.1.8.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.1.6-1
- update to 1.1.6

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.1.5-1
- update to 1.1.5

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> 1.1.3-1
- update to 1.1.3

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 1.1.2-1
- update to 1.1.2

* Tue Jan 27 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- update to version 1.0.1

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-2
- completion of spec file (descriptions)
- added some BuildRequires

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1

