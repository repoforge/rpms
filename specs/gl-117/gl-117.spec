# $Id$

# Authority: dries
# Screenshot: http://home.t-online.de/home/Primetime./gl-117/sshot2_092_700.jpg
# ScreenshotURL: http://home.t-online.de/home/Primetime./gl-117/gallery.htm

# NeedsCleanup

Summary: Action flight simulator
Summary(nl): een actie flight simulator
Name: gl-117
Version: 1.1
Release: 1.dries
License: GPL
Group: Amusements/Games
URL: http://home.t-online.de/home/Primetime./gl-117/gl-117.html

Source: http://dl.sf.net/gl-117/gl-117-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, glut-devel, glut
Requires: glut

%description
GL-117 is an action flight simulator. Enter the Eagle Squadron and succeed 
in several challanging missions leading though different landscapes. Five 
predefined levels of video quality and an amount of viewing ranges let you 
perfectly adjust the game to the performance of your system.

%description -l nl
GL-117 is een actie flight simulator. Ga bij het Eagle Squadron en doe mee
aan verschillende uitdagende missies in verschillende landschappen. Vijf
voorgedefinieerde niveaus van video kwaliteit laten u toe om het spel
perfect aan te passen aan de performantie van uw systeem.

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
%defattr(-,root,root)
%doc README AUTHORS COPYING FAQ INSTALL NEWS
/usr/bin/gl-117
/usr/share/gl-117

%changelog
* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.1-1.dries
- first packaging for Fedora Core 1
