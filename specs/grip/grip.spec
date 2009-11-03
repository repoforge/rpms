# $Id$
# Authority: matthias
# Upstream: Mike Oliphant <grip$nostatic,org>

Summary: Graphical CD player, CD ripper and encoder frontend
Name: grip
Version: 3.2.0
Release: 2%{?dist}
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.nostatic.org/grip/
Source: http://dl.sf.net/grip/grip-%{version}.tar.gz
Patch: grip-3.1.7-default.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: vorbis-tools
BuildRequires: gcc-c++, libgnomeui-devel >= 2.2.0, vte-devel, curl-devel
BuildRequires: id3lib-devel, gettext
# Required on Yellow Dog Linux 3.0
%{?yd3:BuildRequires: ncurses-devel, openssl-devel}

%description
Grip is a CD player and CD ripper for GNOME. It has the ripping capabilities
of cdparanoia built in, but can also use external rippers (such as
cdda2wav). It also provides an automated frontend for MP3 encoders, letting
you take a disc and transform it easily straight into MP3s. The CDDB
protocol is supported for retrieving track information from disc database
servers.


%prep
%setup
%patch -p1 -b .rh-default-encoder


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}-2.2


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}-2.2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS README TODO
%doc %{_datadir}/gnome/help/grip/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png


%changelog
* Wed Apr 28 2004 Matthias Saou <http://freshrpms.net/> 1:3.2.0-1
- Update to 3.2.0.

* Thu Apr 22 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.10-1
- Update to 3.1.10.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.9-1
- Update to 3.1.9.

* Sat Mar 27 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.8-1
- Update to 3.1.8.

* Tue Mar 23 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.7-1
- Update to 3.1.7.
- Change libghttp dependency to curl.

* Wed Mar  3 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.5-1
- Update to 3.1.5.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.4-2
- Removed the duplicate desktop entry and obsolete manipulations too.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 1:3.1.4-1
- Update to 3.1.4.
- Removed the cdparanoia and locking patches as fixes have gone upstream.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1:3.1.3-3
- Include the 3 current RH patches to default config to oggenc, fix
  cdparanoia detection and fix locking issues.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1:3.1.3-2
- Fixed the default menu entry to have it actually appear.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1:3.1.3-1
- Update to 3.1.3, updated dependencies.
- Rebuild for Fedora Core 1.

* Thu Oct  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.1.2.

* Thu Apr 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.7.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Feb 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.6.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.5.

* Tue Dec 31 2002 Ville Skyttä <ville.skytta at iki.fi> - 1:3.0.4-fr1
- Update to 3.0.4.
- Use shared cdparanoia and id3lib.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Wed Sep 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.3.

* Thu Aug 29 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.1.
- Added %%find_lang.
- Updated dependencies.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Wed Apr 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.0.0.

* Mon Mar 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.99.0.

* Sat Feb  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.98.5.

* Thu Jan 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.98.3.

* Mon Jan 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.98.2 and spec file cleanup.

* Thu Jul 26 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 2.96 and spec file cleanup.
- Added .org to "nostatic" in the URL... it's correct now :-)

* Wed Aug 9 2000 Tim Powers <timp@redhat.com>
- added Serial so that we can upgrade from the Helix packages for 6.2

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- include icon properly
- fix up man path patch

* Wed Jun 7 2000 Tim Powers <timp@redhat.com>
- fixed manpage location
- use %%makeinstall and other predefined macros wherever possible

* Fri May 12 2000 Tim Powers <timp@redhat.com>
- updated to 2.94

* Sun Feb 06 2000 Preston Brown <pbrown@redhat.com>
- fix more problems w/man page because of gzip

* Sun Jan 16 2000 Preston Brown <pbrown@redhat.com>
- 2.91
- fix man page symlink

* Thu Nov 11 1999 Tim Powers <timp@redhat.com>
- updated to 2.8
- no longer need separate cdparanoia source
- gzip man pages
- added desktop entry

* Mon Aug 30 1999 Bill Nottingham <notting@redhat.com>
- update to 2.6

* Thu Jul 15 1999 Tim Powers <timp@redhat.com>
- updated grip source
- included cdparanoia source, builds during the build routine so
  we can have a complete grip build
- and all were happy when it twas built for 6.1

* Sat Apr 18 1999 Michael Maher <mike@redhat.com>
- built package for 6.0
