# $Id$

# Authority: dries

Summary: Steer a marble ball through a labyrinth.
Name: trackballs
Version: 1.0.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://trackballs.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://heanet.dl.sourceforge.net/sourceforge/trackballs/trackballs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: guile, guile-devel, SDL

#(d) primscreenshot: http://trackballs.sourceforge.net/pic1.jpg

%description
Trackballs is a game for linux in which you steer a marble ball through
tracks of varying difficulty. The game is loosely based on Marable Madness
and features 3D graphics, an integerated level editor and highquality
soundeffects and background music. 
You can find online documentation at
http://trackballs.sourceforge.net/documentation.html

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup
# the install script does a chgrp to 'games', this doesn't work while 
# building as a user. Is group=games required?
sed -i "s/chgrp/#chgrp/g;" share/Makefile*
%configure

%build
%{__make} %{?_smp_mflags}

%install
%makeinstall
%{__strip} %{buildroot}/%{_bindir}/trackballs

%files
%defattr(-,root,root, 0755)
%{_bindir}/trackballs
/usr/share/man/man6/trackballs.6.gz
%{_datadir}/trackballs/fonts/menuFont.ttf
%{_datadir}/trackballs/highScores
%{_datadir}/trackballs/images
%{_datadir}/trackballs/levels
%{_datadir}/trackballs/sfx

%changelog
* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1
