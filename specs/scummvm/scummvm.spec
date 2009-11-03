# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Interpreter for several adventure games
Name: scummvm
Version: 0.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://scummvm.sourceforge.net/
Source: http://dl.sf.net/scummvm/scummvm-%{version}.tar.bz2
Patch0: scummvm-0.9.0-gcc41.patch
Patch1: scummvm-0.9.0-nostrip.patch
Patch2: scummvm-0.9.0-fontclipping.patch
Patch3: scummvm-0.9.0-theme.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel >= 1.2.2
BuildRequires: libmad-devel, libogg-devel, libvorbis-devel, flac-devel
BuildRequires: mpeg2dec-devel, zlib-devel, nasm, gcc-c++
BuildRequires: desktop-file-utils

%description
ScummVM is an implementation of the SCUMM (Script Creation Utility for
Maniac Mansion) engine used in various Lucas Arts games such as Monkey
Island and Day of the Tentacle. At this time ScummVM should be considered
ALPHA software, as it's still under heavy development. Be aware that while
many games will work with few major bugs, crashes can happen. Also note
that saved games can, and probably will, be incompatible between releases.

Also ScummVM is capable of playing several non-SCUMM games.


%prep
%setup -q
%patch0 -p1 -b .gcc41
%patch1 -p1 -b .nostrip
%patch2 -p0 -b .fontclipping
%patch3 -p0 -b .theme


%build
# No rpm configure because it breaks scummvm configure
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir}
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__install} -D -p -m 0644 gui/themes/modern.ini \
    %{buildroot}%{_datadir}/scummvm/modern.ini
%{__install} -D -p -m 0644 gui/themes/modern.zip \
    %{buildroot}%{_datadir}/scummvm/modern.zip
# Remove doc files we want to include with %doc
%{__rm} -rf %{buildroot}%{_datadir}/doc/scummvm/

desktop-file-install \
    --vendor=%{desktop_vendor} \
    --dir=%{buildroot}%{_datadir}/applications \
    dists/scummvm.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/scummvm
%{_datadir}/applications/*scummvm.desktop
%{_datadir}/pixmaps/scummvm.xpm
%{_datadir}/scummvm/
%{_mandir}/man6/scummvm.6*


%changelog
* Sun Oct 29 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.
- Spec file cleanup.
- Add datadir patch from upstream in order to include themes.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Feb 06 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.2-0.lvn.1
- version upgrade

* Mon Jan 30 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.1-0.lvn.1
- version upgrade

* Thu Dec 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.0-0.lvn.2
- fix #693 (desktop entry)
- beautify desktop-file-install

* Sat Oct 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.0-0.lvn.1
- version upgrade

* Mon Jun 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.3
- add --disable--mt32emu switch to fix build with gcc4

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.2
- fix x86_64 build

* Thu Mar 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.1
- Version Upgrade

* Tue Feb 22 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.3
- add nasm <-> x86_64

* Tue Feb 22 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.2
- fixed #371 (bild on non ix86 - David Woodhouse)

* Fri Dec 24 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.1
- added AUTHORS and TODO

* Thu Dec 23 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- added off. 0.7.0 sources

* Sun Dec 19 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- upgrade to 0.7.0 cvs (20041219), prep. for 0.7.0
- added more BuildRequires
- if without-alsa is defined actually disable alsa via configure

* Thu Nov 25 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.6.1b-0.lvn.1
-upgrade to 0.6.1b

* Thu May 27 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.6.0-0.lvn.1
- upgrade to 0.6.0

* Thu Oct 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.6
- removed #--- lines

* Tue Sep 16 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.5
- added ${RPM_OPT_FLAGS}

* Mon Sep 08 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.4
- added libvorbis-devel

* Tue Sep 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.3
- upgrade to new minor version

* Wed Aug 06 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.0-0.fdr.2
- upgrade to new major version

* Fri Aug 01 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.4.1-0.fdr.1
- Initial RPM release.
