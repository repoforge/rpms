Summary: User-friendly file manager and visual shell
Name: mc
Version: 4.5.55
Release: 13.legacy
License: GPL
Group: System Environment/Shells
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/mc/mc-%{version}.tar.gz
Source1: redhat.links
Source10: mc-ja.po
Source11: redhat.links.ja
Source12: mc-pofiles.tar.gz
Source14: mc-cvs-uzip
URL: http://www.gnome.org/mc/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: pam >= 0.59, %{_sysconfdir}/pam.d/system-auth
%ifnarch s390 s390x
BuildRequires: gpm-devel
%endif
BuildRequires: gnome-libs-devel
BuildRequires: slang

Prereq: /sbin/chkconfig
Prereq: dev >= 3.3-3

Patch0: mc-4.5.35-xtermcolor.patch
Patch2: mc-4.5.35-fixwarning.patch

Patch3: mc-4.5.36-mimekeys.patch

Patch10: mc-4.5.35-homedir.patch
Patch16: mc-4.5.30-norpmmime.patch
Patch17: mc-4.5.42-absoluterm.patch
Patch20: mc-4.5.42-fixsh.patch
Patch21: samba-ia64.patch
Patch22: mc-4.5.43-prototype.patch
Patch23: mc-4.5.46-system-auth.patch
Patch24: mc-4.5.51-initscript.patch
Patch25: mc-4.5.51-showagain.patch
Patch26: mc-4.5.51-stderr.patch
Patch27: mc-4.5.51-gnome-editor.patch 
Patch28: mc-4.5.51-extention.patch
Patch29: mc-4.5.51-fixrescan.patch
Patch30: mc-4.5.51-time.patch
#
Patch40: mc-4.5.51-desktop.patch
Patch41: mc-4.5.51-kudzu.patch
Patch42: mc-4.5.51-troff.patch
Patch43: mc-4.5.51-initialdevices.patch
Patch44: gmc-4.5.51-mountfix.patch
Patch45: mc-4.5.55-vcsa.patch
Patch46: mc-4.5.55-zsh.patch
Patch47: mc-4.5.55-zip-fix.patch
Patch48: mc-4.5.55-trpm-fix.patch
Patch49: mc-4.5.55-regex.patch
Patch50: mc-4.5.55-mb.patch
Patch51: mc-CVE-CAN-2003-1023.patch

%description
Midnight Commander is a visual shell much like a file manager, only
with many more features. It is a text mode application, but it also
includes mouse support if you are running GPM. Midnight Commander's
best features are its ability to FTP, view tar and zip files, and to
poke into RPMs for specific files.

%ifarch nonexistent_arch ## no mcserv/gmc

%package -n gmc
Summary: The GNOME version of the Midnight Commander file manager
Requires: mc >= %{version} redhat-logos
Group: User Interface/Desktops
%description -n gmc
GMC (GNU Midnight Commander) is a file manager based on the terminal
version of Midnight Commander, with the addition of a GNOME GUI
desktop front-end. GMC can FTP, view TAR and compressed files and look
into RPMs for specific files.

%package -n mcserv
Summary: Server for the Midnight Commander network file management system
Group: System Environment/Daemons
Requires: portmap
Prereq: /sbin/chkconfig

%description -n mcserv
The Midnight Commander file management system will allow you to
manipulate the files on a remote machine as if they were local. This
is only possible if the remote machine is running the mcserv server
program. Mcserv provides clients running Midnight Commander with
access to the host's file systems.

Install mcserv on machines if you want to access their file systems
remotely using the Midnight Commander file management system.

%endif ## no mcserv/gmc

%prep
%setup -q

cp -f %{SOURCE14} vfs/extfs

%patch -p1 -b .xtermcolor

# upstream
#%patch2 -p1 -b .fixwarning
%patch3 -p1 -b .mimekeys

