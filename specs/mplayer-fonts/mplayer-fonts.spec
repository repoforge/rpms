# $Id$
# Authority: matthias
# Dist: nodist

# Default font encoding, iso-8859-1 iso-8859-2 iso-8859-7 or cp1250
%define font iso-8859-1

# The default font size for subtitles : 14, 18, 24 or 28
%define size 18

Summary: Font files for MPlayer
Name: mplayer-fonts
Version: 1.1
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/
Source0: http://www.mplayerhq.hu/MPlayer/releases/fonts/font-arial-cp1250.tar.bz2
Source1: http://www.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-1.tar.bz2
Source2: http://www.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-2.tar.bz2
Source3: http://www.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-7.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Conflicts: mplayer < 0.90
BuildArch: noarch

%description
MPlayer is a multimedia player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

This package contains the fonts used for subtitles and OSD.


%prep
%setup -c %{name}-%{version} -a1 -a2 -a3


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/mplayer/
%{__cp} -a * %{buildroot}%{_datadir}/mplayer/
# Make a symlink to the default font
%{__ln_s} -f font-arial-%{font}/font-arial-%{size}-%{font} \
    %{buildroot}%{_datadir}/mplayer/font


%clean
%{__rm} -rf %{buildroot}


%pre
# We provide a symlink... some have an empty dir, this fixes it!
[ -d %{_datadir}/mplayer/font ] && \
    rmdir %{_datadir}/mplayer/font 2>/dev/null || :


%files
%defattr(0644, root, root, 0755)
%{_datadir}/mplayer/*


%changelog
* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.1-3
- Minor spec file cleanups.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1-2
- Rebuild for Fedora Core 1.

* Wed Aug 13 2003 Matthias Saou <http://freshrpms.net/>
- Updated to the latest packages from mplayerhq.hu.
- Added iso-8859-7 and cp1250 fonts.
- Updated dependencies, as some people seem to have trouble with them.

* Tue Apr  8 2003 Matthias Saou <http://freshrpms.net/>
- Split this font package at last!

