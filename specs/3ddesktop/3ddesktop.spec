# $Id$
# Authority: dries
# Upstream: Brad Wasson <bard$systemtoolbox,com>

# Screenshot: http://desk3d.sourceforge.net/images/seq1-thumb.gif
# ScreenshotURL: http://desk3d.sourceforge.net/screenshots.php


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: OpenGL program for switching virtual desktops in 3D
Name: 3ddesktop
Version: 0.2.9
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://desk3d.sourceforge.net/

Source: http://dl.sf.net/desk3d/3ddesktop-%{version}.tar.gz
Patch: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.58, gcc-c++, zlib-devel
BuildRequires: imlib2-devel, qt-devel, kdelibs-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXt-devel, libXext-devel, libICE-devel, libXxf86vm-devel, libXmu-devel, libXi-devel}
%{?el2:BuildRequires: Mesa-devel}
Requires: imlib2

%description
3D-Desktop is an OpenGL program for switching virtual desktops in a seamless
3-dimensional manner on Linux. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available.

%prep
%setup
%patch -p1

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README* TODO
%doc %{_mandir}/man1/3ddesk.1*
%doc %{_mandir}/man1/3ddeskd.1*
%config(noreplace) %{_sysconfdir}/3ddesktop.conf
%{_bindir}/3ddesk
%{_bindir}/3ddeskd
%{_datadir}/3ddesktop/

%changelog
* Sat Mar 10 2007 Dag Wieers <dag@wieers.com> - 0.2.9-1
- Updated to release 0.2.9.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 0.2.8-1
- Updated to release 0.2.8.

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1
- UpdatedA to release 0.2.7.

* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- update to 0.2.6

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> - 0.2.5-3
- buildreqs update

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.2.5-2
- update of spec file

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> - 0.2.5-1
- first packaging for Fedora Core 1
