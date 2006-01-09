# $Id$
# Authority: dries
# Upstream:
# Screenshot: http://kdirstat.sourceforge.net/thumbnails/kdirstat-main.jpg
# ScreenshotURL: http://kdirstat.sourceforge.net/kdirstat.html#screen_shots

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Graphical disk usage utility
Name: kdirstat
Version: 2.4.4
Release: 1
License: GPL
Group: Applications/File
URL: http://kdirstat.sourceforge.net/

Source: http://kdirstat.sourceforge.net/download/kdirstat-%{version}.tar.bz2
Patch: gcc34-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, libpng-devel
BuildRequires: libart_lgpl-devel, arts-devel
BuildRequires: gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel
BuildRequires: libjpeg-devel, kdelibs-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}
Requires: kdelibs, qt


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
%patch -p1

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall
%find_lang %{name}
mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}/usr/share/applnk/Utilities/kdirstat.desktop %{buildroot}/usr/share/applications/kdirstat.desktop
echo "Categories=Application;System;X-Red-Hat-Extra" >> %{buildroot}/usr/share/applications/kdirstat.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING COPYING.LIB CREDITS INSTALL README TODO
%{_bindir}/kdirstat
%{_datadir}/applications/kdirstat.desktop
%{_datadir}/apps/kdirstat
%{_datadir}/doc/HTML/en/kdirstat
%{_datadir}/icons/*/*/apps/kdirstat.png
%{_datadir}/*/*/actions/symlink.png

%changelog
* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.4-1
- Updated to release 2.4.4.

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 2.4.0-3
- spec cleanup

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-2
- added some BuildRequires and Requires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-1
- first packaging for Fedora Core 1
