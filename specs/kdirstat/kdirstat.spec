
%define _name		kdirstat
%define _version	2.4.0
%define _release	2.dries

Summary: a graphical disk usage utility
Summary(nl): grafisch programma dat de grootte van mappen en bestanden toont

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Applications/Utilities
URL: http://kdirstat.sourceforge.net/
Source: http://kdirstat.sourceforge.net/download/kdirstat-2.4.0.tar.bz2
BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
Requires: kdelibs, qt

#(d) primscreenshot: http://kdirstat.sourceforge.net/thumbnails/kdirstat-main.jpg
#(d) screenshotsurl: http://kdirstat.sourceforge.net/kdirstat.html#screen_shots

%description
KDirStat is a graphical disk usage utility, very much like the Unix "du"
command. In addition to that, it comes with some cleanup facilities to
reclaim disk space.

%description -l nl
KDirStat is een grafisch hulpprogramma dat ongeveer hetzelfde doet als "du":
het toont hoeveel bytes gebruikt worden door mappen en bestanden. Het
programma bevat ook een aantal hulpmiddelen om terug vrije ruimte te winnen.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
make

%install
. /etc/profile.d/qt.sh
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS CREDITS COPYING.LIB TODO INSTALL
/usr/bin/kdirstat
/usr/share/applnk/Utilities/kdirstat.desktop
/usr/share/apps/kdirstat/icons/hicolor/16x16/actions/symlink.png
/usr/share/apps/kdirstat/icons/hicolor/32x32/actions/symlink.png
/usr/share/apps/kdirstat/icons/hicolor/48x48/actions/symlink.png
/usr/share/apps/kdirstat/icons/locolor/16x16/actions/symlink.png
/usr/share/apps/kdirstat/kdirstatui.rc
/usr/share/doc/HTML/en/kdirstat
/usr/share/icons/hicolor/16x16/apps/kdirstat.png
/usr/share/icons/hicolor/32x32/apps/kdirstat.png
/usr/share/icons/locolor/16x16/apps/kdirstat.png
/usr/share/icons/locolor/32x32/apps/kdirstat.png
/usr/share/locale/de/LC_MESSAGES/kdirstat.mo
/usr/share/locale/fr/LC_MESSAGES/kdirstat.mo
/usr/share/locale/ja/LC_MESSAGES/kdirstat.mo

%changelog
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-2.dries
- added some BuildRequires and Requires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-1.dries
- first packaging for Fedora Core 1
