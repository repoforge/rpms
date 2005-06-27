# $Id$

# Authority: dries
# Screenshot: http://poedit.sourceforge.net/screenshots/poEditUnicode_s.png
# ScreenshotURL: http://poedit.sourceforge.net/screenshots.php

Summary: PoEdit is a cross-platform gettext catalogs (.po files) editor
Name: poedit
Version: 1.3.3
Release: 1
License: GPL
Group: Development/Tools
URL: http://poedit.sourceforge.net/

Source: http://dl.sf.net/poedit/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, gcc-c++, wxGTK-devel, db4-devel, gettext, zip
Requires: wxGTK, db4, gettext

%description
poEdit is a cross-platform gettext catalogs (.po files) editor. It is built
with wxWindows.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install-strip DESTDIR=%{buildroot}
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/poedit.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=PoEdit
Exec=/usr/bin/poedit
Categories=Application;Development;X-Red-Hat-Extra;
EOF

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/poedit
%{_mandir}/man1/poedit*
%{_datadir}/poedit
%{_datadir}/applications/poedit.desktop

%changelog
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
