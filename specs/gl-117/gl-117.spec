# $Id$

# Authority: dries
# Screenshot: http://home.t-online.de/home/Primetime./gl-117/sshot2_092_700.jpg
# ScreenshotURL: http://home.t-online.de/home/Primetime./gl-117/gallery.htm

Summary: Action flight simulator
Name: gl-117
Version: 1.2
Release: 1
License: GPL
Group: Amusements/Games
URL: http://home.t-online.de/home/Primetime./gl-117/gl-117.html

Source: http://dl.sf.net/gl-117/gl-117-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, glut-devel, glut, SDL-devel, SDL_mixer-devel, XFree86-devel, gcc-c++
Requires: glut

%description
GL-117 is an action flight simulator. Enter the Eagle Squadron and succeed 
in several challanging missions leading though different landscapes. Five 
predefined levels of video quality and an amount of viewing ranges let you 
perfectly adjust the game to the performance of your system.

%prep
%setup -n gl-117-1.1-src

%build
export LDFLAGS=" -lXmu -lXi -lSDL -lSDL_mixer "
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install-strip \
	DESTDIR="%{buildroot}"

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING FAQ INSTALL NEWS
%{_bindir}/gl-117
%{_datadir}/gl-117

%changelog
* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- update to 1.2

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.1-1
- first packaging for Fedora Core 1
