# Authority: freshrpms
Summary: A collection of skins for MPlayer.
Name: mplayer-skins
Version: 1.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/MPlayer/Skin/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://mplayerhq.hu/MPlayer/Skin/AlienMind-1.0.tar.bz2
Source1: http://mplayerhq.hu/MPlayer/Skin/Blue-small-1.0.tar.bz2
Source2: http://mplayerhq.hu/MPlayer/Skin/BlueHeart-1.4.tar.bz2
Source3: http://mplayerhq.hu/MPlayer/Skin/Canary-1.0.tar.bz2
Source4: http://mplayerhq.hu/MPlayer/Skin/CornerMP-1.0.tar.bz2
Source5: http://mplayerhq.hu/MPlayer/Skin/CornerMP-aqua-1.0.tar.bz2
Source6: http://mplayerhq.hu/MPlayer/Skin/Cyrus-1.0.tar.bz2
Source7: http://mplayerhq.hu/MPlayer/Skin/MidnightLove-1.5.tar.bz2
Source8: http://mplayerhq.hu/MPlayer/Skin/Orange-1.0.tar.bz2
Source9: http://mplayerhq.hu/MPlayer/Skin/QPlayer-1.0.2.tar.bz2
Source10: http://mplayerhq.hu/MPlayer/Skin/WindowsMediaPlayer6-1.2.tar.bz2
Source11: http://mplayerhq.hu/MPlayer/Skin/avifile-1.5.tar.bz2
Source12: http://mplayerhq.hu/MPlayer/Skin/default-1.7.tar.bz2
Source13: http://mplayerhq.hu/MPlayer/Skin/disappearer-1.0.tar.bz2
Source14: http://mplayerhq.hu/MPlayer/Skin/gnome-1.1.tar.bz2
Source15: http://mplayerhq.hu/MPlayer/Skin/hayraphon-1.0.tar.bz2
Source16: http://mplayerhq.hu/MPlayer/Skin/hwswskin-1.0.tar.bz2
Source17: http://mplayerhq.hu/MPlayer/Skin/krystal-1.0.tar.bz2
Source18: http://mplayerhq.hu/MPlayer/Skin/mentalic-1.1.tar.bz2
Source19: http://mplayerhq.hu/MPlayer/Skin/neutron-1.4.tar.bz2
Source20: http://mplayerhq.hu/MPlayer/Skin/phony-1.0.tar.bz2
Source21: http://mplayerhq.hu/MPlayer/Skin/plastic-1.1.1.tar.bz2
Source22: http://mplayerhq.hu/MPlayer/Skin/proton-1.1.tar.bz2
Source23: http://mplayerhq.hu/MPlayer/Skin/slim-1.0.tar.bz2
Source24: http://mplayerhq.hu/MPlayer/Skin/softgrip-1.0.tar.bz2
Source25: http://mplayerhq.hu/MPlayer/Skin/trium-1.0.tar.bz2
Source26: http://mplayerhq.hu/MPlayer/Skin/xanim-1.5.tar.bz2
Source27: http://mplayerhq.hu/MPlayer/Skin/xine-lcd-1.0.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: mplayer >= 0.90

%description
This package contains a collection of additional skins for the GUI version
of MPlayer, the movie player for Linux. Install this package if you wish to
change the appeareance of MPlayer.

%prep
%setup -c -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/mplayer/Skin
%{__cp} -afv * %{buildroot}%{_datadir}/mplayer/Skin/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644, root, root, 0755)
%{_datadir}/mplayer/Skin/

%changelog
* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated with new skins from the mplayer website.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Initial package. (using DAR)
