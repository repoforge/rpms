# $Id$
# Authority: dries
# Screenshot: http://gwenview.sourceforge.net/screenshots/shots/thumbs/6.png
# ScreenshotURL: http://gwenview.sourceforge.net/screenshots/

%{?dtag: %{expand: %%define %dtag 1}}

### Temporary exclude as it loops endlessly in configure on x86_64
##ExcludeDist: el4

Summary: Image viewer for KDE
Name: gwenview
Version: 1.4.2
Release: 3
License: GPL
Group: Amusements/Graphics
URL: http://gwenview.sourceforge.net/

Source: http://dl.sf.net/gwenview/gwenview-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libjpeg-devel, exiv2-devel
BuildRequires: libpng-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc-c++
BuildRequires: qt-devel, libexif-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/gwenview*
%{_bindir}/gwenview
%{_datadir}/doc/HTML/*/gwenview/
%{_datadir}/apps/gv*
%{_datadir}/apps/kconf_update/gwenview*
%{_datadir}/config.kcfg/gv*
%{_datadir}/applications/kde/gwenview.desktop
%{_datadir}/apps/gwenview
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_datadir}/icons/*/*/apps/gwenview.*
%{_datadir}/icons/*/*/apps/gvdirpart.*
#%{_datadir}/icons/*/*/apps/imagegallery.png
%{_datadir}/services/gv*.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_libdir}/kde3/libgv*
%{_libdir}/kde3/gwenview.*
%{_libdir}/libgwenview*
%{_libdir}/libkdeinit_gwenview.*

%changelog
* Wed Dec 24 2008 Dag Wieers <dag@wieers.com> - 1.4.2-3
- Rebuild against exiv2 0.17.

* Sun Jan 13 2008 Dag Wieers <dag@wieers.com> - 1.4.2-2
- Rebuild against exiv2 0.16.

* Wed Sep 19 2007 Dries Verachtert <dries@ulyssis.org> - 1.4.2-1
- Updated to release 1.4.2.

* Mon Nov 27 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Updated to release 1.4.1.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.0-1
- Updated to release 1.4.0.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.1-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

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

