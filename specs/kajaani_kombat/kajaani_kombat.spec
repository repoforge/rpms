# $Id$
# Authority: dries

# Screenshot: http://kombat.kajaani.net/ss/07.png
# ScreenshotURL: http://kombat.kajaani.net/screens.php

Summary: Multiplayer game in space
Name: kajaani-kombat
Version: 0.4
Release: 1
License: GPL
Group: Amusements/Games
URL: http://kombat.kajaani.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://kombat.kajaani.net/dl/kajaani-kombat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, SDL-devel, SDL_ttf-devel, SDL_net-devel, SDL_image-devel
Obsoletes: kajaani_kombat <= 0.4

%description
Kajaani Kombat is a funny multiplayer game... and much more! It is a
rampart-like game (old arcade classic) set in space.

Kajaani Kombat is playable with two to four players, over the internet or
alternatively two players sharing one computer. It is also possible to play
over the internet with, for example, 4 players of which two are sharing the
same computer. Enjoy it with your friends! 

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -m 0755 -d %{buildroot}/%{_bindir}
%{__install} -m 0755 -d %{buildroot}/%{_datadir}/games/kajaanikombat
%{__install} -m 0755 -d %{buildroot}/%{_mandir}/man6
%{__install} -m 0755 kajaani-kombat %{buildroot}/%{_bindir}/kajaani-kombat
%{__install} -m 0644 *.png %{buildroot}/%{_datadir}/games/kajaanikombat/
%{__install} -m 0644 *.ttf %{buildroot}/%{_datadir}/games/kajaanikombat/
%{__install} -m 0644 kajaani-kombat.6 %{buildroot}/%{_mandir}/man6/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/kajaani-kombat
%{_datadir}/games/kajaanikombat
%{_mandir}/man6/*

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.4-1
- Renamed from kajaani_kombat to kajaani-kombat to match upstream.

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 0.4-1
- update to 0.4

* Fri Feb 27 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1

