# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Completely configurable key-combo grabber for blackbox
Name: bbkeys
Version: 0.9.0
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://bbkeys.sourceforge.net/
Source: http://dl.sf.net/bbkeys/bbkeys-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: blackbox-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  It is based on the bbtools object code
created by John Kennis and re-uses some of the blackbox window manager classes
as well.  bbkeys is easily configurable via directly hand-editing the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Clean this up, we package the exact same files cleanly in %%doc
%{__rm} -rf %{buildroot}%{_datadir}/doc/bbkeys/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO
%{_bindir}/bbkeys
%dir %{_datadir}/bbkeys/
%config %{_datadir}/bbkeys/bbkeysrc
%config %{_datadir}/bbkeys/defaultStyle
%{_mandir}/man?/*


%changelog
* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.8.6-4
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.8.6-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.6.

* Tue Aug 13 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Sat Jan 12 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing README.bbkeys and adding BUGS and NEWS

* Sat Jan 5 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- gzipping man pages by default and changing file list to reflect this

* Mon Nov 5 2001 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing bbkeysConfigC and replacing with bbkeysconf.pl

* Tue Sep 18 2001 Jason Kasper <vR@movingparts.net>
- changing to a dynamically-created bbkeys.spec

* Sun Aug 5 2001 Jason Kasper <vR@movingparts.net>
- added to file list for newly included files (docs and man pages)
- install to %{prefix} instead of /usr

* Sun May 6 2001 Hollis Blanchard <hollis@terraplex.com>
- removed file list in favor of explicit %files section
- install to /usr instead of /usr/local
- buildroot = /var/tmp/bbkeys-buildroot instead of /tmp/buildroot

