# $Id$

# Authority: dries

Summary: OpenGL program for switching virtual desktops in 3D.
Name: 3ddesktop
Version: 0.2.5
Release: 2
License: GPL
Group: Applications/Desktop
URL: http://desk3d.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/desk3d/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: imlib2-devel, XFree86-devel
Requires: imlib2

#(d) primscreenshot: http://desk3d.sourceforge.net/images/seq1-thumb.gif
#(d) screenshotsurl: http://desk3d.sourceforge.net/screenshots.php

%description
3D-Desktop is an OpenGL program for switching virtual desktops in a seamless
3-dimensional manner on Linux. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS COPYING INSTALL NEWS README.windowmanagers TODO
%config(noreplace) %{_sysconfdir}/3ddesktop.conf
%{_bindir}/3ddesk
%{_bindir}/3ddeskd
/usr/share/3ddesktop/digits.bmp


%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.2.5-2
- update of spec file

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.2.5-1
- first packaging for Fedora Core 1
