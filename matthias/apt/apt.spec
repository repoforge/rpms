# $Id$

Summary: Debian's Advanced Packaging Tool with RPM support
Name: apt
Version: 0.5.15cnc6
Release: 0
Group: System Environment/Base
License: GPL
URL: https://moin.conectiva.com.br/AptRpm
# The full URL can't be downloaded directly (referer protection?)
Source0: apt-%{version}.tar.bz2
Source1: apt.conf
Source2: vendors.list
Source3: RPM-GPG-KEY.freshrpms
Source4: sources.list.i386
Source5: sources.list.ppc
Patch0: apt-0.5.5cnc1-freshrpms.patch
Patch1: apt-0.5.15cnc6-rpmpriorities.patch
Patch10: apt-0.5.15cnc5-nodigest.patch
Patch50: apt-0.5.5cnc6-rpm402.patch
Requires: rpm >= 4.0, libstdc++
# Common to all
BuildRequires: gcc-c++, rpm-devel >= 4.0, zlib-devel, libstdc++-devel
BuildRequires: gettext, ncurses-devel, readline-devel
# For Red Hat Linux 6.2 & 7.0 (and --disable-scripts to configure too)
#BuildRequires: bzip2
# For Red Hat Linux 7.1 (and --disable-scripts to configure too)
#BuildRequires: bzip2-devel, db1-devel, docbook-utils, docbook-dtd31-sgml
#define __libtoolize :
# For YellowDog 3.0
#BuildRequires: bzip2-devel, docbook-utils, beecrypt-devel, libelf-devel
# For Red Hat Linux 8.0 & 9, Fedora Core
BuildRequires: bzip2-devel, docbook-utils, beecrypt-devel, elfutils-devel
# For Fedora Core Development
#BuildRequires: libselinux-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
A port of Debian's apt tools for RPM based distributions, or at least
originally for Conectiva and now Red Hat Linux. It provides the apt-get
utility that provides a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source capability and
several other unique features.

Available rpmbuild rebuild options :
--without : scripts


%package devel
Summary: Development files and documentation for APT's libapt-pkg
Group: Development/Libraries
PreReq: %{name} = %{version}

%description devel
This package contains the header files and static libraries for developing
with APT's libapt-pkg package manipulation library, modified for RPM.


%prep
%setup -q
%patch0 -p1 -b .httpversion
%patch1 -p1 -b .rpmpriorities
%patch10 -p1 -b .nodigest
# Only needed for rpm 4.0.2
#patch50 -p1 -b .402


%build
%configure \
    --program-prefix=%{?_program_prefix} \
    --includedir=%{_includedir}/apt-pkg \
    %{?_without_scripts: --disable-scripts}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall includedir=%{buildroot}%{_includedir}/apt-pkg
%find_lang %{name}

# The config files and empty dirs
mkdir -p %{buildroot}%{_sysconfdir}/apt
mkdir    %{buildroot}%{_sysconfdir}/apt/{apt.conf.d,sources.list.d}
cp -a rpmpriorities %{buildroot}%{_sysconfdir}/apt/
cp -a %{SOURCE1} %{SOURCE2} %{buildroot}%{_sysconfdir}/apt/
cp -a %{SOURCE3} .
%ifarch %ix86
    cp -a %{SOURCE4} %{buildroot}%{_sysconfdir}/apt/sources.list
%else
  %ifarch ppc
    cp -a %{SOURCE5} %{buildroot}%{_sysconfdir}/apt/sources.list
  %else
    echo "# No repositories for %{arch} are available, sorry." \
    > %{buildroot}%{_sysconfdir}/apt/sources.list
  %endif
%endif