%patch10 -p1 -b .homedir
%patch16 -p1 -b .norpmmime
%patch17 -p1 -b .absoluterm
# upstream
# %patch20 -p1 -b .fixsh
# file to patch doesn't exist anymore
#pushd vfs/samba
#%patch21 -p2 -b .ia64
#popd
%patch22 -p1 -b .prototype
%patch23 -p1 -b .system-auth
## no longer include mcserv
## %patch24 -p1 -b .initscript
# upstream
# %patch25 -p1 -b .showagain
# upstream
# %patch26 -p1 -b .stderr
%patch27 -p1 -b .gnome
# upstream
# %patch28 -p1 -b .extention
# upstream
# %patch29 -p1 -b .fixrescan
# hopefully no longer required, just a build fix
# %patch30 -p1 -b .time
%patch40 -p1 -b .desktop

## THIS PATCH NEEDS FORWARD PORTING to use the GNOME frontend
# %patch41 -p1 -b .kudzu

## disabled for testing, see:
## https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=30647
%patch42 -p1 -b .troff
%patch43 -p1 -b .initialdevices
%patch44 -p1 -b .mountfix
%patch45 -p1 -b .vcsa
%patch46 -p1 -b .zsh
%patch47 -p1 -b .zip-fix
%patch48 -p1 -b .trpm-fix
%patch49 -p1 -b .regex
%patch50 -p1 -b .mb
%patch51 -p1 -b .vfs-fix

## replaced by sources file below
## cp %{SOURCE10} po/ja.po

## unpack pofiles
tar zxf %{SOURCE12}

%build
export CFLAGS="-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE $RPM_OPT_FLAGS"
%configure --sysconfdir=%{_sysconfdir}\
	--with-gnome \
	--without-debug
make

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,pam.d,profile.d,X11/wmconfig}

%{makeinstall} sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
# make DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT%{_bindir}/*
(cd icons; make prefix=$RPM_BUILD_ROOT%{_prefix} install_icons)
install lib/mcserv.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/mcserv

install -m 644 lib/mcserv.pamd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/mcserv
install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 644 lib/mc.global $RPM_BUILD_ROOT%{_sysconfdir}

# clean up this setuid problem for now
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/mc/bin/cons.saver

# copy redhat desktop default icons
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/desktop-links/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_libdir}/desktop-links/
# Japanese specific desktop icons
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/desktop-links/ja
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_libdir}/desktop-links/ja/redhat.links

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%ifarch nonexistent_arch ## no mcserv/gmc

%post   -n mcserv
/sbin/chkconfig --add mcserv

%preun -n mcserv
if [ "$1" = "0" ]; then
    service mcserv stop >/dev/null 2>&1
    /sbin/chkconfig --del mcserv
fi

%postun -n mcserv
if [ "$1" -ge "1" ]; then
    service mcserv condrestart >/dev/null 2>&1
fi

%endif ## no mcserv/gmc

%files -f %{name}.lang
%defattr(-, root, root, 0755)

