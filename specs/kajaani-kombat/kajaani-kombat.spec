# $Id$
# Authority: dries

# Screenshot: http://kombat.kajaani.net/ss/07.png
# ScreenshotURL: http://kombat.kajaani.net/screens.php

Summary: Multiplayer game in space
Name: kajaani-kombat
Version: 0.7
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://kombat.kajaani.net/

Source: http://kombat.kajaani.net/dl/kajaani-kombat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, SDL-devel, SDL_ttf-devel, SDL_net-devel
BuildRequires: SDL_image-devel, SDL_mixer-devel
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
%{__perl} -pi -e 's|MEDIA_PATH=\\"\./\\"|MEDIA_PATH=\\"/usr/share/games/kajaanikombat/\\"|g;' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 kajaani-kombat %{buildroot}%{_bindir}/kajaani-kombat
%{__install} -Dp -m0644 kajaani-kombat.6 %{buildroot}%{_mandir}/man6/kajaani-kombat.6

%{__install} -d -m0755 %{buildroot}/%{_datadir}/games/kajaanikombat
%{__install} -p -m0644 *.ogg *.png *.ttf %{buildroot}%{_datadir}/games/kajaanikombat/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man6/kajaani-kombat.6*
%{_bindir}/kajaani-kombat
%{_datadir}/games/kajaanikombat/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1.2
- Rebuild for Fedora Core 5.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> 0.7-1
- Updated to release 0.7.

* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> 0.6-1
- Updated to release 0.6.
- Removed the patch (is applied upstream).

* Tue Jan 04 2005 Dries Verachtert <dries@ulyssis.org> 0.5-2
- Some fixes: gcc 3.4 patch and also include the ogg files.

* Sat Oct 30 2004 Dries Verachtert <dries@ulyssis.org> 0.5-1
-  Update to release 0.5.

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.4-1
- Renamed from kajaani_kombat to kajaani-kombat to match upstream.

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 0.4-1
- update to 0.4

* Fri Feb 27 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1
