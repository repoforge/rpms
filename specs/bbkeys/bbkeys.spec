# $Id$
# Authority: matthias

Summary: completely configurable key-combo grabber for blackbox
Name: bbkeys
Version: 0.8.6
Release: 3
License: GPL
Group: User Interface/Desktops
URL: http://bbkeys.sf.net/
Source: http://dl.sf.net/bbkeys/%{name}-%{version}.tar.gz
BuildRequires: XFree86-devel, gcc-c++
BuildRoot: %{_tmppath}/%{name}-root

%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  It is based on the bbtools object code
created by John Kennis and re-uses some of the blackbox window manager classes
as well.  bbkeys is easily configurable via directly hand-editting the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755) 
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%exclude %{_prefix}/doc
%{_bindir}/*
%dir %{_datadir}/bbtools
%config %{_datadir}/bbtools/*
%{_mandir}/man?/*
 
%changelog 
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.8.6-3.fr
- Rebuild for Fedora Core.

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

