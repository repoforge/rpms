# $Id$
# Authority: dries
# Upstream: <tom.drexl@gmx.de>

# Screenshot: http://home.t-online.de/home/Primetime./gl-117/sshot2_092_700.jpg
# ScreenshotURL: http://home.t-online.de/home/Primetime./gl-117/gallery.htm

%{?dist: %{expand: %%define %dist 1}}

Summary: Action flight simulator
Name: gl-117
Version: 1.2
Release: 1
License: GPL
Group: Amusements/Games
URL: http://home.t-online.de/home/Primetime./gl-117/gl-117.html

Source: http://dl.sf.net/gl-117/gl-117-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_mixer-devel
%{!?dist:BuildRequires: freeglut-devel, xorg-x11-devel}
%{?fc2:BuildRequires: freeglut-devel, xorg-x11-devel}
%{?fc1:BuildRequires: freeglut-devel, XFree86-devel}
%{?rh9:BuildRequires: glut-devel, XFree86-devel}

%description
GL-117 is an action flight simulator. Enter the Eagle Squadron and succeed 
in several challanging missions leading though different landscapes. Five 
predefined levels of video quality and an amount of viewing ranges let you 
perfectly adjust the game to the performance of your system.

%prep
%setup -n %{name}-%{version}-src

%build
export LDFLAGS=" -lXmu -lXi -lSDL -lSDL_mixer "
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ INSTALL NEWS README
%{_bindir}/gl-117
%{_datadir}/gl-117/

%changelog
* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Cosmetic cleanup.

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- update to 1.2

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.1-1
- first packaging for Fedora Core 1
