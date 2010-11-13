# $Id$
# Authority: matthias

Summary: Easy to use client for ED2K Peer-to-Peer Network based on eMule
Name: xmule
Version: 1.13.6
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.xmule.ws/

Source: http://dl.sf.net/xmule/xmule-%{version}.tar.bz2
Patch0: xmule-1.10.0-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, wxGTK-devel >= 2.4.2, zlib-devel, gettext
BuildRequires: cryptopp-devel
# Required by xrc
BuildRequires: expat-devel
Requires: /usr/sbin/alternatives
Obsoletes: lmule <= 1.2.1

%description
xMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.

%prep
%setup
%patch0 -p1 -b .install

%build
#CXXFLAGS="`echo "%{optflags}" | sed 's/-O./-O1/'`" \
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang xmule
%{__mv} %{buildroot}%{_bindir}/ed2k %{buildroot}%{_bindir}/ed2k.xmule

%clean
%{__rm} -rf %{buildroot}

%post
/usr/sbin/alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k.xmule 40 || :

%preun
/usr/sbin/alternatives --remove ed2k %{_bindir}/ed2k..xmule || :

%files -f xmule.lang
%defattr(-, root, root, 0755)
%doc docs/*
%{_bindir}/ed2k.xmule
%{_bindir}/xmule
%{_datadir}/applications/xmule.desktop
%{_datadir}/pixmaps/xmule.xpm

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.13.6-1
- Updated to release 1.13.6.

* Fri Oct 28 2005 Matthias Saou <http://freshrpms.net/> 1.12.0-1
- Update to 1.12.0.
- Source is back from BerliOS to SourceForge...
- Re-add cryptopp dependency, as there is now a gcc4 fix to 5.2.1... but it
  seems that the configure check is buggy and the internal lib is used.

* Thu Jul 21 2005 Matthias Saou <http://freshrpms.net/> 1.10.1-1
- Update to 1.10.1.
- Change find_land from xMule to xmule (again!).
- Update %%doc to docs/*.
- Apparently, cryptopp could maybe be used again, but it doesn't build w/ gcc4.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.10.0-1
- Update to 1.10.0 w/ new install patch.

* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net/> 1.9.4b-2
- Rebuild changing -O? to -O1 to fix cryptopp error with -O2.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 1.9.4b-1
- Update to 1.9.4b.
- Reflect xmule -> xMule change for the .po files.

* Fri Oct  1 2004 Matthias Saou <http://freshrpms.net/> 1.9.2-1
- Update to 1.9.2, updated install patch.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.4-1
- Update to 1.8.4, updated install patch.

* Sat Jul 10 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-1
- Update to 1.8.3, fails to compile.

* Tue Jun 22 2004 Matthias Saou <http://freshrpms.net/> 1.8.2d-1
- Update to 1.8.2d.
- Makefile now works with %%makeinstall, but still needs a patch.

* Mon Jun 21 2004 Matthias Saou <http://freshrpms.net/> 1.8.2c-1
- Update to 1.8.2c.

* Thu May 13 2004 Matthias Saou <http://freshrpms.net/> 1.8.2b-1
- Update to 1.8.2b.
- Added gettext build dependency otherwise the po stuff fails.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 1.8.2-1
- Update to 1.8.2, finally found after some hunting.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.1-1
- Update to 1.8.1.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.7.4b-2
- Included a fix to get downloads working better again.

* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net/> 1.7.4b-1
- Update to 1.7.4b.
- Updated Source URL to point to the file.
- Force exit status of the alternatives scriplets to true.

* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 1.7.4a-1
- Update to 1.7.4a.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 1.7.3-1
- Update to 1.7.3.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1.7.2-1
- Update to 1.7.2.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1.7.1-2
- Added alternatives support for the ed2k binary between amule and xmule.
  The highest priority is for amule since it's under active development.

* Sun Nov 23 2003 Matthias Saou <http://freshrpms.net/> 1.7.1-1
- Update to 1.7.1.
- Added patch to add DESTDIR support to the Makefile.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.6.1-7
- Bump the release to be higher than the RHL ones.
- Rebuild against gtk+ wxGTK.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.6.1-2
- Rebuild for Fedora Core 1.

* Mon Oct 13 2003 Matthias Saou <http://freshrpms.net/>
- Update stable to 1.6.1.
- Removed stable/unstable conditional build.

* Fri Aug 29 2003 Matthias Saou <http://freshrpms.net/>
- Update stable to 1.6.0a.

* Mon Aug 11 2003 Matthias Saou <http://freshrpms.net/>
- Update stable to 1.4.3.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update unstable to 1.5.6a.

* Tue Jul 22 2003 Matthias Saou <http://freshrpms.net/>
- Update stable to 1.4.2.

* Fri Jul 11 2003 Matthias Saou <http://freshrpms.net/>
- Update unstable to 1.5.5.

* Sun Jul  6 2003 Matthias Saou <http://freshrpms.net/>
- Update unstable to 1.5.4.

* Wed Jul  2 2003 Matthias Saou <http://freshrpms.net/>
- Update unstable to 1.5.3.

* Wed Jun 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.4.1a.

* Sun Jun 22 2003 Matthias Saou <http://freshrpms.net/>
- Added --with unstable build option to enable 1.5.x branch.

* Fri Jun 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.4.1.

* Wed May 28 2003 Matthias Saou <http://freshrpms.net/>
- Renamed from lmule to xmule.
- Update to 1.4.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.1.

* Wed Apr 23 2003 Stéphane Petit <stephane@petit-fr.net>
- Update to 1.2.0.1.
- Remove no more needed --with-wx-prefix= on configure.
- Remove NEWS file in doc.

* Wed Apr  2 2003 Matthias Saou <http://freshrpms.net/>
- Fix the automatic dep problem on the wxGTK lib.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.1.13c.
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

