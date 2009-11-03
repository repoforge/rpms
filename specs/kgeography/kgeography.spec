# $Id$

# Authority: dries
# Upstream:
# Screenshot: http://kgeography.berlios.de/screen1.png
# ScreenshotURL: http://kgeography.berlios.de/screenshots.html

# ExcludeDist: el3 fc2 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Geography learning tool
Name: kgeography
Version: 0.4
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://kgeography.berlios.de/

Source: http://download.berlios.de/kgeography/kgeography-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, gcc
BuildRequires: kdelibs-devel, make, gcc-c++
BuildRequires: qt-devel
BuildRequires: desktop-file-utils, flex
%{?fc5:BuildRequires: gcc-gfortran}
%{?fc4:BuildRequires: gcc-gfortran}
%{?fc3:BuildRequires: gcc-g77}
%{?el4:BuildRequires: gcc-g77}

%description
KGeography is a geography learning tool. Right now it has three usage modes:
* Browse the maps clicking in a map division to see it's name
* The game tells you a map division name and you have to click on it
* The game shows you a map division flag and you have to guess its name

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README TODO
%doc /usr/share/doc/HTML/en/kgeography
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/kgeography
%{_datadir}/icons/*/*/apps/kgeography.*
%{_datadir}/config.kcfg/kgeography.kcfg

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Aug 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Sun Dec 26 2004 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Tue May 4 2004 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
