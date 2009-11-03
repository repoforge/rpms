# $Id$
# Authority: dries
# Upstream: <tom,drexl$gmx,de>

# Screenshot: http://home.t-online.de/home/Primetime./gl-117/sshot2_092_700.jpg
# ScreenshotURL: http://home.t-online.de/home/Primetime./gl-117/gallery.htm


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

%{?el3:%define _without_freeglut 1}
%{?rh9:%define _without_freeglut 1}

Summary: Action flight simulator
Name: gl-117
Version: 1.3.2
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.heptargon.de/gl-117/gl-117.html

Source: http://dl.sf.net/gl-117/gl-117-%{version}-src.tar.bz2
#Patch: gcc-fc3-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, gcc-c++
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{?_without_freeglut:BuildRequires: glut-devel}
%{!?_without_modxorg:BuildRequires: libXmu-devel, libXi-devel}

%description
GL-117 is an action flight simulator. Enter the Eagle Squadron and succeed
in several challanging missions leading though different landscapes. Five
predefined levels of video quality and an amount of viewing ranges let you
perfectly adjust the game to the performance of your system.

%prep
%setup -n %{name}-%{version}-src
#%patch -p1

%build
export LDFLAGS=" -lXmu -lXi -lSDL -lSDL_mixer "
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ INSTALL NEWS README
%{_bindir}/gl-117
%{_datadir}/gl-117/

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Update to release 1.3.2.

* Mon Jun 14 2004 Dries Verachtert <dries@ulyssis.org> 1.3-1
- update to 1.3

* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Cosmetic cleanup.

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- update to 1.2

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.1-1
- first packaging for Fedora Core 1

