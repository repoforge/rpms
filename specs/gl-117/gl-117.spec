# $Id: gl-117.spec,v 1.1 2004/03/01 15:41:09 driesve Exp $

# Authority: dries

# NeedsCleanup

%define _name		gl-117
%define _version	1.1
%define _release	1.dries

Summary: an action flight simulator
Summary(nl): een actie flight simulator

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Amusements/Games
URL: http://home.t-online.de/home/Primetime./gl-117/gl-117.html
Source: http://dl.sf.net/gl-117/gl-117-1.1-src.tar.gz
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

#(d) primscreenshot: http://home.t-online.de/home/Primetime./gl-117/sshot2_092_700.jpg
#(d) screenshotsurl: http://home.t-online.de/home/Primetime./gl-117/gallery.htm

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n gl-117-1.1-src

%build
export LDFLAGS=" -lXmu -lXi -lSDL -lSDL_mixer "
%configure
make

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
make install-strip

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING FAQ INSTALL NEWS
/usr/bin/gl-117
/usr/share/gl-117

%changelog
* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.1-1.dries
- first packaging for Fedora Core 1
