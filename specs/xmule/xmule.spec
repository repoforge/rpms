# $Id$
# Authority: matthias

Summary: Easy to use client for ED2K Peer-to-Peer Network based on eMule
Name: xmule
Version: 1.8.1
Release: 1
License: GPL
Group: Applications/Internet
Source: http://dl.sf.net/xmule/%{name}-%{version}.tar.bz2
Patch: xmule-1.7.1-destdir.patch
URL: http://www.xmule.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: wxGTK, /usr/sbin/alternatives
BuildRequires: gcc-c++, wxGTK-devel, zlib-devel
Obsoletes: lmule <= 1.2.1

%description
xMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.


%prep
%setup
%patch -p1 -b .destdir


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/ed2k %{buildroot}%{_bindir}/ed2k.%{name}
%find_lang %{name}


%post
/usr/sbin/alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k.%{name} 40 || :


%preun
/usr/sbin/alternatives --remove ed2k %{_bindir}/ed2k.%{name} || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.1-1
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

