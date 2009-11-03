# $Id$
# Authority: dries

# Screenshot: http://kile.sourceforge.net/images/screenshots/kile_screen.png
# ScreenshotURL: http://kile.sourceforge.net/screenshots.php

# ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: User friendly TeX/LaTeX editor
Name: kile
Version: 2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://kile.sourceforge.net/

Source: http://dl.sf.net/kile/kile-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, kdelibs-devel, gcc, make, gcc-c++
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs

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

%prep
%setup

echo "Encoding=UTF-8" >>src/kile/kile.desktop

%{__perl} -pi.orig -e '
        s|KDE Desktop Entry|Desktop Entry|g;
        s|Categories=.*|Categories=Qt;KDE;Application;Office;|g;
    ' src/kile/kile.desktop

%build
source "/etc/profile.d/qt.sh"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
%{__mv} -v %{buildroot}%{_datadir}/applications/kde/kile.desktop %{buildroot}%{_datadir}/applications/kile.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_datadir}/doc/HTML/*/kile/
%{_bindir}/kile
%{_datadir}/applications/kile.desktop
%{_datadir}/apps/kconf_update/kile.upd
%{_datadir}/apps/kconf_update/kile*_upd.pl
%{_datadir}/apps/kile/
%{_datadir}/config.kcfg/kile.kcfg
%{_datadir}/icons/*/*/apps/kile.*
%{_datadir}/mimelnk/text/x-kilepr.desktop
### Conflicts with kdelibs-3.2.2-8.FC2
%exclude %{_datadir}/apps/katepart/syntax/bibtex.xml
%exclude %{_datadir}/apps/katepart/syntax/latex.xml

%changelog
* Mon Feb 11 2008 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Updated to release 2.0.

* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 1.9.3-1
- Updated to release 1.9.3.

* Sat Jul 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.1-1
- Updated to release 1.9.1.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 1.8-1
- Update to release 1.8.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 1.7.1-1
- Update to release 1.7.1.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> 1.7-1
- Update to 1.7.
- %%find_lang removed.. it doesn't seem to work with version 1.7.
- syntax files excluded.. conflict with kdelibs

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net> 1.6.3-1
- Partial spec file cleanup, added %%find_lang.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> 1.6.3-1
- update to 1.6.3

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
