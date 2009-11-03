# $Id$

# Authority: dries
# Screenshot: http://kolourpaint.sourceforge.net/screenshot0_big.png
# ScrenshotURL: http://kolourpaint.sourceforge.net/screenshots.html
# Upstream: Clarence Dang <dang$kde,org>


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

%define real_version 1.2.2_kde3

Summary: Free easy-to-use paint program
Name: kolourpaint
Version: 1.2.2
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kolourpaint.sourceforge.net/

Source: http://dl.sf.net/kolourpaint/kolourpaint-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
KolourPaint is a free, easy-to-use paint program for KDE. It aims to be
conceptually simply to understand; providing a level of functionality
targeted towards the average user. It's designed for daily tasks like:

* Painting - drawing diagrams and "finger painting"
* Image Manipulation - editing screenshots and photos; applying effects
* Icon Editing - drawing clipart and logos with transparency

%prep
%setup -n kolourpaint-%{real_version}

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%{__mv} %{buildroot}/usr/share/applications/kde/kolourpaint.desktop %{buildroot}/usr/share/applications/kolourpaint.desktop
%{__sed} -i 's/Categories=.*/Categories=Application;Graphics;X-Red-Hat-Extra;/g;' %{buildroot}/usr/share/applications/kolourpaint.desktop
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING README
%{_bindir}/kolourpaint
%{_datadir}/applications/kolourpaint.desktop
%{_datadir}/apps/kolourpaint
%{_datadir}/icons/hicolor/*/apps/kolourpaint.png
%{_datadir}/icons/crystalsvg/*/apps/kolourpaint.png
%{_datadir}/doc/HTML/en/kolourpaint

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.2-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> 1.2.2-1
- Update to version 1.2.2.

* Tue Aug 17 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- Update to version 1.2.

* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 1.0.2-1
- update to 1.0.2

* Sun Apr 18 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-2
- spec file changes

* Fri Mar 19 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- first packaging for Fedora Core 1