# Empty cache and state directories
mkdir -p %{buildroot}%{_localstatedir}/cache/apt/archives/partial
mkdir -p %{buildroot}%{_localstatedir}/state/apt/lists/partial


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS* COPYING* RPM-GPG-KEY.freshrpms TODO doc/examples/
%dir %{_sysconfdir}/apt
%config(noreplace) %{_sysconfdir}/apt/apt.conf 
%config(noreplace) %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/apt/vendors.list
%config %{_sysconfdir}/apt/rpmpriorities
%dir %{_sysconfdir}/apt/apt.conf.d
%dir %{_sysconfdir}/apt/sources.list.d
# List all to be informed if the building of one breaks some day
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-get
%{_bindir}/apt-shell
%{_bindir}/genbasedir
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_libdir}/*.so.*
%{_libdir}/apt/
%{_mandir}/man?/*
%{_localstatedir}/cache/apt
%{_localstatedir}/state/apt


%files devel
%defattr(-, root, root)
%{_includedir}/apt-pkg
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Tue Mar 23 2004 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc6-0.1
- Update to 0.5.15cnc6.
- Updated rpmpriorities patch.
- Removed merged promoteepoch patch.

* Tue Feb 10 2004 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc5-0.2
- Added missing URL tag.
- Rebuild for Yellow Dog Linux 3.0.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc5-0.1
- Update to 0.5.15cnc5.
- updated the nodigest patch to not change genpkglist.cc nor gensrclist.cc.

* Thu Nov 27 2003 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc3-0.2
- Added missing ncurses-devel and readline-devel for apt-shell to be built,
  thanks to Gary Peck.

- Update to 0.5.15cnc3.
* Wed Nov 26 2003 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc3-0.1
- Update to 0.5.15cnc3.
- Added the testing update to the default sources.list.

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc2-1
- Update to 0.5.15cnc2.
- Removed obsolete fclose and pinning patches.

* Sun Nov  9 2003 Matthias Saou <http://freshrpms.net/> - 0.5.15cnc1-1
- Update to 0.5.15cnc1.
- Added pinning patch.

* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> - 0.5.5cnc7-1
- Update to 0.5.5cnc7.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> - 0.5.5cnc6-2
- Rebuild for Fedora Core 1.

* Mon Jun 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc6 at last.

* Sat May 20 2003 Matthias Saou <http://freshrpms.net/>
- Added a different sources.list for ppc.

* Wed Apr 16 2003 Matthias Saou <http://freshrpms.net/>
- Added Panu's nodigest patch to speed up basic operations.

* Tue Apr 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc5.

* Mon Apr  7 2003 Matthias Saou <http://freshrpms.net/>
- Removed fileutils from the rpmpriorities file, as coreutils replaces it.
- Cleaned up sources.list
- Added empty apt.conf.d and sources.list.d dirs.
- Added build option to disable the lua script engine.
- Updated %%doc.
- Removed explicit bzip2-libs dep as old systems only have bzip2.
- Added the program-prefix to workaround bad binary prefix on RHL 7.x.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to latest snapshot, first Red Hat 9 build.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc4.1.

* Fri Mar  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc4.

* Fri Feb 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc3.
- Re-enabled the man pages.

* Sat Feb 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc2.

* Thu Jan 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.5cnc1_rc1.
- Removed static libraries.
- Minor apt.conf tweaks.
- Disabled man pages since they are not being built properly.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.4cnc9.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.4cnc8.
- Added Show-Upgraded "true" to apt.conf.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Added empty /etc/apt/preferences file to make synaptic happy.
- Updated default apt.conf file to handle gpg keys.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.4cnc7.
- Removed obsolete %%docs entries.
- Now build for Red Hat Linux 8.0 with updated sources.list.

* Wed Jul 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.4cnc1.
- Updated the freshrpms version and rpmpriorities patches.
- Added mdfile, gcc3 + rpm 4.1 patches.
- Removed the flat, md5fix and nodeps patches.

* Wed Jul 10 2002 Matthias Saou <http://freshrpms.net/>
- Removed the mirror patch that was preventing signed repositories from working.
- Added my RPM-GPG-KEY file.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 7.3.
- Changed the rpmpriorities file a bit.
- Added the %%{?_smp_mflags} expansion.

* Thu Mar 21 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for rpm 4.0.4 and changed the sources.list.
- Added patch to fix md5 issue.

* Fri Feb  1 2002 Matthias Saou <http://freshrpms.net/>
- Synced against Stelian Pop's version, new patches : algo and flat.

* Wed Jan 30 2002 Matthias Saou <http://freshrpms.net/>
- Updated the source.list file with the new freshrpms.net layout.

* Wed Jan  2 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the default sources.list to not authenticate.

* Mon Dec 24 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and rebuild for Red Hat Linux.

* Tue Dec 11 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc55-1cl
- released version 0.3.19cnc55
- removed config.cache from distribution
- added --progress patch to gensrclist
- added --flat option to gensrclist

* Fri Nov 30 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc54-1cl
- released version 0.3.19cnc54
- added RPM::IgnorePkgs option
- added --progress option to most utilities 
	(Stelian Pop <stelian.pop@fr.alcove.com>)
- added RPM::IgnoreRpmlibDeps

* Mon Nov 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc53-2cl
- fixed bug in mirror patch

* Mon Nov 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc53-1cl
- released version 0.3.19cnc53
- added kernel-tape to default AllowedDupPkgs
- cleaned up gen{pkg,src}list (Alexander Bokovoy <ab@avilink.net>)
- fixed crash bug in genpkglist
- added patch to fix bug in genbasedir with empty dirs 
  (Stelian Pop <stelian.pop@fr.alcove.com>)
- configure.in patch to detect rpmdb (Stelian Pop <stelian.pop@fr.alcove.com>)
-       * Skips correctly over empty package directories
-       * Adds the --bz2only argument which makes genbasedir
-       to generate only the .bz2 compressed versions of pkglist
-       and srclist (space gain...)
-       * Doesn't change the timestamps on pkglists/srclists if
-       the contents are not modified (making possible for example
-       to make several consecutive runs of genbasedir without
-       having the apt clients download the indexes again and again).
-       * Some minor cleanups (remove the temporary files in /tmp
-       at the end of the script etc).
- (Stelian Pop <stelian.pop@fr.alcove.com>)
- cleanup patch for gensrclist (Stelian Pop <stelian.pop@fr.alcove.com>)
- fixed multi-arch pkg handling (Stelian Pop <stelian.pop@fr.alcove.com>)
- added -K (RPM::Check-Signatures) option to verify rpm sigs
- updated russian translation (Alexander Bokovoy <ab@avilink.net>)
- updated i18n (Dmitry Levin <ldv@alt-linux.org>)
- replaced Apt::GPG::Pubring with Apt::GPG::PubringPath
  also uses --homedir instead of --keyring in gpg (Ivan Zakharyashev)
- patch to detect replaced (instead of just removed) packages 
  Dmitry Levin <ldv@alt-linux.org> 
- updated mirrors patch

* Fri Oct 19 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc52-5cl
- Fixed mirrors infinite loop bug (closes: #4420).

* Tue Sep 04 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc52-4cl
- Fixed error handling.

* Thu Aug 09 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc52-3cl
- Updated mirrors patch.

* Tue Aug 07 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc52-2cl
- Added mirrors patch.

* Wed Aug 01 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc52-1cl
- released version 0.3.19cnc52
- fixed compile problem with gcc 2.96.x
- fixed bug in file method with authentication enabled 
  (Alexander Bokovoy <ab@avilink.net>)
- added RPM::RemoveOptions and RPM::UpgradeOptions

* Thu Jul 12 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc51-1cl
- released version 0.3.19cnc51
- included many portability (Solaris) fixes from 
  AUSTIN MURPHY <amurphy@nbcs.rutgers.edu>
- make packages with same version and diff deps be ignored (closes: 1628)

* Fri Jun 29 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc50-1cl
- released version 0.3.19cnc50

* Thu Jun 28 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc50-1cl
- fixed buglet in apt-cdrom

* Thu Jun 28 2001 Andreas Christian Hasenack <andreas@conectiva.com>
+ apt-0.3.19cnc49-2cl
- updated sources.list for CL7.0. Only left Rik's mirror there, I'm sure
  he will be mirroring it. Hmm, have to think about distro's instructions
  regarding apt since we will now have two versions of the distribution
  using it
- Closes: #4002 (sources.list padrão deve conter repositório de atualizações)

* Wed Jun 27 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc49-1cl
- released version 0.3.19cnc49
- added workaround for kernel installations that require upgrde on mkinitrd
  (closes: #3889)

* Mon Jun 25 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc48-1cl
- released version 0.3.19cnc48
- added RPM::AutoRebuildDB (enabled by default)
- added fetch status to CDROM method
- released (closes: #3905)

* Fri Jun 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc47-1cl
- released version 0.3.19cnc47
- fixed bug in RPM::HoldPkgs (closes: #3838)
- removed debug msg

* Tue Jun 19 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc46-1cl
- released version 0.3.19cnc46
- changed apt.conf to include RPM::AllowDupPkgs, RPM::HoldPkgs (closes: #3433)
- added Acquire::cdrom::copy, which will fetch all pkgs before installing (closes: #1024)
- added delay before file fetch retry (closes: #1294)
- fixed architecture selection (closes: #3606)
- iterating over Packages instead of Names to figure package count

* Wed Jun 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc45-1cl
- released version 0.3.19cnc45
- fixed bug with progress update (closes: #2915)

* Mon Jun 11 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc44-1cl
- released version 0.3.19cnc44
- removed %config from method drivers
- replaced option RPM::AllowedDupPackages with RPM::AllowedDupPkgs
- added option RPM::HoldPkgs (closes: #3462)

* Fri May 18 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc43-1cl
- fixed bug with record offsets (shows bad pkg description under rpm4)
- fixed bug with apt-get source (closes: #3047)

* Thu May 17 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc42-1cl
- released version 0.3.19cnc42
- merged all src patches into main src tree
- fixed stupid bug on rpminit header...
- extended Acquire::Retries to all file type acquirations (closes: #1617)

* Mon May 14 2001 Claudio Matsuoka <claudio@conectiva.com>
+ apt-0.3.19cnc41-8cl
- added Ivan Zakharyaschev's line break patch (closes: #1616)

* Wed May  9 2001 Claudio Matsuoka <claudio@conectiva.com>
+ apt-0.3.19cnc41-7cl
- adjusting rpmpriorities to reflect changes in conectiva's package base
  (glibc-base is marked as essential replacing glibc, elvis-tiny marked
  as essential, info and glib not marked as essential, etc.) (closes:
  #3115, #3117)

* Fri May  4 2001 Claudio Matsuoka <claudio@conectiva.com>
+ apt-0.3.19cnc41-6cl
- spec cleanup: removing static components from buildrequires

* Fri May  4 2001 Claudio Matsuoka <claudio@conectiva.com>
+ apt-0.3.19cnc41-5cl
- removing static link kludge added in 3cl, a better solution is in the works.

* Fri Apr 27 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc41-4cl
- Fixed NextRecord() and GetRecord() (Closes: #2915).

* Thu Apr 26 2001 Claudio Matsuoka <claudio@conectiva.com>
+ apt-0.3.19cnc41-3cl
- statically linking rpmlib and friends to avoid lossage with glibc
  upgrade from conectiva 6.0 to snapshot

* Sun Apr 15 2001 Gustavo Niemeyer <niemeyer@conectiva.com>
+ apt-0.3.19cnc41-2cl
- Added patch for ia64.

* Thu Mar 29 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc41-1cl
- released version 0.3.19cnc41
- auto rebuild rpmdb when rpm is upgraded

* Tue Mar 27 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc40-1cl
- released version 0.3.19cnc40
- custom OrderInstall() (ignores all deb specific ordering/debconf stuff)

* Fri Mar 23 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc39-1cl
- released version 0.3.19cnc39
- fixes problem with different rpmdb versions

* Thu Mar 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc38-2cl
- autotester workaround...

* Thu Mar 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc38-1cl
- released version 0.3.19cnc38
- fixed epoch display on apt-cache
- added user specified public keyring option for gpg 
- added italian po file
- fixed bug on dependency resolution for virtual packages with mult.providers

* Tue Feb 20 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc37-1cl
- released version 0.3.19cnc37
- noreplace put back for sources.list (closes: #1548)
- recompiled (closes: #1559)
- fixed dist-upgrade bogus msg (closes: #1254)
- fixed no_proxy handling

* Sat Feb 17 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc36-1cl
- released version 0.3.19cnc36
- fixed problem with arch selection (I swear it works now!)
- fixed bug with rpm4

* Wed Feb 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc35
- fixed problem with case sensitiveness
- fixed rpmpriority interpretation

* Wed Feb 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc34
- rpm4 fix?

* Wed Jan 24 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc33
- added new gui hookz

* Sat Jan 20 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc32
- fixed arch selection code
- fixed priority and section info in internal package structs

* Tue Jan 16 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- unbroke potfiles

* Mon Jan 15 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc31

* Mon Jan 15 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc30

* Sat Jan 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc29

* Thu Jan 04 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc28
- added gnupg dependency

* Thu Dec 07 2000 Andreas Hasenack <andreas@conectiva.com>
- damn! Wrong URL in sources.list, atualizacoes.conectiva.com
  doesn't exist, of course...

* Thu Dec 07 2000 Andreas Hasenack <andreas@conectiva.com>
- updated sources.list with new mirrors and new download tree
- removed (noreplace) for the sources.list file for this
  upgrade. It will be easier for the user. The (noreplace)
  should be back in place after this update as we expect no
  further big modifications for that file, only new mirrors.

* Wed Dec 06 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- fixed prob in vendors.list

* Tue Dec 05 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc27

* Wed Nov 08 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc26

* Mon Nov 06 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc25

* Thu Nov 02 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc24

* Thu Nov 02 2000 Rud<E1> Moura <ruda@conectiva.com>
- updated source.list (again)

* Thu Nov 02 2000 Rud<E1> Moura <ruda@conectiva.com>
- updated source.list

* Wed Nov 01 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc23
- added cache directories for gen{pkg,src}list
- pt_BR manpages

* Tue Oct 31 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc22
- Requires -> PreReq in apt-devel

* Mon Oct 30 2000 Alfredo Kojima <kojima@conectiva.com>
- collapsed libapt-pkg-devel and -doc to apt-devel

* Mon Oct 30 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc21

* Sun Oct 29 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc20

* Sun Oct 29 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc19
- added gensrclist
- support for apt-get source

* Fri Oct 27 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc18

* Thu Oct 26 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc17
- new manpages

* Wed Oct 25 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc16

* Sun Oct 22 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc15

* Sat Oct 21 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc14

* Thu Oct 19 2000 Claudio Matsuoka <claudio@conectiva.com>
- new upstream release: 0.3.9cnc13

* Tue Oct 17 2000 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added rpmpriorities to filelist and install

* Tue Oct 17 2000 Claudio Matsuoka <claudio@conectiva.com>
- updated to 0.3.19cnc12
- fresh CVS snapshot including: support to Acquire::ComprExtension,
  debug messages removed, fixed apt-cdrom, RPM DB path, rpmlib call
  in pkgRpmLock::Close(), package priority kludge removed, i18n
  improvements, and genbasedir/genpkglist updates.
- handling language setting in genpkglist to make aptitude happy

* Wed Oct 11 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc11
- fixed problem with shard lib symlinks

* Tue Oct 10 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc10

* Mon Oct  2 2000 Claudio Matsuoka <claudio@conectiva.com>
- fixed brown paper bag bug with method permissions
- added parameter --sign to genbasedir
- added html/text doc files

* Sat Sep 30 2000 Claudio Matsuoka <claudio@conectiva.com>
- bumped to 0.3.19cnc9
- added vendors.list
- added gpg method
- fixed minor stuff to make Aptitude work
- added missing manpages
- fixed shared libs
- split in apt, libapt-pkg, libapt-pkg-devel, libapt-pkg-doc
- rewrote genbasedir in shell script (original was in TCL)
- misc cosmetic changes

* Tue Sep 26 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc8

* Wed Sep 20 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc7

* Mon Sep 18 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc6

* Sat Sep 16 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc5

* Fri Sep 15 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc4

* Mon Sep 12 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc3

* Mon Sep 5 2000 Alfredo K. Kojima <kojima@conectiva.com>
- renamed package to apt, with version 0.3.19cncV

* Mon Sep 5 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.10
- added genpkglist and rapt-config
- program names changed back to apt-*

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.9

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.8

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.7

* Fri Sep 1 2000 Alfredo K. Kojima <kojima@conectiva.com>
- fixed typo in sources.list

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.6

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.5

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.4

* Wed Aug 30 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.3

* Thu Aug 28 2000 Alfredo K. Kojima <kojima@conectiva.com>
- second try. new release with direct hdlist handling

* Thu Aug 10 2000 Alfredo K. Kojima <kojima@conectiva.com>
- initial package creation. Yeah, it's totally broken for sure.