%doc FAQ COPYING NEWS README
%{_bindir}/mc
%{_bindir}/mcedit
%{_bindir}/mcmfmt
%{_libdir}/mc/mc.ext
%{_libdir}/mc/mc.hint
%{_libdir}/mc/mc.hlp
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu
%attr(4711, vcsa, root) %{_libdir}/mc/bin/cons.saver
%{_libdir}/mc/extfs/
%{_libdir}/mc/syntax/
%{_mandir}/man1/*
%config %{_sysconfdir}/profile.d/*
%dir %{_libdir}/mc
%dir %{_libdir}/mc/bin
#%{_datadir}/mime-info/*

%ifarch nonexistent_arch  ## no mcserv/gmc

%files -n mcserv
%defattr(-, root, root, 0755)

%attr(0644, root, root) %config %{_sysconfdir}/pam.d/mcserv
%config %{_sysconfdir}/rc.d/init.d/mcserv
%attr(-, root, man)  %{_mandir}/man8/mcserv*
%{_bindir}/mcserv

%files -n gmc
%defattr(-, root, root, 0755)

%doc lib/README.desktop
%config %{_sysconfdir}/mc.global
%{_bindir}/gmc
%{_bindir}/plain-gmc
%{_bindir}/gmc-client
%{_libdir}/mc/layout
%{_libdir}/mc/mc-gnome.ext
%{_datadir}/pixmaps/mc/*
%{_datadir}/mime-info/mc.keys
%{_datadir}/idl/*.idl

%config %{_sysconfdir}/CORBA/servers/*
%config %{_libdir}/desktop-links/*

%endif  ## no mcserv/gmc

%changelog
* Sun Jan 18 2004 Jesse Keating <jkeating@j2solutions.net>
- patched for CAN-2003-1023
- updated to 2.5.55-13.legacy

* Fri Aug 23 2002 Karsten Hopp <karsten@redhat.de>
- fix german umlaut in menues (#68130)

* Fri Jul 19 2002 Jakub Jelinek <jakub@redhat.com> 4.5.55-11
- removed trailing backslash for %%configure, which
  caused mc to build with the buildroot prefix

* Wed Jul 17 2002 Karsten Hopp <karsten@redhat.de> 4.5.55-10
- support large files (#65159, #65160)
- own /usr/lib/mc/extfs and /usr/lib/mc/syntax
- fix NL translation (#63495)

* Thu Jul  4 2002 Jakub Jelinek <jakub@redhat.com>
- fix regex usage

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12 2002 Havoc Pennington <hp@redhat.com>
- patch for trpm vfs, #62306

* Wed Apr 10 2002 Havoc Pennington <hp@redhat.com>
- don't build --with-included-slang on upstream recommendation
- add uzip method from cvs, fixes some sort of format string problem
- get fix for breaking zip files while browsing them from upstream

* Tue Apr  9 2002 Havoc Pennington <hp@redhat.com>
- remove bash-specific export from mc.sh

* Thu Mar 28 2002 Havoc Pennington <hp@redhat.com>
- cons.saver rewrite to use vcsa user from Jakub, #61149
- make cons.saver attr(4711, vcsa, root)
- require new dev package

* Thu Mar  7 2002 Havoc Pennington <hp@redhat.com>
- rebuild in new environment
- 4.5.55, with lots of patch-adapting to make it build

* Fri Jan 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide
- fix prefix/share -> datadir
- comment out gmc/mcserv subpackages, place order for asbestos suit

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Sun Jul 22 2001 Havoc Pennington <hp@redhat.com>
- build requires gnome-libs-devel, #49518

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Apr 25 2001 Bill Nottingham <notting@redhat.com>
- fix mc-4.5.51-desktop.patch to work on ia64

* Mon Apr  2 2001 Preston Brown <pbrown@redhat.com>
- check return code of mount for failure (ewt)

* Thu Mar 22 2001 Owen Taylor <otaylor@redhat.com>
- Fix problem where CORBA notification wasn't working since last change.

* Fri Mar 16 2001 Owen Taylor <otaylor@redhat.com>
- Rescan devices on startup

* Mon Mar 12 2001  <jrb@redhat.com>
- remove man pages from mc.ext.in so that tgz and rpm browsing work in
  non LANG=C locales

* Wed Mar  7 2001 Owen Taylor <otaylor@redhat.com>
- Add patch to recognize kudzu's fstab entries
- Fix path to memstick icon

* Fri Feb 23 2001 Trond Eivind Glomsr鷣 <teg@redhat.com>
- use %%{_tmppath}
- langify

* Tue Feb 21 2001 Akira TAGOH <tagoh@redhat.com>
- Fixed install some desktop icons for specific language.

* Fri Feb 16 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Red Hat JP desktop icons.

* Wed Feb 14 2001 Jakub Jelinek <jakub@redhat.com>
- include both sys/time.h and time.h on glibc 2.2.2
- fix Japanese patch to include locale.h.

* Tue Feb  6 2001 Trond Eivind Glomsr鷣 <teg@redhat.com>
- i18nize initscript

* Sat Jan 27 2001 Akira TAGOH <tagoh@redhat.com>
- Added Japanese patch(language specific desktop icons).

* Fri Jan 19 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese translation.

* Sun Jan 14 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- do not prereq %{_sysconfdir}/init.d
- do not require gpm for s390

* Mon Aug 21 2000 Jonathan Blandford <jrb@redhat.com>
- fixed bug 16467

* Thu Aug 17 2000 Tim Powers <timp@redhat.com>
- modified my patch (again) to free quoted

* Thu Aug 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- run %%configure in the build phase, not the setup
- modify Tim's patch to always just edit one file

* Thu Aug 17 2000 Than Ngo <than@redhat.com>
- fix problems viewing the package (Bug #16378)

* Thu Aug 17 2000 Tim Powers <timp@redhat.com>
- fixed bug #16269

* Fri Aug  4 2000 Tim Waugh <twaugh@redhat.com>
- make stdout/stderr writable before forking

* Wed Aug 02 2000 Jonathan Blandford <jrb@redhat.com>
- Updated desktop entries.

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 19 2000 Jonathan Blandford <jrb@redhat.com>
- make the togglebutton patch work correctly

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error in mcserv.init that crept in with condrestart

* Mon Jul 17 2000 Jonathan Blandford <jrb@redhat.com>
- added a toggle button to let people turn off the "you are running
  gmc as root" warning.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript, add condrestart stuff

* Mon Jul 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- remove execute bits from config/pam files

* Mon Jul  3 2000 Jonathan Blandford
- Update to 4.5.51.  Now there is a trashcan!

* Thu Jun 15 2000 Owen Taylor <otaylor@redhat.com>
- Update to 4.5.49

* Fri Jun  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Mon May 22 2000 Bill Nottingham <notting@redhat.com>
- hmmm, ia64 patches fell out.

* Fri May 19 2000 Jonathan Blandford <jrb@redhat.com>
- upgrade to new version of mc.
- removed builtincpio patch

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Wed Feb 22 2000 Preston Brown <pbrown@redhat.com>
- fix mc.sh, function was not exported

* Wed Feb 17 2000 Jakub Jelinek <jakub@redhat.com>
- builtin cpio vfs, change rpm extfs to use it -
  should speed up e.g. copyout from rpm by orders of magnitude
  patch by Jan Hudec <jhud7196@artax.karlin.mff.cuni.cz>
- fix buglet in the patch

* Mon Feb 14 2000 Preston Brown <pbrown@redhat.com>
- move redhat-logos depency to gmc (#9395)

* Fri Feb 4 2000 Jonathan Blandford <jrb@redhat.com>
- changed default rpm action to be upgrade.
- Changed locale to be in mc package, instead of gmc.

* Thu Feb 3 2000 Jonathan Blandford <jrb@redhat.com>
- use /bin/rm instead of rm so that aliases won't interfere with the
  script

* Fri Sep 25 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Wed Sep 22 1999 Michael Fulbright <drmike@redhat.com>
- updated to 4.5.39-pre9

* Wed Aug 04 1999 Michael K. Johnson <johnsonm@redhat.com>
- moved configure to setup
- buildrequires gpm-devel so mouse works in console

* Wed Jul 22 1999 Michael Fulbright <drmike@redhat.com>
- added ${prefix}/lib/mc/syntax to mc file list
- turned off samba support

* Wed Jul  7 1999 Jonathan Blandford <jrb@redhat.com>
- updated mc to work with mc 4.5.36.  Thanks to Brian Ryner
  <bryner@uiuc.edu> for providing the patch.

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- removed rpm menu defs - we depend on gnorpm for these
- fixed bug that caused crash if group doesnt exist for file

* Thu Apr 15 1999 Michael Fulbright <drmike@redhat.com>
- cleanup several dialogs

* Mon Apr 12 1999 Michael Fulbright <drmike@redhat.com>
- true version 4.5.30

* Fri Apr 09 1999 Michael Fulbright <drmike@redhat.com>
- version pre-4.5.30 with patch to make this link on alpha properly
  Mark as version 0.7 to denote not the official 4.5.30 release

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- fixed errata support URL

* Tue Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.29
- added default desktop icons for Red Hat desktop
- added redhat-logos to requirements
- added README.desktop to doc list for gmc
- added locale data

* Fri Mar 25 1999 Preston Brown <pbrown@redhat.com>
- patched so that TERM variable set to xterm produces color

* Mon Mar 22 1999 Michael Fulbright <drmike@redhat.com>
- made sure %{_sysconfdir}/pam.d/mcserv has right permissions

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.27

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- fix'd icon display problem

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.25 AND 4.5.26

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.24

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.16
- removed mc.keys from mc file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.14
- fixed file list

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.11

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.10

* Fri Jan 22 1999 Michael Fulbright <drmike@redhat.com>
- added metadata to gmc file list

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.9

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.6

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against gnome-libs 0.27 and gtk+-1.1

* Thu Jul 09 1998 Michael Fulbright <msf@redhat.com>
- made cons.saver not setuid

* Sun Apr 19 1998 Marc Ewing <marc@redhat.com>
- removed tkmc

* Wed Apr 8 1998 Marc Ewing <marc@redhat.com>
- add %{prefix}/lib/mc/layout to gmc

* Tue Dec 23 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
- added --without-debug to configure,
- modification in %build and %install and cosmetic modification in packages
  headers,
- added %%{PACKAGE_VERSION} macro to Buildroot,
- removed "rm -rf $RPM_BUILD_ROOT" from %prep.
- removed Packager field.

* Thu Dec 18 1997 Michele Marziani <marziani@fe.infn.it>
- Merged spec file with that from RedHat-5.0 distribution
  (now a Hurricane-based distribution is needed)
- Added patch for RPM script (didn't always work with rpm-2.4.10)
- Corrected patch for mcserv init file (chkconfig init levels)
- Added more documentation files on termcap, terminfo, xterm

* Thu Oct 30 1997 Michael K. Johnson <johnsonm@redhat.com>

- Added dependency on portmap

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>

- fixed spec file.
- Updated to 4.1.8

* Sun Oct 26 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- updated to 4.1.6
- added %attr macros in %files,
- a few simplification in %install,
- removed glibc patch,
- fixed installing %{_sysconfdir}/X11/wmconfig/tkmc.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>

- updated to 4.1.5
- added wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>

- chkconfig is for mcserv package, not mc one

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>

- patched init script for chkconfig
- don't turn on the service by default

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>

- Converted to new PAM conventions.
- Updated to 4.1.3
- No longer needs glibc patch.

* Thu May 22 1997 Michele Marziani <marziani@fe.infn.it>

- added support for mc alias in %{_sysconfdir}/profile.d/mc.csh (for csh and tcsh)
- lowered number of SysV init scripts in %{_sysconfdir}/rc.d/rc[0,1,6].d
  (mcserv needs to be killed before inet)
- removed all references to $RPM_SOURCE_DIR
- restored $RPM_OPT_FLAGS when compiling
- minor cleanup of spec file: redundant directives and comments removed

* Sun May 18 1997 Michele Marziani <marziani@fe.infn.it>

- removed all references to non-existent mc.rpmfs
- added mcedit.1 to the %files section
- reverted to un-gzipped man pages (RedHat style)
- removed double install line for mcserv.pamd

* Tue May 13 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- added new rpmfs script,
- removed mcfn_install from mc (adding mc() to bash enviroment is in
  %{_sysconfdir}/profile.d/mc.sh),
- %{_sysconfdir}/profile.d/mc.sh changed to %config,
- removed %{prefix}/lib/mc/bin/create_vcs,
- removed %{prefix}/lib/mc/term.

* Wed May 9 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- changed source url,
- fixed link mcedit to mc,

* Tue May 7 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- new version 3.5.27,
- %dir %{prefix}/lib/mc/icons and icons removed from tkmc,
- added commented xmc part.

* Tue Apr 22 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- FIX spec:
   - added URL field,
   - in mc added missing %{prefix}/lib/mc/mc.ext, %{prefix}/lib/mc/mc.hint,
     %{prefix}/lib/mc/mc.hlp, %{prefix}/lib/mc/mc.lib, %{prefix}/lib/mc/mc.menu.

* Fri Apr 18 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>

- added making packages: tkmc, mcserv (xmc not work yet),
- gziped man pages,
- added %{_sysconfdir}/pamd.d/mcserv PAM config file.
- added instaling icons,
- added %{_sysconfdir}/profile.d/mc.sh,
- in %doc added NEWS README,
- removed %{prefix}/lib/mc/FAQ,
- added mcserv.init script for mcserv (start/stop on level 86).
