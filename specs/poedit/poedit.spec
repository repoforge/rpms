# $Id: poedit.spec,v 1.3 2004/03/01 09:33:38 driesve Exp $

# Authority: dries

Summary: PoEdit is a cross-platform gettext catalogs (.po files) editor.
Summary(nl): PoEdit is een cross-platform gettext catalogs (.po bestanden) editor.
Name: poedit
Version: 1.2.5
Release: 1
License: GPL
Group: Development/Tools
URL: http://poedit.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/poedit/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gcc, wxGTK-devel, db4-devel, gettext
Requires: wxGTK, db4, gettext

#(d) primscreenshot: http://poedit.sourceforge.net/screenshots/poEditUnicode_s.png
#(d) screenshotsurl: http://poedit.sourceforge.net/screenshots.php

%description
poEdit is a cross-platform gettext catalogs (.po files) editor. It is built
with wxWindows.

%description -l nl
PoEdit is een cross-platform gettext catalogs (.po bestanden) editor. Het is
gemaakt met wxWindows.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/poedit.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=PoEdit
Exec=/usr/bin/poedit
Categories=Application;Development;X-Red-Hat-Extra;
EOF

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/poedit
/usr/share/locale/*/LC_MESSAGES/poedit.mo
/usr/share/man/man1/poedit.1.gz
/usr/share/poedit
/usr/share/applications/poedit.desktop

%changelog
* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.2.5-1
- update to 1.2.5

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.2.4-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.2.4-2
- added a desktop icon

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.2.4-1
- first packaging for Fedora Core 1
