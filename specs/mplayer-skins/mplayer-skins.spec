# $Id$
# Authority: matthias

%define	skindir	%{_datadir}/mplayer/Skin

Summary: A collection of skins for MPlayer
Name: mplayer-skins
Version: 1.3
Release: 3
License: GPL
Group: Applications/Multimedia
Source0: http://www.mplayerhq.hu/MPlayer/Skin/AlienMind-1.1.tar.bz2
#Source1: http://www.mplayerhq.hu/MPlayer/Skin/Blue-1.0.tar.bz2
Source2: http://www.mplayerhq.hu/MPlayer/Skin/Blue-small-1.0.tar.bz2
Source3: http://www.mplayerhq.hu/MPlayer/Skin/BlueHeart-1.4.tar.bz2
Source4: http://www.mplayerhq.hu/MPlayer/Skin/Canary-1.1.tar.bz2
Source5: http://www.mplayerhq.hu/MPlayer/Skin/Corelian-1.0.tar.bz2
Source6: http://www.mplayerhq.hu/MPlayer/Skin/CornerMP-1.0.tar.bz2
Source7: http://www.mplayerhq.hu/MPlayer/Skin/CornerMP-aqua-1.0.tar.bz2
Source8: http://www.mplayerhq.hu/MPlayer/Skin/Cyrus-1.0.tar.bz2
Source9: http://www.mplayerhq.hu/MPlayer/Skin/Dushku-1.1.tar.bz2
Source10: http://www.mplayerhq.hu/MPlayer/Skin/JiMPlayer-1.1.tar.bz2
Source11: http://www.mplayerhq.hu/MPlayer/Skin/MidnightLove-1.5.tar.bz2
Source12: http://www.mplayerhq.hu/MPlayer/Skin/OSX-Brushed-2.2.tar.bz2
Source13: http://www.mplayerhq.hu/MPlayer/Skin/OSX-Mod-1.0.tar.bz2
Source14: http://www.mplayerhq.hu/MPlayer/Skin/Orange-1.1.tar.bz2
Source15: http://www.mplayerhq.hu/MPlayer/Skin/QPlayer-1.0.3.tar.bz2
Source16: http://www.mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6-1.2.tar.bz2
Source17: http://www.mplayerhq.hu/MPlayer/Skin/avifile-1.5.tar.bz2
Source18: http://www.mplayerhq.hu/MPlayer/Skin/default-1.7.tar.bz2
Source19: http://www.mplayerhq.hu/MPlayer/Skin/disappearer-1.1.tar.bz2
Source20: http://www.mplayerhq.hu/MPlayer/Skin/gnome-1.1.tar.bz2
Source21: http://www.mplayerhq.hu/MPlayer/Skin/handheld-1.0.tar.bz2
Source22: http://www.mplayerhq.hu/MPlayer/Skin/hayraphon-1.0.tar.bz2
Source23: http://www.mplayerhq.hu/MPlayer/Skin/hwswskin-1.0.tar.bz2
Source24: http://www.mplayerhq.hu/MPlayer/Skin/iTunes-1.0.tar.bz2
Source25: http://www.mplayerhq.hu/MPlayer/Skin/iTunes-mini-1.1.tar.bz2
Source26: http://www.mplayerhq.hu/MPlayer/Skin/krystal-1.0.tar.bz2
Source27: http://www.mplayerhq.hu/MPlayer/Skin/mentalic-1.1.tar.bz2
Source28: http://www.mplayerhq.hu/MPlayer/Skin/mplayer_red-1.0.tar.bz2
Source29: http://www.mplayerhq.hu/MPlayer/Skin/neutron-1.4.tar.bz2
Source30: http://www.mplayerhq.hu/MPlayer/Skin/phony-1.0.tar.bz2
Source31: http://www.mplayerhq.hu/MPlayer/Skin/plastic-1.1.1.tar.bz2
Source32: http://www.mplayerhq.hu/MPlayer/Skin/proton-1.1.tar.bz2
Source33: http://www.mplayerhq.hu/MPlayer/Skin/sessene-1.0.tar.bz2
Source34: http://www.mplayerhq.hu/MPlayer/Skin/slim-1.0.tar.bz2
Source35: http://www.mplayerhq.hu/MPlayer/Skin/softgrip-1.0.tar.bz2
Source36: http://www.mplayerhq.hu/MPlayer/Skin/trium-1.1.tar.bz2
Source37: http://www.mplayerhq.hu/MPlayer/Skin/xanim-1.5.tar.bz2
Source38: http://www.mplayerhq.hu/MPlayer/Skin/xine-lcd-1.0.tar.bz2
Source39: http://www.mplayerhq.hu/MPlayer/Skin/xmmplayer-1.0.tar.bz2
URL: http://mplayerhq.hu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer >= 0.90
BuildArch: noarch

%description
This package contains a collection of additional skins for the GUI version
of MPlayer, the movie player for Linux. Install this package if you wish to
change the appeareance of MPlayer.

%prep
%setup -c %{name}-%{version} -a0  -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{skindir}
# As the default is now "Blue", move the old "default" to "classic"
mv default classic
cp -a * %{buildroot}%{skindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%{skindir}/*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3.fr
- Rebuild for Fedora Core 1.

* Thu Aug 14 2003 Matthias Saou <http://freshrpms.net/>
- Added Corelian, Dushku, JiMPlayer, OSX-Brushed, handheld.
- Added also iTunes, iTunes-mini, sessene.
- Updated the already included skins that have a new version available.

* Tue Apr  8 2003 Matthias Saou <http://freshrpms.net/>
- Updated package with all updated and new skins from the final 0.90.
- Renamed default to classic now that Blue is the new default.
- Removed mplayerred, as its _huge_ and buggy (needs updating I guess).

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Major update of all themes as found on the MPlayer webpage.
- Added sanity check for modes as many files are o-r :-(

* Wed Jan 15 2003 Matthias Saou <http://freshrpms.net/>
- Fixed version dependency... no, really, I mean it this time :-/
- Added MPlayer Red theme I came across on freshmeat.

* Fri Dec 13 2002 Matthias Saou <http://freshrpms.net/>
- Fixed version dependency...

* Thu Sep  5 2002 Matthias Saou <http://freshrpms.net/>
- Added trium and gnome themes.

* Tue Aug  6 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

