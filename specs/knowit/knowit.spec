# $Id: $

# Authority: dries

Summary: Tool for managing notes
Name: knowit
Version: 0.10
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://knowit.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://knowit.sourceforge.net/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires:libselinux-devel}

# Screenshot: http://knowit.sourceforge.net/images/knowit.png
# ScreenshotURL: http://knowit.sourceforge.net/screenshots.html

%description
KnowIt is a tool for managing notes. Notes are organized in a tree-like
hierarchy.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/knowit
%{_datadir}/applnk/Applications/knowit.desktop
%{_datadir}/apps/knowit/knowitui.rc
%{_datadir}/apps/knowit/tips
%{_datadir}/doc/HTML/en/knowit/index.cache.bz2
%{_datadir}/doc/HTML/en/knowit/index.docbook
%{_datadir}/doc/HTML/en/knowit/screenshot.png
%{_datadir}/icons/hicolor/*/apps/knowit.png
%{_datadir}/locale/*/LC_MESSAGES/knowit.mo

%changelog
* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1
- update to 0.10

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.9-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.9-1
- first packaging for Fedora Core 1
