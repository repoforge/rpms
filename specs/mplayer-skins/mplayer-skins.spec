# $Id$
# Authority: matthias

%define	skindir	%{_datadir}/mplayer/Skin

Summary: Collection of skins for MPlayer
Name: mplayer-skins
Version: 1.5
Release: 1
License: GPL
Group: Applications/Multimedia
# To get the list from the files in the PWD :
# LANG=C i=0; for file in *.bz2; do
#  echo "Source${i}: http://www1.mplayerhq.hu/MPlayer/Skin/$file"; i=$(($i+1))
# done
Source0: http://www1.mplayerhq.hu/MPlayer/Skin/Abyss-1.1.tar.bz2
Source1: http://www1.mplayerhq.hu/MPlayer/Skin/AlienMind-1.2.tar.bz2
#Source2: http://www1.mplayerhq.hu/MPlayer/Skin/Blue-1.4.tar.bz2
Source3: http://www1.mplayerhq.hu/MPlayer/Skin/Blue-small-1.2.tar.bz2
Source4: http://www1.mplayerhq.hu/MPlayer/Skin/BlueHeart-1.5.tar.bz2
Source5: http://www1.mplayerhq.hu/MPlayer/Skin/Canary-1.2.tar.bz2
Source6: http://www1.mplayerhq.hu/MPlayer/Skin/Corelian-1.1.tar.bz2
Source7: http://www1.mplayerhq.hu/MPlayer/Skin/CornerMP-1.1.tar.bz2
Source8: http://www1.mplayerhq.hu/MPlayer/Skin/CornerMP-aqua-1.3.tar.bz2
Source9: http://www1.mplayerhq.hu/MPlayer/Skin/Cyrus-1.2.tar.bz2
Source10: http://www1.mplayerhq.hu/MPlayer/Skin/DVDPlayer-1.1.tar.bz2
Source11: http://www1.mplayerhq.hu/MPlayer/Skin/Dushku-1.2.tar.bz2
Source12: http://www1.mplayerhq.hu/MPlayer/Skin/Industrial-1.0.tar.bz2
Source13: http://www1.mplayerhq.hu/MPlayer/Skin/JiMPlayer-1.4.tar.bz2
Source14: http://www1.mplayerhq.hu/MPlayer/Skin/KDE-0.3.tar.bz2
Source15: http://www1.mplayerhq.hu/MPlayer/Skin/MidnightLove-1.6.tar.bz2
Source16: http://www1.mplayerhq.hu/MPlayer/Skin/OSX-Brushed-2.3.tar.bz2
Source17: http://www1.mplayerhq.hu/MPlayer/Skin/OSX-Mod-1.1.tar.bz2
Source18: http://www1.mplayerhq.hu/MPlayer/Skin/Orange-1.3.tar.bz2
Source19: http://www1.mplayerhq.hu/MPlayer/Skin/PowerPlayer-1.1.tar.bz2
Source20: http://www1.mplayerhq.hu/MPlayer/Skin/QPlayer-1.2.tar.bz2
Source21: http://www1.mplayerhq.hu/MPlayer/Skin/Terminator3-1.1.tar.bz2
Source22: http://www1.mplayerhq.hu/MPlayer/Skin/WMP6-2.2.tar.bz2
Source23: http://www1.mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6-2.0.tar.bz2
Source24: http://www1.mplayerhq.hu/MPlayer/Skin/XFce4-1.0.tar.bz2
Source25: http://www1.mplayerhq.hu/MPlayer/Skin/avifile-1.6.tar.bz2
Source26: http://www1.mplayerhq.hu/MPlayer/Skin/bluecurve-1.0.tar.bz2
Source27: http://www1.mplayerhq.hu/MPlayer/Skin/default-1.8.tar.bz2
Source28: http://www1.mplayerhq.hu/MPlayer/Skin/disappearer-1.1.tar.bz2
Source29: http://www1.mplayerhq.hu/MPlayer/Skin/divxplayer-1.2.tar.bz2
Source30: http://www1.mplayerhq.hu/MPlayer/Skin/gnome-1.1.tar.bz2
Source31: http://www1.mplayerhq.hu/MPlayer/Skin/handheld-1.0.tar.bz2
Source32: http://www1.mplayerhq.hu/MPlayer/Skin/hayraphon-1.0.tar.bz2
Source33: http://www1.mplayerhq.hu/MPlayer/Skin/hwswskin-1.1.tar.bz2
Source34: http://www1.mplayerhq.hu/MPlayer/Skin/iTunes-1.1.tar.bz2
Source35: http://www1.mplayerhq.hu/MPlayer/Skin/iTunes-mini-1.1.tar.bz2
Source36: http://www1.mplayerhq.hu/MPlayer/Skin/krystal-1.1.tar.bz2
Source37: http://www1.mplayerhq.hu/MPlayer/Skin/mentalic-1.2.tar.bz2
Source38: http://www1.mplayerhq.hu/MPlayer/Skin/mini-0.1.tar.bz2
Source39: http://www1.mplayerhq.hu/MPlayer/Skin/moonphase-1.0.tar.bz2
Source40: http://www1.mplayerhq.hu/MPlayer/Skin/neutron-1.5.tar.bz2
Source41: http://www1.mplayerhq.hu/MPlayer/Skin/new-age-1.0.tar.bz2
Source42: http://www1.mplayerhq.hu/MPlayer/Skin/phony-1.1.tar.bz2
Source43: http://www1.mplayerhq.hu/MPlayer/Skin/plastic-1.2.tar.bz2
Source44: http://www1.mplayerhq.hu/MPlayer/Skin/proton-1.2.tar.bz2
Source45: http://www1.mplayerhq.hu/MPlayer/Skin/sessene-1.0.tar.bz2
Source46: http://www1.mplayerhq.hu/MPlayer/Skin/slim-1.2.tar.bz2
Source47: http://www1.mplayerhq.hu/MPlayer/Skin/softgrip-1.1.tar.bz2
Source48: http://www1.mplayerhq.hu/MPlayer/Skin/trium-1.3.tar.bz2
Source49: http://www1.mplayerhq.hu/MPlayer/Skin/tvisor-1.1.tar.bz2
Source50: http://www1.mplayerhq.hu/MPlayer/Skin/ultrafina-1.1.tar.bz2
Source51: http://www1.mplayerhq.hu/MPlayer/Skin/xanim-1.6.tar.bz2
Source52: http://www1.mplayerhq.hu/MPlayer/Skin/xine-lcd-1.2.tar.bz2
Source53: http://www1.mplayerhq.hu/MPlayer/Skin/xmmplayer-1.1.tar.bz2
URL: http://mplayerhq.hu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer >= 1.0
BuildArch: noarch


%description
This package contains a collection of additional skins for the GUI version
of MPlayer, the movie player for Linux. Install this package if you wish to
change the appeareance of MPlayer.


%prep
%setup -c %{name}-%{version} -a0 -a1  -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51 -a52 -a53


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{skindir}
# As the default is now "Blue", move the old "default" to "classic"
%{__mv} default classic
%{__cp} -a * %{buildroot}%{skindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{skindir}/*


%changelog
* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 1.5-1
- Updated JiMPlayer and WMP6.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net/> 1.4-1
- Update all existing skins and add all new available ones.
- Remove mplayer_red, it's 1.3MB alone!

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3
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

