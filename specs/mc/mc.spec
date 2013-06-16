# $Id$
# Authority: dfateyev
# Upstream: MC Team <mc-devel$gnome,org>

# Tag: rfx

Summary:   User-friendly text console file manager and visual shell
Name:      mc
Version:   4.8.8
Release:   1%{?dist}
Epoch:     2
License:   GPLv2
Group:     System Environment/Shells

Source:    http://ftp.midnight-commander.org/mc-%{version}.tar.bz2
URL:       http://www.midnight-commander.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel
BuildRequires: e2fsprogs-devel
BuildRequires: slang-devel
BuildRequires: pcre-devel
BuildRequires: gpm-devel

%description
GNU Midnight Commander is a visual file manager.  It's a feature rich
full-screen text mode application that allows you to copy, move and
delete files and whole directory trees, search for files and run
commands in the subshell.  Internal viewer and editor are included.
Mouse is supported under X Window System and on Linux console.  VFS
(Virtual Filesystem) allows you to view archives and files on remote
servers (via SAMBA, FTP or SSH).

%prep
%setup

%build
%configure \
	--with-screen=slang \
	--enable-charset \
	--enable-vfs-smb \
	--with-samba \
	--with-x \
	--with-gpm-mouse
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}

%{__install} -d -m 755 %{buildroot}/%{_sysconfdir}/profile.d
%{__install} contrib/{mc.sh,mc.csh} %{buildroot}/%{_sysconfdir}/profile.d

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)

%doc doc/FAQ COPYING doc/NEWS doc/README
%{_bindir}/mc
%{_bindir}/mcedit
%{_bindir}/mcview
%{_bindir}/mcdiff
%attr(4755, vcsa, tty) %{_libexecdir}/mc/cons.saver
%{_libexecdir}/mc/mc*sh
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/mc.1*
%lang(hu) %{_mandir}/hu/man1/mc.1*
%lang(it) %{_mandir}/it/man1/mc.1*
%lang(pl) %{_mandir}/pl/man1/mc.1*
%lang(ru) %{_mandir}/ru/man1/mc.1*
%lang(sr) %{_mandir}/sr/man1/mc.1*

