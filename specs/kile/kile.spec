# $Id$

# Authority: dries

Summary: user friendly TeX/LaTeX editor
Name: kile
Version: 1.6.2
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://kile.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kile/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

# Screenshot: http://kile.sourceforge.net/images/screenshots/kile_screen.png
# ScreenshotURL: http://kile.sourceforge.net/screenshots.php

%description
Kile is a user friendly TeX/LaTeX editor. The main features are:
* Compile, convert and view your document with one click.
* Templates and wizards makes starting a new document very little work.
* Easy insertion of many standard tags and symbols and the option 
to define (an arbitrary number of) user defined tags
* Inverse and forward search: click in the DVI viewer and jump to the
corresponding LaTeX line in the editor, or jump from the editor to the
corresponding page in the viewer.
* Finding chapter or sections is very easy, Kile constructs a list of all
the chapter etc. in your document. You can use the list to jump to the
corresponding section.

%description -l nl
Kile is een gebruiksvriendelijke TeX/LaTeX editor met ondersteuning voor:
* Het compileren, transformeren en bekijken van uw document met 1 klik.
* Een nieuw document starten is eenvoudig met templates en wizards.
* U kan eenvoudig vele standaard tags en symbolen toevoegen en ook uw eigen 
tags toevoegen.
* Zoeken: klikken in de DVI viewer opent de overeenkomstige LaTeX lijn in
de editor en andersom.
* Het vinden van hoofdstukken en secties is eenvoudig: Kile maakt een lijst
van alle hoofdstukken en dergelijke.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip
echo "Encoding=UTF-8" >> $DESTDIR/usr/share/applications/kde/kile.desktop
sed -i "s/KDE Desktop Entry/Desktop Entry/g;" $DESTDIR/usr/share/applications/kde/kile.desktop
sed -i "s/Categories=.*/Categories=Qt;KDE;Application;Office;X-Red-Hat-Extra;/g;" $DESTDIR/usr/share/applications/kde/kile.desktop
mv $DESTDIR/usr/share/applications/kde/kile.desktop $DESTDIR/usr/share/applications/kile.desktop

%files
%defattr(-,root,root,0755)
%doc README
%{_datadir}/doc/HTML/*/kile
%{_datadir}/apps/kile
%{_datadir}/apps/katepart/syntax/latex-kile.xml
%{_datadir}/apps/katepart/syntax/bibtex-kile.xml
%{_datadir}/icons/crystalsvg/48x48/apps/kile.png
%{_datadir}/icons/crystalsvg/16x16/apps/kile.png
%{_datadir}/icons/crystalsvg/22x22/apps/kile.png
%{_datadir}/icons/crystalsvg/32x32/apps/kile.png
%{_datadir}/applications/kile.desktop
%{_datadir}/locale/*/LC_MESSAGES/kile.mo
%{_datadir}/mimelnk/text/x-kilepr.desktop
%{_bindir}/kile


%changelog
* Sun Apr 18 2004 Dries Verachtert <dries@ulyssis.org> 1.6.2-1
- update to 1.6.2

* Sun Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- update to 1.6.1

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.6-4
- make install changed to make install-strip

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.6-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.6-2
- cleanup and completion of spec file

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 1.6-1
- first packaging for Fedora Core 1

