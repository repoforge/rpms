# $Id: $

# Authority: dries

Summary: Free easy-to-use paint program
Name: kolourpaint
Version: 1.0.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kolourpaint.sourceforge.net/


Source: http://dl.sf.net/kolourpaint/kolourpaint-%{version}.tar.bz2
# Patch: brush_1x1_kolourpaint-1.0.1.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel

# Screenshot: http://kolourpaint.sourceforge.net/screenshot0_big.png
# ScrenshotURL: http://kolourpaint.sourceforge.net/screenshots.html

%description
KolourPaint is a free, easy-to-use paint program for KDE. It aims to be
conceptually simply to understand; providing a level of functionality
targeted towards the average user. It's designed for daily tasks like:

* Painting - drawing diagrams and "finger painting" 
* Image Manipulation - editing screenshots and photos; applying effects 
* Icon Editing - drawing clipart and logos with transparency 

%prep
%setup
# patch -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
mv %{buildroot}/usr/share/applications/kde/kolourpaint.desktop %{buildroot}/usr/share/applications/kolourpaint.desktop
sed -i 's/Categories=.*/Categories=Application;Graphics;X-Red-Hat-Extra;/g;' %{buildroot}/usr/share/applications/kolourpaint.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO BUGS
%{_bindir}/kolourpaint
%{_datadir}/applications/kolourpaint.desktop
%{_datadir}/apps/kolourpaint
%{_datadir}/icons/hicolor/*/apps/kolourpaint.png

%changelog
* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 1.0.2-1
- update to 1.0.2

* Sun Apr 18 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-2
- spec file changes

* Fri Mar 19 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-1
- first packaging for Fedora Core 1
