# $Id$
# Authority: dries
# Screenshot: http://uml.sourceforge.net/images/thumbnails/activity-diagram.png
# ScreenshotURL: http://uml.sourceforge.net/screen.php

# ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: unified modelling language (UML) diagrams modeller
Name: umbrello
Version: 1.5.2
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://uml.sourceforge.net/

Source: http://dl.sf.net/uml/umbrello-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: qt-devel, flex

%description
Umbrello UML Modeller is a Unified Modelling Language diagram programme for
KDE. UML allows you to create diagrams of software and other systems in a
standard format.

%description -l nl
Umbrello UML Modeller is een KDE programma om Unified Modelling Language
schema's te maken. UML laat u toe om schema's te maken van software in een
standaard formaat.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%{__make} install \
	DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
%{__cat} <<EOF >%{buildroot}%{_datadir}/applications/umbrello.desktop
[Desktop Entry]
Type=Application
Exec=umbrello -caption "%c" %i %m
Icon=umbrello.png
MiniIcon=umbrello.png
DocPath=umbrello/index.html
Comment=
Terminal=false
Name=Umbrello UML Modeller
MimeType=application/x-uml
Categories=Application;Development;X-Red-Hat-Extra;
EOF
%{__rm} -f %{buildroot}%{_datadir}/applications/kde/umbrello.desktop
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/umbrello
%{_datadir}/apps/umbrello
%{_datadir}/icons/*/*/apps/umbrello.*
%{_datadir}/icons/*/*/mimetypes/umbrellofile.*
%{_datadir}/mimelnk/application/x-umbrello.desktop
%{_datadir}/applications/umbrello.desktop
%{_datadir}/icons/*/*/actions/umbrello_diagram_*.png
%{_datadir}/doc/HTML/*/umbrello

%changelog
* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.5.2-1
- Updated to release 1.5.2.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.5.1-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> 1.5.1-1
- Updated to release 1.5.1.

* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> 1.5.0-2
- Fixed the download url.

* Fri Dec 09 2005 Dries Verachtert <dries@ulyssis.org> 1.5-1
- Updated to release 1.5.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> 1.4.3-1
- Updated to release 1.4.3.

* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> 1.4.2-1
- Updated to release 1.4.2

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 1.4.1-1
- Updated to release 1.4.1

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> 1.4-1
- Updated to release 1.4.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> 1.3.1-1
- Updated to release 1.3.1.

* Tue Feb 24 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- updated to 1.2 (1.2-1 on download page)
- fixed the 'Categories=' in the desktop file
- buildrequires checked with mach
- missing links of the libcodegenerator library
  bug found by Stefan Ekman, thanks Stefan!

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-4
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-3
- added a desktop file

* Sun Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.1.1-2
- completion of spec file

* Tue Dec 02 2003 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1
