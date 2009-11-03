# $Id$
# Authority: dries
# Upstream:
# Screenshot: http://kdirstat.sourceforge.net/thumbnails/kdirstat-main.jpg
# ScreenshotURL: http://kdirstat.sourceforge.net/kdirstat.html#screen_shots


Summary: Graphical disk usage utility
Name: kdirstat
Version: 2.5.2
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://kdirstat.sourceforge.net/

Source: http://kdirstat.sourceforge.net/download/kdirstat-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, libpng-devel
BuildRequires: gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel
BuildRequires: libjpeg-devel, kdelibs-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
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

%build
. /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
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
%doc AUTHORS COPYING* CREDITS INSTALL README TODO
%{_bindir}/kdirstat
%{_bindir}/kdirstat-cache-writer
%{_datadir}/apps/kconf_update/fix_move_to_trash_bin.pl
%{_datadir}/apps/kconf_update/kdirstat.upd
%{_datadir}/applications/kdirstat.desktop
%{_datadir}/apps/kdirstat/
%{_datadir}/doc/HTML/en/kdirstat/
%{_datadir}/icons/*/*/apps/kdirstat.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.2-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.2-1
- Updated to release 2.5.2.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.4-1
- Updated to release 2.4.4.

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 2.4.0-3
- spec cleanup

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-2
- added some BuildRequires and Requires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 2.4.0-1
- first packaging for Fedora Core 1
