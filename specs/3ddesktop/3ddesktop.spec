# $Id$
# Authority: dries
# Upstream: Brad Wasson <bard$systemtoolbox,com>

# Screenshot: http://desk3d.sourceforge.net/images/seq1-thumb.gif
# ScreenshotURL: http://desk3d.sourceforge.net/screenshots.php

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
# %{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: OpenGL program for switching virtual desktops in 3D
Name: 3ddesktop
Version: 0.2.7
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://desk3d.sourceforge.net/

Source: http://dl.sf.net/desk3d/3ddesktop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, XFree86-devel, zlib-devel
BuildRequires: imlib2-devel, qt-devel, kdelibs-devel
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGL, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU, xorg-x11-Mesa-libGL}
%{?el2:BuildRequires: Mesa-devel}
Requires: imlib2

%description
3D-Desktop is an OpenGL program for switching virtual desktops in a seamless
3-dimensional manner on Linux. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README* TODO
%config(noreplace) %{_sysconfdir}/3ddesktop.conf
%{_bindir}/3ddesk
%{_bindir}/3ddeskd
%{_datadir}/3ddesktop/

%changelog
* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> 0.2.7-1
- Update to release 0.2.7.

* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> 0.2.6-1
- update to 0.2.6

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 0.2.5-3
- buildreqs update

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.2.5-2
- update of spec file

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.2.5-1
- first packaging for Fedora Core 1
