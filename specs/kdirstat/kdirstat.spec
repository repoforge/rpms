# $Id: $

# Authority: dries
# Upstream:

Summary: Graphical disk usage utility
Name: kdirstat
Version: 2.4.0
Release: 3
License: GPL
Group: Applications/File
URL: http://kdirstat.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://kdirstat.sourceforge.net/download/kdirstat-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
Requires: kdelibs, qt

# Screenshot: http://kdirstat.sourceforge.net/thumbnails/kdirstat-main.jpg
# ScreenshotURL: http://kdirstat.sourceforge.net/kdirstat.html#screen_shots

%description
KDirStat is a graphical disk usage utility, very much like the Unix "du"
command. In addition to that, it comes with some cleanup facilities to
reclaim disk space.

%description -l nl
KDirStat is een grafisch hulpprogramma dat ongeveer hetzelfde doet als "du":
het toont hoeveel bytes gebruikt worden door mappen en bestanden. Het
programma bevat ook een aantal hulpmiddelen om terug vrije ruimte te winnen.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%makeinstall
mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}/usr/share/applnk/Utilities/kdirstat.desktop %{buildroot}/usr/share/applications/kdirstat.desktop
echo "Categories=Application;System;X-Red-Hat-Extra" >> %{buildroot}/usr/share/applications/kdirstat.desktop

%files
%defattr(-,root,root,0755)
%doc README COPYING AUTHORS CREDITS COPYING.LIB TODO INSTALL
%{_bindir}/kdirstat
%{_datadir}/applications/kdirstat.desktop
%{_datadir}/apps/kdirstat
%{_datadir}/doc/HTML/en/kdirstat
%{_datadir}/icons/*/*/apps/kdirstat.png
%{_datadir}/locale/*/LC_MESSAGES/kdirstat.mo

%changelog
* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 2.4.0-3
- spec cleanup

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-2
- added some BuildRequires and Requires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-1
- first packaging for Fedora Core 1
