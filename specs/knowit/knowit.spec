# $Id$
# Authority: dries

# Screenshot: http://knowit.sourceforge.net/images/knowit.png
# ScreenshotURL: http://knowit.sourceforge.net/screenshots.html

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Tool for managing notes
Name: knowit
Version: 0.10
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://knowit.sourceforge.net/

Source: http://knowit.sourceforge.net/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
KnowIt is a tool for managing notes. Notes are organized in a tree-like
hierarchy.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/knowit
%{_datadir}/applnk/Applications/knowit.desktop
%{_datadir}/apps/knowit/
%{_datadir}/doc/HTML/en/knowit/
%{_datadir}/icons/hicolor/*/apps/knowit.png

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.10-1
- Spec file cleanup, use %%find_lang.
- Fix orphaned directories.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1
- update to 0.10

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.9-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.9-1
- first packaging for Fedora Core 1
