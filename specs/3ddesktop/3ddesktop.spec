# $Id$

# Authority: dries
# Upstream: 

Summary: OpenGL program for switching virtual desktops in 3D
Name: 3ddesktop
Version: 0.2.5
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://desk3d.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/desk3d/3ddesktop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: imlib2-devel, XFree86-devel, gcc-c++
Requires: imlib2

# Screenshot: http://desk3d.sourceforge.net/images/seq1-thumb.gif
# screenshotURL: http://desk3d.sourceforge.net/screenshots.php

%description
3D-Desktop is an OpenGL program for switching virtual desktops in a seamless
3-dimensional manner on Linux. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available.

%prep
%setup

%build
%{__rm} -rf %{buildroot}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS COPYING INSTALL NEWS README.windowmanagers TODO
%config(noreplace) %{_sysconfdir}/3ddesktop.conf
%{_bindir}/3ddesk
%{_bindir}/3ddeskd
%{_datadir}/3ddesktop/digits.bmp

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.2.5-2
- update of spec file

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.2.5-1
- first packaging for Fedora Core 1