%{_sysconfdir}/profile.d/*

%config %{_sysconfdir}/mc/sfs.ini

%config(noreplace) %{_sysconfdir}/mc/*edit*
%config(noreplace) %{_sysconfdir}/mc/mc.ext
%config(noreplace) %{_sysconfdir}/mc/mc.menu
%config(noreplace) %{_sysconfdir}/mc/filehighlight.ini
%config(noreplace) %{_sysconfdir}/mc/mc.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.default.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.emacs.keymap
%config(noreplace) %{_sysconfdir}/mc/mc.menu.sr
%dir %{_datadir}/mc
%{_datadir}/mc/*

%dir %{_libexecdir}/mc
%{_libexecdir}/mc/ext.d/*
%{_libexecdir}/mc/extfs.d/*
%{_libexecdir}/mc/fish/*

%changelog
* Sun Jun 16 2013 Denis Fateyev <denis@fateyev.com> - 4.8.8-1
- rebuild for Repoforge

* Mon May 20 2013 Denis Fateyev <denis@fateyev.com> - 4.8.8-1.denf
- update to 4.8.8

* Thu Jan 10 2013 Denis Fateyev <denis@fateyev.com> - 4.8.7-1.denf
- update to 4.8.7

* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 4.8.6-1.denf
- update to 4.8.6

* Fri Sep 14 2012 Denis Fateyev <denis@fateyev.com> - 4.8.5-1.denf
- update to 4.8.5

* Wed Feb 08 2012 Denis Fateyev <denis@fateyev.com> - 4.8.1-1.denf
- update to 4.8.1

* Tue Oct 25 2011 Denis Fateyev <denis@fateyev.com> - 4.8.0-1.denf
- update to 4.8.0

* Sat Oct 01 2011 Denis Fateyev <denis@fateyev.com> - 4.7.5.5-1.denf
- update to 4.7.5.5

* Fri May 06 2011 Denis Fateyev <denis@fateyev.com> - 4.7.5.2-1.denf
- update to 4.7.5.2

* Fri Apr 08 2011 Denis Fateyev <denis@fateyev.com> - 4.7.5.1-2.denf
- added epoch for more compatibility with original package

* Sun Feb 27 2011 Denis Fateyev <denis@fateyev.com> - 4.7.5.1-1.denf
- rebuild for 'denf' repository

* Mon Feb 07 2011 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.5.1

* Thu Dec 28 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.5

* Sat Sep 11 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.4

* Fri Aug 06 2010 Denis Frolov <d.frolov81@mail.ru>
- add patch achown http://www.midnight-commander.org/changeset/ce12059b0e7c7df3b7a1ebc908d48e4eb3b454e5

* Thu Jul 06 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.3

* Wed May 06 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.2

* Wed Feb 26 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.1

* Wed Feb 03 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.0.2

* Sun Jan 03 2010 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.0.1

* Sat Dec 26 2009 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7.0

* Thu Nov 24 2009 Denis Frolov <d.frolov81@mail.ru>
- add syntax patch

* Sat Oct 31 2009 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7-pre4

* Fri Oct 02 2009 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7-pre3

* Sun Aug 30 2009 Denis Frolov <d.frolov81@mail.ru>
- update to 4.7-pre2

* Mon Aug 03 2009 Denis Frolov <d.frolov81@mail.ru>
- Rebuild for CentALT repo

* Sat Jul 04 2009 Yury V. Zaytsev <yury@shurup.com>
- Fix the issue when wrappers were left unpackaged

* Thu May 21 2009 Slava Zanko <slavazanko@gmail.com>
- Fix install patches: use %{_sysconfdir}/mc directory

* Fri May 8 2009 Slava Zanko <slavazanko@gmail.com>
- Review spec-file to build on the current distributions
- Change build rules
- Fix install pathes

* Fri Jun 22 2007 Pavel Roskin <proski@gnu.org>
- Make cons.saver suid vcsa, it's needed for Fedora 7

* Thu Dec 21 2006 Pavel Roskin <proski@gnu.org>
- Don't rely on brace expansion, it may be disabled

* Mon Jan 30 2006 Pavel Roskin <proski@gnu.org>
- Avoid using %{_prefix} where more specialized macros are available.

* Tue Aug 02 2005 Pavel Roskin <proski@gnu.org>
- Replace obsolete "Copyright" with "License".

* Thu Mar 31 2005 Pavel Roskin <proski@gnu.org>
- Comment out build dependencies - they are too distribution specific.

* Tue Sep 23 2003 Pavel Roskin <proski@gnu.org>
- Remove term directory, it's obsolete and irrelevant on modern systems.
- Include translated menu files.

* Sun Feb 16 2003 Pavel Roskin <proski@gnu.org>
- Remove obsolete dependency on /sbin/chkconfig.

* Tue Dec 24 2002 Pavel Roskin <proski@gnu.org>
- Work around bug in rpm 4.1 that expands defines in comments.
- Handle --without-x.

* Mon Nov 04 2002 Andrew V. Samoilov <sav@bcs.zp.ua>
- Handle --with ext2undel.

* Fri Nov 01 2002 Pavel Roskin <proski@gnu.org>
- Add wrappers to support setting last directory on exit.  Keep all
  scripts in their original directory, just copy them.

* Tue Oct 22 2002 Pavel Roskin <proski@gnu.org>
- Don't use the included S-Lang, there is a workaround for Red Hat 8.0
  S-Lang, and binary compatibility with Red Hat 7.x doesn't work anyway.

* Tue Oct 08 2002 Pavel Roskin <proski@gnu.org>
- Use the included S-Lang again, since we include a better version now.
  This should avoid incompatibility with Red Hat 7.x.
- Add _with_glib2 option.

* Mon Oct 07 2002 Pavel Roskin <proski@gnu.org>
- Remove installed mc.sh and mc.csh from %{_prefix}/share/mc/bin to
  suppress a warning about installed but unpackaged files.

* Mon Sep 30 2002 Andrew V. Samoilov <sav@bcs.zp.ua>
- Don't require slang-devel if _with_ncurses.
- Handle --with samba.

* Sun Sep 29 2002 Pavel Roskin <proski@gnu.org>
- Use --with-screen instead of --with-ncurses and --with-included-slang.

* Mon Sep 23 2002 Andrew V. Samoilov <sav@bcs.zp.ua>
- Restore %config for %{_prefix}/share/mc/mc.charsets.
- Restore %{_prefix}/share/mc/edit.spell.rc.

* Sat Sep 21 2002 Pavel Roskin <proski@gnu.org>
- Use FHS-compliant paths.
- Drop %config from files under /usr/share - users are not supposed to
  edit them.  Local copies under ~/.mc should be used for that.

* Wed Aug 21 2002 Pavel Roskin <proski@gnu.org>
- Change description, update URLs, allow dash in the version.

* Tue Aug 20 2002 Pavel Roskin <proski@gnu.org>
- Support conditional builds.

* Tue Aug 20 2002 Andrew V. Samoilov <sav@bcs.zp.ua>
- Add /usr/lib/mc/mc.charsets.
- Add %{_mandir}/*/man1/*.

* Fri Aug 16 2002 Pavel Roskin <proski@gnu.org>
- Remove mc.global.

* Mon Jan 21 2002 Pavel Roskin <proski@gnu.org>
- Remove --with-gnome and --with-included-slang from configure options.
- Add BuildPrereq.

* Fri Aug 24 2001 Pavel Roskin <proski@gnu.org>
- Remove gmc.  Reunite mc and mc-common.

* Sun Aug 05 2001 Pavel Roskin <proski@gnu.org>
- Set epoch.

* Sun Jul 15 2001 Pavel Roskin <proski@gnu.org>
- Remove /usr/lib/mc/layout.

* Sat Jun 09 2001 Pavel Roskin <proski@gnu.org>
- Use %{_prefix} and %{_mandir}. Specify --mandir to configure.

* Fri May 25 2001 Pavel Roskin <proski@gnu.org>
- Change groups. Don't include locale directories. More config files.

* Sun May 20 2001 Pavel Roskin <proski@gnu.org>
- Don't require stylesheets, since HTML files are now in the tarball.

* Thu Apr 19 2001 Pavel Roskin <proski@gnu.org>
- Remove package mcserv. Drop dependency on PAM.

* Mon Feb 26 2001 Pavel Roskin <proski@gnu.org>
- Remove mc-gnome.ext.

* Thu Jan 11 2001 Pavel Roskin <proski@gnu.org>
- Include mcview.

* Mon Oct 23 2000 Pavel Roskin <proski@gnu.org>
- Allow mcserv.8 to be gzipped.

* Sat Sep 30 2000 Pavel Roskin <proski@gnu.org>
- New package mc-common.
- Use DESTDIR instead of misusing prefix.
- Don't install old icons - they don't exist

* Sat Sep 23 2000 Pavel Roskin <proski@gnu.org>
- Include translations with mc, not gmc
- chkconfig --del in %preun, not %postun
- --without-debug not needed
- /etc/X11/wmconfig not needed
- /etc/pam.d/mcserv shouldn't be executable
- New files in %{prefix}/lib/mc/ - translated hints, editor files

* Thu Sep 09 1999 Elliot Lee <sopwith@redhat.com>
- Include .idl files in the package.

* Sat Sep 04 1999 Gregory McLean <gregm@comstar.net>
- Added a build prereq so that rpms get built with documentation ;)

* Mon Jul 12 1999 Kjartan Maraas  <kmaraas@online.no>
- added help and locale files to %files

* Tue Jun 22 1999 Vladimir Kondratiev <vkondra@iil.intel.com>
- added syntax files to %files

* Wed May 26 1999 Cody Russell <bratsche@dfw.net>
- chmod cons.saver at $RPM_BUILD_ROOT%{prefix}/lib rather than at
  $RPM_BUILD_ROOT/usr/lib. We can now install to somewhere other than /usr.

* Sun Apr 18 1999 Gregory McLean <gregm@comstar.net>
- Updated the specfile, removed some kludges.

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against gnome-libs 0.27 and gtk+-1.1

* Thu Jul 09 1998 Michael Fulbright <msf@redhat.com>
- made cons.saver not setuid

* Sun Apr 19 1998 Marc Ewing <marc@redhat.com>
- removed tkmc

* Wed Apr 8 1998 Marc Ewing <marc@redhat.com>
- add /usr/lib/mc/layout to gmc
