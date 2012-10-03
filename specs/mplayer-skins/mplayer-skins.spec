# $Id$
# Authority: matthias
# Dist: nodist

%define skindir %{_datadir}/mplayer/skins

Summary: Collection of skins for MPlayer
Name: mplayer-skins
Version: 1.9
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
# To get the list from the files in the PWD :
# LANG=C i=0; for file in *.bz2; do
#  echo "Source${i}: http://www1.mplayerhq.hu/MPlayer/skins/$file"; i=$(($i+1))
# done
# Exclude Blue (our default in the mplayer package) and mplayer_red (1.3MB)
Source0: http://www1.mplayerhq.hu/MPlayer/skins/Abyss-1.7.tar.bz2
Source1: http://www1.mplayerhq.hu/MPlayer/skins/AlienMind-1.2.tar.bz2
Source2: http://www1.mplayerhq.hu/MPlayer/skins/Ater-1.2.tar.bz2
#Source3: http://www1.mplayerhq.hu/MPlayer/skins/Blue-1.8.tar.bz2
Source4: http://www1.mplayerhq.hu/MPlayer/skins/Blue-small-1.5.tar.bz2
Source5: http://www1.mplayerhq.hu/MPlayer/skins/BlueHeart-1.5.tar.bz2
Source6: http://www1.mplayerhq.hu/MPlayer/skins/Canary-1.2.tar.bz2
Source7: http://www1.mplayerhq.hu/MPlayer/skins/Clearlooks-1.5.tar.bz2
Source8: http://www1.mplayerhq.hu/MPlayer/skins/Corelian-1.1.tar.bz2
Source9: http://www1.mplayerhq.hu/MPlayer/skins/CornerMP-1.2.tar.bz2
Source10: http://www1.mplayerhq.hu/MPlayer/skins/CornerMP-aqua-1.4.tar.bz2
Source11: http://www1.mplayerhq.hu/MPlayer/skins/CubicPlayer-1.1.tar.bz2
Source12: http://www1.mplayerhq.hu/MPlayer/skins/Cyrus-1.2.tar.bz2
Source13: http://www1.mplayerhq.hu/MPlayer/skins/DVDPlayer-1.1.tar.bz2
Source14: http://www1.mplayerhq.hu/MPlayer/skins/Dushku-1.2.tar.bz2
Source15: http://www1.mplayerhq.hu/MPlayer/skins/ICY-1.0.tar.bz2
Source16: http://www1.mplayerhq.hu/MPlayer/skins/Industrial-1.0.tar.bz2
Source17: http://www1.mplayerhq.hu/MPlayer/skins/JiMPlayer-1.4.tar.bz2
Source18: http://www1.mplayerhq.hu/MPlayer/skins/KDE-0.3.tar.bz2
Source19: http://www1.mplayerhq.hu/MPlayer/skins/Linea-1.0.tar.bz2
Source20: http://www1.mplayerhq.hu/MPlayer/skins/MidnightLove-1.6.tar.bz2
Source21: http://www1.mplayerhq.hu/MPlayer/skins/OSX-Brushed-2.3.tar.bz2
Source22: http://www1.mplayerhq.hu/MPlayer/skins/OSX-Mod-1.1.tar.bz2
Source23: http://www1.mplayerhq.hu/MPlayer/skins/OpenDoh-1.1.tar.bz2
Source24: http://www1.mplayerhq.hu/MPlayer/skins/Orange-1.3.tar.bz2
Source25: http://www1.mplayerhq.hu/MPlayer/skins/PowerPlayer-1.1.tar.bz2
Source26: http://www1.mplayerhq.hu/MPlayer/skins/QPlayer-1.2.tar.bz2
Source27: http://www1.mplayerhq.hu/MPlayer/skins/QuickSilver-1.0.tar.bz2
Source28: http://www1.mplayerhq.hu/MPlayer/skins/Terminator3-1.1.tar.bz2
Source29: http://www1.mplayerhq.hu/MPlayer/skins/WMP6-2.2.tar.bz2
Source30: http://www1.mplayerhq.hu/MPlayer/skins/XFce4-1.0.tar.bz2
Source31: http://www1.mplayerhq.hu/MPlayer/skins/avifile-1.6.tar.bz2
Source32: http://www1.mplayerhq.hu/MPlayer/skins/bluecurve-1.3.tar.bz2
Source33: http://www1.mplayerhq.hu/MPlayer/skins/brushedGnome-1.0.tar.bz2
Source34: http://www1.mplayerhq.hu/MPlayer/skins/changuito-0.2.tar.bz2
Source35: http://www1.mplayerhq.hu/MPlayer/skins/clearplayer-0.9.tar.bz2
Source36: http://www1.mplayerhq.hu/MPlayer/skins/disappearer-1.1.tar.bz2
Source37: http://www1.mplayerhq.hu/MPlayer/skins/divxplayer-1.3.tar.bz2
Source38: http://www1.mplayerhq.hu/MPlayer/skins/gnome-1.1.tar.bz2
Source39: http://www1.mplayerhq.hu/MPlayer/skins/handheld-1.0.tar.bz2
Source40: http://www1.mplayerhq.hu/MPlayer/skins/hayraphon-1.0.tar.bz2
Source41: http://www1.mplayerhq.hu/MPlayer/skins/hwswskin-1.3.tar.bz2
Source42: http://www1.mplayerhq.hu/MPlayer/skins/iTunes-1.1.tar.bz2
Source43: http://www1.mplayerhq.hu/MPlayer/skins/iTunes-mini-1.1.tar.bz2
Source44: http://www1.mplayerhq.hu/MPlayer/skins/krystal-1.1.tar.bz2
Source45: http://www1.mplayerhq.hu/MPlayer/skins/mentalic-1.2.tar.bz2
Source46: http://www1.mplayerhq.hu/MPlayer/skins/mini-0.1.tar.bz2
Source47: http://www1.mplayerhq.hu/MPlayer/skins/moonphase-1.0.tar.bz2
#Source48: http://www1.mplayerhq.hu/MPlayer/skins/mplayer_red-1.0.tar.bz2
Source49: http://www1.mplayerhq.hu/MPlayer/skins/nativeRed-1.1.tar.bz2
Source50: http://www1.mplayerhq.hu/MPlayer/skins/netscape4-1.0.tar.bz2
Source51: http://www1.mplayerhq.hu/MPlayer/skins/neutron-1.5.tar.bz2
Source52: http://www1.mplayerhq.hu/MPlayer/skins/new-age-1.0.tar.bz2
Source53: http://www1.mplayerhq.hu/MPlayer/skins/phony-1.1.tar.bz2
Source54: http://www1.mplayerhq.hu/MPlayer/skins/plastic-1.2.tar.bz2
Source55: http://www1.mplayerhq.hu/MPlayer/skins/plastik-2.0.tar.bz2
Source56: http://www1.mplayerhq.hu/MPlayer/skins/productive-1.0.tar.bz2
Source57: http://www1.mplayerhq.hu/MPlayer/skins/proton-1.2.tar.bz2
Source58: http://www1.mplayerhq.hu/MPlayer/skins/sessene-1.0.tar.bz2
Source59: http://www1.mplayerhq.hu/MPlayer/skins/slim-1.2.tar.bz2
Source60: http://www1.mplayerhq.hu/MPlayer/skins/smoothwebby-1.1.tar.bz2
Source61: http://www1.mplayerhq.hu/MPlayer/skins/softgrip-1.1.tar.bz2
Source62: http://www1.mplayerhq.hu/MPlayer/skins/standard-1.9.tar.bz2
Source63: http://www1.mplayerhq.hu/MPlayer/skins/trium-1.3.tar.bz2
Source64: http://www1.mplayerhq.hu/MPlayer/skins/tvisor-1.1.tar.bz2
Source65: http://www1.mplayerhq.hu/MPlayer/skins/ultrafina-1.1.tar.bz2
Source66: http://www1.mplayerhq.hu/MPlayer/skins/webby-1.3.tar.bz2
Source67: http://www1.mplayerhq.hu/MPlayer/skins/xanim-1.6.tar.bz2
Source68: http://www1.mplayerhq.hu/MPlayer/skins/xine-lcd-1.2.tar.bz2
Source69: http://www1.mplayerhq.hu/MPlayer/skins/xmmplayer-1.5.tar.bz2
URL: http://mplayerhq.hu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer >= 1.0
BuildArch: noarch


%description
This package contains a collection of additional skins for the GUI version
of MPlayer, the movie player for Linux. Install this package if you wish to
change the appeareance of MPlayer.


%prep
%setup -c %{name}-%{version} -a0 -a1 -a2     -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47     -a49 -a50 -a51 -a52 -a53 -a54 -a55 -a56 -a57 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{skindir}
%{__cp} -a * %{buildroot}%{skindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{skindir}/*


%changelog
* Wed Oct 03 2012 Denis Fateyev <denis@fateyev.com> - 1.9-1
- Updated skins versions, added new skins
- Fixed skin directory path

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 1.8-1
- Updated all skins : Abyss, Blue-small, smoothwebby and webby.
- Added new skins : Ater, brushedGnome, clearplayer, Linea and productive.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.7-1
- Updated all skins, 6 new ones too.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.6-1
- Updated all skins, two new ones too.
- No longer need to rename "default" to "classic".

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

