# $Id$

# Authority: dries
# Screenshot: http://uml.sourceforge.net/images/thumbnails/activity-diagram.png
# ScreenshotURL: http://uml.sourceforge.net/screen.php

Summary: unified modelling language (UML) diagrams modeller
Name: umbrello
Version: 1.2
Release: 1
License: GPL
Group: Development/Tools
URL: http://uml.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/uml/%{name}-1.2-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: XFree86-devel, qt-devel, flex


%description
Umbrello UML Modeller is a Unified Modelling Language diagram programme for
KDE. UML allows you to create diagrams of software and other systems in a
standard format.

%description -l nl
Umbrello UML Modeller is een KDE programma om Unified Modelling Language
schema's te maken. UML laat u toe om schema's te maken van software in een
standaard formaat. 

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
cat > $RPM_BUILD_ROOT/usr/share/applications/umbrello.desktop <<EOF
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
rm -f $RPM_BUILD_ROOT/usr/share/applications/kde/umbrello.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING README
%{_bindir}/umbrello
/usr/share/apps/umbrello
/usr/share/icons/*/*/apps/umbrello.png
/usr/share/icons/*/*/mimetypes/umbrellofile.png
/usr/share/mimelnk/application/x-umbrello.desktop
/usr/share/applications/umbrello.desktop

%changelog
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
