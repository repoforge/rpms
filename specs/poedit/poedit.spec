# $Id$
# Authority: dries
# Screenshot: http://poedit.sourceforge.net/screenshots/poEditUnicode_s.png
# ScreenshotURL: http://poedit.sourceforge.net/screenshots.php

Summary: PoEdit is a cross-platform gettext catalogs (.po files) editor
Name: poedit
Version: 1.4.2
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://poedit.sourceforge.net/

Source: http://dl.sf.net/poedit/poedit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, gcc-c++, wxGTK-devel >= 2.6, db4-devel, gettext, zip
Requires: wxGTK, db4, gettext

%description
poEdit is a cross-platform gettext catalogs (.po files) editor. It is built
with wxWindows.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install-strip DESTDIR="%{buildroot}"
%find_lang %{name}
#mkdir -p %{buildroot}%{_datadir}/applications
#cat > %{buildroot}%{_datadir}/applications/poedit.desktop <<EOF
#[Desktop Entry]
#Version=1.0
#Type=Application
#Encoding=UTF-8
#Name=PoEdit
#Exec=/usr/bin/poedit
#Categories=Application;Development;X-Red-Hat-Extra;
#EOF

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/poedit*
%{_bindir}/poedit
%{_datadir}/applications/poedit.desktop
%{_datadir}/icons/hicolor/*/apps/poedit.png
%{_datadir}/icons/hicolor/scalable/apps/poedit.svg*
%{_datadir}/pixmaps/poedit.png
%{_datadir}/poedit/

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Updated to release 1.4.2.

* Fri Apr 11 2008 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Tue Dec 11 2007 Dag Wieers <dag@wieers.com> - 1.3.8-1
- Updated to release 1.3.8.

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 1.3.7-1
- Updated to release 1.3.7.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.5-1
- Updated to release 1.3.5.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.4-1
- Updated to release 1.3.4.

* Mon Jun 27 2005 Dries Verachtert <dries@ulyssis.org> 1.3.3-1
- Update to release 1.3.3.

* Sat Jan 29 2005 Dries Verachtert <dries@ulyssis.org> 1.3.2-1
- Update to version 1.3.2.

* Sun Sep 12 2004 Dries Verachtert <dries@ulyssis.org> 1.3.1-1
- Update to version 1.3.1.

* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.2.5-1
- update to 1.2.5

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.2.4-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.2.4-2
- added a desktop icon

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.2.4-1
- first packaging for Fedora Core 1
