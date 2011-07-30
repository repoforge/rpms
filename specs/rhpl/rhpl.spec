# $Id$
# Authority: dag

### EL5 ships with rhpl-0.194.1-1
### EL4 ships with rhpl-0.148.6-1
### EL3 ships with rhpl-0.110.6-1
# ExcludeDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Library of Python code used by installation and configuration tools
Name: rhpl
Version: 0.221
Release: 2%{?dist}
License: GPLv2+
Group: System Environment/Libraries

Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: python-devel
%ifnarch s390 s390x
BuildRequires: wireless-tools-devel
%endif
Conflicts: hwdata < 0.169
Conflicts: kbd < 1.12-21
Conflicts: wireless-tools < 28-0.pre8.5

%description
The rhpl package contains Python code used throughout the system.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%{python_sitearch}/rhpl/

%changelog
* Sat Jul 30 2011 Dag Wieers <dag@wieers.com> - 0.222-2
- Forward ported from RHEL6 Beta.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Jeremy Katz <katzj@redhat.com> 0.222-1
- Fix leaking fd for loadkeys with a big hammer (#501368)
- Fix Russian keyboard (#492544)

* Mon Apr 13 2009 Chris Lumens <clumens@redhat.com> 0.220-1
- Attempt to fix an error when catching OSError (#493271).

* Tue Jan 27 2009 Martin Sivak <msivak@redhat.com> 0.219-1
- National keyboard layout is prefered over us variant (#473056)

* Mon Oct 13 2008 Chris Lumens <clumens@redhat.com> 0.217-1
- Don't set XKB model (ajax, #461832).
- Don't use the deprecated gtk.mainiteration function (#432115).
- Use $(MAKE), not make (#458455).
- Use the Save stock button instead of Open (#432345).

* Fri Jun 13 2008 Chris Lumens <clumens@redhat.com> 0.216-1
- Fix Swiss French keyboard layout (#448878).
- Now with more Romanian keyboard layouts! (#450381)
- Add irish (#431998).
- Add inet keycodes to the model (like XKB expects) instead of to
  the layout (like it doesn't) (ajax).

* Fri Mar 28 2008 Adam Jackson <ajax@redhat.com> 0.215-1
- Fix keyboard typo

* Thu Mar 27 2008 Dennis Gilmore <dennis@ausil.us> 0.214-2
- sparc64 is a lib64 arch

* Thu Mar 27 2008 Adam Jackson <ajax@redhat.com> 0.214-1
- pci alias parsing module (ajax)
- keyboard scanning converted from kudzu to hal (notting)

* Fri Feb 08 2008 Chris Lumens <clumens@redhat.com> - 0.213-1
- Update Serbian keyboard layouts again (#431304). (clumens)

* Tue Dec 11 2007 Jeremy Katz <katzj@redhat.com> - 0.212-1
- fix broken build

* Fri Dec  7 2007 Jeremy Katz <katzj@redhat.com> - 0.211-1
- package review cleanups (#226372) (katzj)
- git-ify the makefile, remove the ChangeLog (katzj)
- Add Efika detection to getPPCMachine() (dwmw2)
- Update Romanian keyboard layout (#386861). (clumens)
- remove py-compile; we haven't used it for a long time (katzj)
- Run make in build section (#353751) (katzj)
- removed sr@Latn translation (kmilos)
- Remove obsolete translation (#332231). (clumens)

* Fri Oct 12 2007 Jeremy Katz <katzj@redhat.com> 0.210-1
- Translation updates
- Alpha support (Oliver Falk, #253824)
- Correct mapping for Serbian keyboard (msivak, #259101)
- Setup us+inet as the keyboard mapping for US keyboards so that we get 
  working multimedia keys.  

* Thu Jul 19 2007 Chris Lumens <clumens@redhat.com> 0.209-1
- Don't traceback on keyboard maps that we don't support (#246766).

* Mon Jun  4 2007 Jeremy Katz <katzj@redhat.com> - 0.208-2
- rebuild for new wireless-tools

* Thu May 24 2007 Jeremy Katz <katzj@redhat.com> - 0.208-1
- revert some of the unicode changes so that we're more sane (#241246, #241077)
- Fix Bulgarian phonetic keyboard layout (clumens)

* Mon May 21 2007 Jeremy Katz <katzj@redhat.com> - 0.207-1
- Fix so that stdout/stderr have a reasonable encoding (#240787)

* Wed May 16 2007 Chris Lumens <clumens@redhat.com> - 0.206-1
- Use the correct Bulgarian keyboard layout (#238345, #240087).
- Fix Pegasos platform detection (#237413).

* Thu Apr 26 2007 Jeremy Katz <katzj@redhat.com> - 0.205-1
- Fix tracebacks with unicode strings (#237956)

* Wed Apr 18 2007 Chris Lumens <clumens@redhat.com> - 0.204-1
- Fix PS3 platform detection (#236507).

* Thu Mar 15 2007 David Cantrell <dcantrell@redhat.com> - 0.203-2
- Remove 'Red Hat Linux' from the package description (#208444)

* Thu Mar  1 2007 Jeremy Katz <katzj@redhat.com> - 0.203-1
- Fix pSeries detection (Jerone Young, #229231)

* Wed Feb 28 2007 Chris Lumens <clumens@redhat.com> - 0.202-1
- Replace deprecated exceptions with real classes (#220802).

* Sat Jan 13 2007 Jesse Keating <jkeating@redhat.com> - 0.201-2
- rebuild in correct collection

* Fri Jan 12 2007 Chris Lumens <clumens@redhat.co> - 0.201-1
- Fix traceback.

* Thu Jan 11 2007 Paul Nasrat <pnasrat@redhat.com> - 0.200-1
- Add PS3 ppc machine type

* Wed Jan 10 2007 Paul Nasrat <pnasrat@redhat.com> - 0.199-1
- Fix Korean keyboard map (#212280)

* Tue Jan 09 2007 David Cantrell <dcantrell@redhat.com> - 0.198-1
- Conflicts with kbd < 1.12-21

* Tue Jan 09 2007 Paul Nasrat <pnasrat@redhat.com> - 0.197-1
- Fix Korean keyboard (#212280)

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.196-1
- fix build with new gettext
- simplify russian keyboard choices (clumens, #218264)
- build against python 2.5

* Thu Nov 30 2006 Paul Nasrat <pnasrat@redhat.com> - 0.195-1
- Add Maple support (#217145)

* Fri Oct 13 2006 Bill Nottingham <notting@redhat.com> - 0.194-1
- use valid charsets in po files (#210720)

* Wed Oct  4 2006 Harald Hoyer <harald@redhat.com> - 0.193-1
- fix to build ethtool on ia64

* Wed Oct  4 2006 Harald Hoyer <harald@redhat.com> - 0.191-1
- split iwlib functions from ethtool in iwlib module (bug #197954)

* Mon Oct  2 2006 Jeremy Katz <katzj@redhat.com> - 0.190-1
- rebuild for translations

* Wed Sep 06 2006 Chris Lumens <clumens@redhat.com> 0.188-3
- Remove pyxf86config requirement (#205019).

* Tue Aug 29 2006 Christopher Aillon <caillon@redhat.com> - 0.188-2
- Update BR to use the now split-out wireless-tools-devel package

* Tue Jul 25 2006 Harald Hoyer <harald@redhat.com> - 0.188-1
- correctly parse bool values in genClass.py

* Wed Jun 21 2006 Chris Lumens <clumens@redhat.com> 0.187-1
- Remove deprecated comps.py.
- Fix traceback when updating resolv.conf (#182395).

* Thu Mar 23 2006 Chris Lumens <clumens@redhat.com> 0.186-1 
- Remove deprecated files now in rhpl or firstboot.

* Thu Mar  2 2006 Jeremy Katz <katzj@redhat.com> - 0.185-1
- fix serbian keyboard (#182591)

* Wed Mar 01 2006 David Cantrell <dcantrell@redhat.com> 0.184-1
- Use ca(fr) without fr-legacy variant for Canadian French (#182007).

* Fri Feb 24 2006 Chris Lumens <clumens@redhat.com> 0.183-1
- Fix keyboard layout switching (#173267).

* Wed Feb 15 2006 David Cantrell <dcantrell@redhat.com> - 0.182-1
- setxkbmap corrections for loading X keymaps (#179845)

* Thu Dec 22 2005 Jeremy Katz <katzj@redhat.com> - 0.181-1
- Clean up spacing and use current widgets for exception dialog
- add serbian keyboard models (#175611)

* Wed Dec 21 2005 Chris Lumens <clumens@redhat.com> 0.180-1
- Deprecate rhpl.log.

* Tue Dec 13 2005 Chris Lumens <clumens@redhat.com> 0.179-1.1
- Change pl keymap to pl2.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Chris Lumens <clumens@redhat.com> 0.178-1
- Update keyboard model dict to match modular X (#173268).

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> - 0.177-1
- call setxkbmap by searching path instead of exact location since it moves 
  with modular X

* Tue Oct 11 2005 Chris Lumens <clumens@redhat.com> 0.176-1
- Make deprecated module warnings more useful.
- Move data files and ddcprobe to rhpxl.

* Mon Oct 10 2005 Chris Lumens <clumens@redhat.com> 0.175-2
- Remove rhpxl and firstboot requires.

* Fri Oct 07 2005 Chris Lumens <clumens@redhat.com> 0.175-1
- Move X-related chunks into rhpxl, replace with deprecation warnings.
- Fix rhpl requires.

* Tue Sep 20 2005 Jeremy Katz <katzj@redhat.com> - 0.174-1
- fix traceback with x86_64 x config

* Thu Sep 15 2005 Chris Lumens <clumens@redhat.com> 0.173-1
- Move firstboot_gui_window to firstboot.

* Mon Sep 12 2005 Jeremy Katz <katzj@redhat.com> - 0.172-1
- fix from Nalin for gratuitous iwlib api change (#168017)

* Mon Sep 12 2005 Jeremy Katz <katzj@redhat.com> - 0.171-1
- tweaks for new kudzu X driver model
- Move some of the anaconda X startup handling to rhpl for use in 
  firstboot (clumens)

* Fri Sep  9 2005 Bill Nottingham <notting@redhat.com> 0.170-1
- adapt to new kudzu X driver model, related cleanups

* Wed Jul 06 2005 Chris Lumens <clumens@redhat.com> 0.169-1
- Fix ppc64 requires. (katzj)
- Handle uncompressed .mo files as well.

* Thu Jun 30 2005 Chris Lumens <clumens@redhat.com> 0.168-1
- Use Python's gzip module instead of our own gzread for .mo files.

* Tue May 24 2005 Paul Nasrat <pnasrat@redhat.com> - 0.167-1
- Fix for ALPS specific settings

* Thu May 19 2005 Jeremy Katz <katzj@redhat.com> - 0.166-1
- Retranslate keyboard names each time so that it works with anaconda's 
  lang changing (#157733)

* Thu May 19 2005 Paul Nasrat <pnasrat@redhat.com> 0.165-1
- ALPS configuration (#155291)

* Mon May 16 2005 Chris Lumens <clumens@redhat.com> 0.164-1
- Remove directory name from dvorak so it'll show up in anaconda's
  lists (#157763, #157840).

* Mon May 16 2005 Chris Lumens <clumens@redhat.com> 0.163-1
- Change resolution sorting to match X's behavior (Jef Spaleta, #157596).
- Don't pad IP address information with unnecessary zeros (#157657).

* Thu May  5 2005 Jeremy Katz <katzj@redhat.com> - 0.162-1
- look up monitor in MonitorsDB if we can't probe horiz/vert

* Mon May  2 2005 Jeremy Katz <katzj@redhat.com> - 0.161-1
- Only default to fbdev X server on ppc64pseries, not all ppc (#149188)
- Set UseFBDev on ppc boxes using ati video cards (#149188)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 0.160-1
- don't build ethtool stuff on s390

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 0.159-1
- add some more weird X modes (sandmann AT redhat DOT com)
- fix gtk deprecation warnings (clumens)

* Thu Mar 31 2005 Harald Hoyer <harald@redhat.com> - 0.158-1
- fixed buffer overflow #151948

* Wed Mar  9 2005 Peter Jones <pjones@redhat.com> - 0.157-1
- get rid of "constructors" in favor of a Unit class and "units",
  which works like the old constructors.
- rework storage.Size.__str__ to be much cleaner
- make clamp/unclamp/shrink return self.

* Wed Mar  9 2005 Peter Jones <pjones@redhat.com> - 0.156-1
- added NonNegativeIntegerDescriptor
- changed storage.Size to allow for displaying 1GB as 1024MB

* Wed Mar 09 2005 Harald Hoyer <harald@redhat.com> - 0.155-1
- fixed segfault #150449 with s/strcpy/strncpy/ in ethtool

* Tue Mar  8 2005 Peter Jones <pjones@redhat.com> - 0.154-1
- add descriptors.py, implementing SimpleBoolDescriptor, BoolDescriptor,
  and TristateDescriptor classes.
- added storage.py, implementing a Size class useful for representing
  the size of disks or ram, and several utility functions such as Bytes(),
  KiloBytes, MegaBytes(), etc., which act as constructors.
- added genModule.py, which generates python modules on the fly, so
  you don't need to make a directory, __init__.py, etc just to
  do "from foo.bar import baz"

* Tue Jan 25 2005 Peter Jones <pjones@redhat.com> - 0.153-1
- add Russian unicode keyboard (#146009)
- revert glibc-kernheaders fix.
		
* Wed Jan 19 2005 Jeremy Katz <katzj@redhat.com> - 0.152-1
- fix build with new glibc-kernheaders (#145442)

* Wed Nov 17 2004 Jeremy Katz <katzj@redhat.com> - 0.151-1
- add patch from Jim Parsons to add executil.execWithCaptureErrorStatus as 
  needed by system-config-lvm

* Mon Nov 08 2004 Paul Nasrat <pnasrat@redhat.com> - 0.150-1
- Remove synaptics Requires

* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 0.149-1
- rebuild for python 2.4

* Wed Oct 13 2004 Paul Nasrat <pnasrat@redhat.com> - 0.148-1
- Indic keyboard fixups
- Multi-input synaptics 
- require synaptics
- Less verbose ddcprobe

* Thu Sep 30 2004 Harald Hoyer <harald@redhat.com> - 0.147-1
- let Conf.ConfModules use modprobe.conf name and format (bug 131952)
- use network script resolv.conf merger/changer (bug 132485)

* Fri Sep 24 2004 Jeremy Katz <katzj@redhat.com> 
- require python (#133462)

* Wed Sep 22 2004 Jeremy Katz <katzj@redhat.com> - 0.146-1
- add synaptics support (pnasrat)
- add arabic and indic keyboards (pnasrat)

* Fri Jun 18 2004 Jeremy Katz <katzj@redhat.com> - 0.145-1
- improved lib64 detection, rebuild with gcc 3.4

* Wed May  5 2004 Jeremy Katz <katzj@redhat.com> - 0.144-1
- open cd device with O_NONBLOCK so eject ioctl works (#122524)

* Tue Apr 20 2004 Brent Fox <bfox@redhat.com> 0.143-1
- Do not write out XkbRules line to config file, as it is unnecessary to hard
  code the rules file, which has a built in default which should always
  work. (#120858)

* Fri Apr 16 2004 Jeremy Katz <katzj@redhat.com> - 0.142-1
- more XFree86->xorg

* Thu Apr 15 2004 Jeremy Katz <katzj@redhat.com> - 0.141-1
- xserver.py: workaround libxf86config not writing out the monitor stuff 
  we tell it to (#120950)

* Wed Apr 14 2004 Jeremy Katz <katzj@redhat.com> - 0.140-1
- translate.py: one more try at string encoding madness (#119391)

* Tue Apr 13 2004 Jeremy Katz <katzj@redhat.com> - 0.139-1
- videocard.py: fixups for VESA handling on x86_64
- videocard.py, xserver.py: XFree86 -> Xorg changes

* Wed Mar 17 2004 Bill Nottingham <notting@redhat.com> 0.138-1
- mouse.py cleanups

* Tue Mar 16 2004 Bill Nottingham <notting@redhat.com> 0.135-1
- remove old default keymap when writing config (#116852)

* Tue Mar  9 2004 Brent Fox <bfox@redhat.com> 0.134-1
- user fr-latin9 for the X keymap too (bug #113672)

* Tue Mar  9 2004 Jeremy Katz <katzj@redhat.com> - 0.133-1
- use vesa for unknown cards on x86_64

* Fri Mar  5 2004 Brent Fox <bfox@redhat.com> 0.132-1
- use fr-latin9 instead of fr-latin0 (bug #113672)

* Thu Mar  4 2004 Jeremy Katz <katzj@redhat.com> - 0.131-1
- switch some default keyboard layouts (#117007)

* Thu Mar  4 2004 Brent Fox <bfox@redhat.com> 0.130-1
- strip out refresh rate data (bug #117327)

* Wed Mar  3 2004 Brent Fox <bfox@redhat.com> 0.129-1
- enable DRI extentions for all i386, x86_64, and ia64 systems (bug #115672)
- vmware doesn't do 24bpp (#117375)
- fix for savage + lcds (#117079)

* Thu Feb 26 2004 Brent Fox <bfox@redhat.com> 0.128-1
- add some hooks to xhwstate.py to get PCI bus ID info

* Fri Feb 20 2004 Brent Fox <bfox@redhat.com> 0.127-2
- correct a typo

* Fri Feb 20 2004 Brent Fox <bfox@redhat.com> 0.127-1
- changes to mouse handling in xhwstate.py

* Wed Feb 18 2004 Jeremy Katz <katzj@redhat.com> 0.126-1
- minor tweak for mouse stuff

* Fri Feb 13 2004 Brent Fox <bfox@redhat.com> 0.125.1-1
- use hu_qwerty for Hungarian (101 key) (bug #114629)

* Thu Jan 22 2004 Jeremy Katz <katzj@redhat.com> 0.124.1-1
- translate.py: minor tweaks

* Tue Jan 20 2004 Jeremy Katz <katzj@redhat.com> 0.124-1
- translate.py: return UTF-8 encoded strings (#113202) 

* Thu Jan  8 2004 Brent Fox <bfox@redhat.com> 0.123.1-1
- add an entry for Korean keyboards (bug #112024)

* Tue Jan  6 2004 Jeremy Katz <katzj@redhat.com> 
- mark keyboard model names as keyboard|name to make them differ 
  from language names (#84969)

* Tue Dec 16 2003 Jeremy Katz <katzj@redhat.com> 
- use EISA if name doesn't exist in ddc data (#112281)

* Fri Nov 14 2003 Jeremy Katz <katzj@redhat.com> 0.122.2-1
- more python2.3

* Sat Nov  8 2003 Jeremy Katz <katzj@redhat.com> 0.122.1-1
- more python 2.3 fixups

* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 0.122-1
- python 2.3

* Tue Oct 21 2003 Jeremy Katz <katzj@redhat.com> 0.121-1
- don't try to use 24bpp on old hardware (#105713)

* Thu Oct 16 2003 Brent Fox <bfox@redhat.com> 0.120-1
- mouse.py - add two entries for optical mice

* Thu Oct 16 2003 Jeremy Katz <katzj@redhat.com> 0.119-1
- keyboard_models.py: fix greek keyboard layout (#100773)

* Wed Oct 15 2003 Jeremy Katz <katzj@redhat.com> 0.118-1
- translate.py: assume UTF-8 if we can't figure out the encoding of a mofile

* Thu Oct  8 2003 Michael Fulbright <msf@redhat.com> 0.117-1
- xhwstate.py - dont write out video ram option to XF86Config

* Thu Oct  2 2003 Brent Fox <bfox@redhat.com> 0.116-1
- videocard.py: added pci busID functions 

* Tue Sep 30 2003 Jeremy Katz <katzj@redhat.com> 0.115-1
- mouse.py: add new API and make sane to use for translation

* Thu Sep 25 2003 Harald Hoyer <harald@redhat.de> 0.114-1
- preserve comments in modules.conf #76640

* Tue Sep 23 2003 Michael Fulbright <msf@redhat.com>
- fix bug dealing with determining video modes supported by a monitor

* Mon Sep  8 2003 Jeremy Katz <katzj@redhat.com> 
- use RPM_OPT_FLAGS (#103970)

* Thu Sep 04 2003 Harald Hoyer <harald@redhat.de> 0.112-1
- fixed ConfPAP.getfields()

* Thu Sep 04 2003 Michael Fulbright <msf@redhat.com> 0.111-1
- fixes for bugzilla #103353

* Tue Sep 02 2003 Michael Fulbright <msf@redhat.com> 0.111-1
- fixes to X setup code

* Fri Aug 29 2003 Harald Hoyer <harald@redhat.de> 0.110-1
- removed memory leak

* Wed Jul 16 2003 Jeremy Katz <katzj@redhat.com> 0.110-1
- add an interface for adding packages to groups

* Mon Jul 14 2003 Jeremy Katz <katzj@redhat.com> 0.109-1
- multilib on ia64

* Wed Jul 09 2003 Harald Hoyer <harald@redhat.de> 0.108-3
- rebuilt with all files updated from cvs

* Tue Jul  8 2003 Jeremy Katz <katzj@redhat.com> 0.108-1
- comps.py: preserve xml doc/nodes
- translate.py: make it so we can use translations from update disks in 
  anaconda

* Thu Jun 12 2003 Brent Fox <bfox@redhat.com> 0.107-1
- add a get_xconfig() method to xhwstate.py

* Tue Jun 10 2003 Harald Hoyer <harald@redhat.de> 0.106-1
- better regexp in Conf.py
- strip filename from subject

* Fri Jun  6 2003 Jeremy Katz <katzj@redhat.com> 0.105-1
- more biarch fun

* Wed Jun  4 2003 Jeremy Katz <katzj@redhat.com> 0.104-1
- add ppc64[ip]series

* Wed Jun  4 2003 Jeremy Katz <katzj@redhat.com> 0.103.1-1
- arch.py tweaks

* Fri May 30 2003 Jeremy Katz <katzj@redhat.com> 0.103-1
- comps.py extensions for biarch

* Fri May 23 2003 Jeremy Katz <katzj@redhat.com> 0.102.1-1
- fix tyop

* Fri May 23 2003 Jeremy Katz <katzj@redhat.com> 0.102-1
- add arch.py

* Wed May 21 2003 Harald Hoyer <harald@redhat.de> 0.101.1-1
- strip quotes from PAP/CHAP server also
- Conf.py, cope with lines at the end of the file, that have no newline
- speedup some things

* Wed May 07 2003 Michael Fulbright <msf@redhat.com> 0.100.1-1
- fixed simpleconfig.py and how it uppercases keys

* Tue Apr 29 2003 Harald Hoyer <harald@redhat.com> 0.99.1-1
- genClass and ethtool updates

* Thu Apr 24 2003 Brent Fox <bfox@redhat.com> 0.98.1-2
- strip an invalid char from monitor name (bug #87588)

* Wed Apr 23 2003 Jeremy Katz <katzj@redhat.com> 0.98.1-1
- revert broken part of pseries fb change

* Mon Apr 21 2003 Jeremy Katz <katzj@redhat.com> 0.98-1
- handle headless case better

* Fri Apr 18 2003 Jeremy Katz <katzj@redhat.com> 0.97-1
- fixes so that framebuffer can work for use on ppc machines

* Thu Apr  3 2003 Brent Fox <bfox@redhat.com> 0.96-2
- update the list of dri drivers from mharris

* Thu Apr  3 2003 Brent Fox <bfox@redhat.com> 0.96-1
- add ati and i810 to dri supported list in xhwstate.py

* Wed Apr  2 2003 Brent Fox <bfox@redhat.com> 0.95-1
- allow dialog size to be passed into firstboot_gui_window

* Thu Feb 27 2003 Bill Nottingham <notting@redhat.com> 0.94-1
- make py_bind_textdomain_codeset not segfault on ia64 (#85334)

* Mon Feb 24 2003 Jeremy Katz <katzj@redhat.com> 0.93-1
- mouse.py (mouseWindow): try to ensure we have a locale that 
  we can do linedrawing chars for (#84908)

* Wed Feb 12 2003 Brent Fox <bfox@redhat.com> 0.92-1
- add grp_led:scroll to all lines with XkbOptions (bug #82096)

* Tue Feb 11 2003 Brent Fox <bfox@redhat.com> 0.91-1
- convert all toggles to grp:shift_toggle (bug #79287)

* Fri Feb  7 2003 Brent Fox <bfox@redhat.com> 0.90-1
- add grp_led:scroll to all Russian keyboards

* Fri Feb  7 2003 Brent Fox <bfox@redhat.com> 0.89-1
- add translate.textdomain('rhpl') to fix bug #69760

* Thu Feb  6 2003 Matt Wilson <msw@redhat.com> 0.88-1
- only reset the mouse if you have to

* Thu Feb  6 2003 Brent Fox <bfox@redhat.com> 0.87-1
- load additional us keymap for all ru keyboards in keyboard_models.py
- make sure the kbd option gets set in keyboard.py

* Thu Feb  6 2003 Brent Fox <bfox@redhat.com> 0.86-1
- use sv-latin1 for swedish keyboards (bug #80508)

* Wed Feb  5 2003 Matt Wilson <msw@redhat.com> 0.85-1
- autodetect ps/2 wheel mice (#81902)

* Wed Feb  5 2003 Brent Fox <bfox@redhat.com> 0.84-1
- if there are no display Modes in the XF86Config file, create one and default to 800x600 (bug #83314)

* Tue Feb 04 2003 Harald Hoyer <harald@redhat.de> 0.83-1
- ConfPAP fix for quotation

* Fri Jan 31 2003 Jeremy Katz <katzj@redhat.com> 0.81-2
- fix typo

* Fri Jan 31 2003 Adrian Likins <alikins@redhat.com>
- added get_ipaddr, get_netmask, get_broadcast
  to ethtool module

* Fri Jan 31 2003 Harald Hoyer <harald@redhat.de>
- added some BuildRequires

* Thu Jan 30 2003 Jeremy Katz <katzj@redhat.com> 0.80-1
- default non-i386 arches to 8 megs of videoram

* Wed Jan 22 2003 Brent Fox <bfox@redhat.com> 0.79-1
- add us keymap and XkbOptions to non-latin keymaps in keyboard_models.py
- change keyboard.py to handle the XkbOptions field

* Mon Jan 20 2003 Michael Fulbright <msf@redhat.com> 0.78-1
- improved code for LCD guessing

* Fri Jan 17 2003 Michael Fulbright <msf@redhat.com> 0.77-1
- added code to xserver.py to guess LCD size using guesslcd.py

* Fri Jan 17 2003 Brent Fox <bfox@redhat.com> 0.76-1
- changes to firstbootGuiWindow.py for new firstboot look

* Tue Jan 14 2003 Michal Fulbright <msf@redhat.com> 0.75-1
- fix xserver.py to include keyboard import

* Fri Jan 10 2003 Brent Fox <bfox@redhat.com> 0.74-2
- change se-latin1 kbd to se-fi-lat6 according to bug #80508

* Fri Jan  3 2003 Brent Fox <bfox@redhat.com> 0.74-1
- default to pc105 for most keyboards

* Thu Jan  2 2003 Jeremy Katz <katzj@redhat.com> 0.73-3
- make the translate.py change less noisy

* Thu Jan  2 2003 Jeremy Katz <katzj@redhat.com> 0.73-2
- typo fix

* Wed Jan  1 2003 Jeremy Katz <katzj@redhat.com> 0.73-1
- discid.py: add readFromBuffer

* Sun Dec 29 2002 Jeremy Katz <katzj@redhat.com> 
- translate.py: if we fail, at least gracefully fall back instead of 
  causing a traceback (#76104)

* Thu Dec 19 2002 Harald Hoyer <harald@redhat.de> 0.72-1
- added exception.py 

* Tue Dec 17 2002 Jeremy Katz <katzj@redhat.com> 0.71-2
- fix silly typo

* Tue Dec 17 2002 Jeremy Katz <katzj@redhat.com> 0.71-1
- simpleconfig.py: gracefully handle non-existent config files

* Mon Dec 16 2002 Harald Hoyer <harald@redhat.de> 0.70-1
- _setParent() in GenClass::__setitem__

* Fri Dec 13 2002 Jeremy Katz <katzj@redhat.com> 0.69-1
- only probe for the mouse once to fix mouse probing problems
- make keyboard names more consistent (#79354)

* Thu Dec 12 2002 Harald Hoyer <harald@redhat.de> 0.68-1
- genClass: slicing of anonymous lists
- executil: dup2 more output redirectors

* Tue Nov 26 2002 Michael Fulbright <msf@redhat.com> 0.67-1
- Fixed issue related to not defaulting to sane monitor values if monitor
  was not probed.

* Tue Nov 26 2002 Phil Knirsch <pknirsch@redhat.com> 0.66-1
- Fixed -fpic handling for s390 and s390x.

* Thu Nov 21 2002 Michael Fulbright <msf@redhat.com> 0.65-1
- added some code to handle the no mouse setup better

* Thu Nov 21 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not require pyxf86config for mainframe

* Tue Nov 19 2002 Michael Fulbright <msf@redhat.com> 0.64-1
- Added new xserver.py which has code to help get X up and running from scratch

* Tue Nov 19 2002 Jeremy Katz <katzj@redhat.com> 0.63-2
- rebuild for all arches

* Fri Nov 15 2002 Brent Fox <bfox@redhat.com> 0.63-1
- Added Latin American (la-latin1) keyboard

* Thu Nov 14 2002 Harald Hoyer <harald@redhat.de> 0.62-1
- removed Alchemist dependency from genClass
- executil extended

* Tue Nov 12 2002 Michael Fulbright <msf@redhat.com> 0.61-1
- big changes as we moved alot of code from redhat-config-xfree86 into xhwstate.py

* Tue Nov  5 2002 Jeremy Katz <katzj@redhat.com> 0.59-1
- access Cards database in /usr/share/hwdata instead of 
  /usr/X11R6/lib/X11 (#73899)
- excludearch x86_64 until python is fixed

* Fri Nov  1 2002 Jeremy Katz <katzj@redhat.com> 0.58-1	
- add macedonian keyboard (#76902)
- find loadkeys for anaconda (#75329)

* Thu Oct 31 2002 Brent Fox <bfox@redhat.com> 0.57-1
- Mark keyboard names for translations

* Mon Oct 21 2002 Brent Fox <bfox@redhat.com> 0.56-1
- Use cz_qwerty keymap for Czech qwerty keyboards

* Thu Oct 10 2002 Jeremy Katz <katzj@redhat.com> 0.55-2
- rebuild so that we actually get object files for the correct architectures

* Wed Oct  9 2002 Dan Walsh <dwalsh@redhat.de> 0.55-1
- removed chmod from ConfSMB.py file protection should remain the same

* Tue Oct  8 2002 Harald Hoyer <harald@redhat.de> 0.54-1
- removed fd/socket leaking

* Tue Oct 08 2002 Phil Knirsch <pknirsch@redhat.com> 0.53-2
- Integreated Karsten Hopp's 64bit bigendian patch for s390x.

* Fri Oct  4 2002 Brent Fox <bfox@redhat.com> 0.53-1
- Allow window icon to be passed into stand_alone in firstboot_gui_window.py

* Thu Oct  3 2002 Jeremy Katz <katzj@redhat.com> 0.52-2
- fixup installation into %%{_libdir}/python2.2/

* Thu Oct  3 2002 Jeremy Katz <katzj@redhat.com> 0.52-1
- iconvmodule.c: PyObject_asReadBuffer() expects *int while iconv() 
  expects size_t.

* Thu Aug 29 2002 Jeremy Katz <katzj@redhat.com> 0.51-1
- src/keyboard_models.py: fix romanian console keymap (#72952)

* Wed Aug 28 2002 Jeremy Katz <katzj@redhat.com> 0.50-1
- diskutil.py: update /etc/mtab

* Fri Aug 23 2002 Michael Fulbright <msf@redhat.com> 0.49-1
- videocard.py: Use unsupported VGA compatible card entry if card unknown

* Thu Aug 22 2002 Brent Fox <bfox@redhat.com> 0.48-1
- translate.py: add ability to set codeset for textdomains not pulled in by us

* Thu Aug 22 2002 Brent Fox <bfox@redhat.com> 0.47-1
- fix another typo in translate.py

* Thu Aug 22 2002 Jeremy Katz <katzj@redhat.com> 0.46-1
- fix a typo in translate.py

* Thu Aug 22 2002 Jeremy Katz <katzj@redhat.com> 0.45-1
- minor mouse fixups (#70289, #71893)

* Wed Aug 21 2002 Michael Fulbright <msf@redhat.com> 0.44-1
- added sanity check to ddcprobe'd range values

* Tue Aug 20 2002 Harald Hoyer <harald@redhat.de> 0.43-1
- fixed genClass.py:toContext()
- ValueError -> TypeError in checkType

* Fri Aug 16 2002 Brent Fox <bfox@redhat.com> 0.42-1
- Mark window title for translations in firstboot_gui_window

* Fri Aug 16 2002 Jeremy Katz <katzj@redhat.com> 0.41-1
- translate.py fixes
- "None - None" is back, but as "No mouse"

* Thu Aug 15 2002 Jeremy Katz <katzj@redhat.com> 0.40-1
- comps.py: handle translated category names

* Wed Aug 14 2002 Harald Hoyer <harald@redhat.de>
- added iwconfig-support to ethtool

* Wed Aug 14 2002 Brent Fox <bfox@redhat.com> 0.37-1
- Call destroy() when a firstboot window exits

* Mon Aug 12 2002 Jeremy Katz <katzj@redhat.com> 0.36-1
- add generic wheel mouse types
- add bad hack to handle packages which should only be installed 
  if another package is installed

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.35-1
- Create US International keymap line for bug 71105

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.34-2
- Fix typo that I made with the last build

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.34-1
- Fix Brazilian abnt2 keyboard map for bug 70351

* Tue Aug  6 2002 Michael Fulbright <msf@redhat.com>
- added sanity checks for sync rates

* Fri Aug  2 2002 Jeremy Katz <katzj@redhat.com>
- keyboard_models.py: be-latin2 isn't a valid keymap

* Wed Jul 31 2002 Jeremy Katz <katzj@redhat.com> 0.32-1
- add losetup, unlosetup, and getUnusedLoop to diskutil

* Tue Jul 30 2002 Brent Fox <bfox@redhat.com> 0.31-1
- remove some dead code
- make the font big for firstboot_gui_window titles

* Thu Jul 25 2002 Jeremy Katz <katzj@redhat.com> 0.30-1
- mouse.py: don't enable emulate three buttons on the fly (#68129)

* Thu Jul 25 2002 Jeremy Katz <katzj@redhat.com> 0.29-1
- translate.py: set up default langs based on environment

* Wed Jul 24 2002 Jonathan Blandford  <jrb@redhat.com> 0.28-1
* add GenericError.py

* Wed Jul 24 2002 Jeremy Katz <katzj@redhat.com> 0.27-2
- actually install _diskutil.so

* Wed Jul 24 2002 Jeremy Katz <katzj@redhat.com> 0.27-1
- diskutil.py, diskutil.c: add some simple disk utility methods (mount, 
  umount, sync, ejectCdrom)

* Mon Jul 22 2002 Jeremy Katz <katzj@redhat.com> 0.26-1
- comps.py: add support for reading group hierarchy

* Thu Jul 17 2002 Brent Fox <bfox@redhat.com> 0.25-1
- Make firstboot windows use GtkDialog instead of GtkWindow

* Wed Jul 17 2002 Brent Fox <bfox@redhat.com> 0.24-3
- Change Poland keyboard to Polish.  Bug #68520

* Wed Jul 17 2002 Michael Fulbright <msf@redhat.com> 0.24-2
- minor typo fix

* Wed Jul 17 2002 Michael Fulbright <msf@redhat.com> 0.24-1
- executil.py: add getfd() function

* Tue Jul 16 2002 Jeremy Katz <katzj@redhat.com> 0.23-1
- comps.py: add metapkg support

* Tue Jul 16 2002 Brent Fox <bfox@redhat.com> 0.22-2
- Call loadkeys if the binary exists when changing keymaps

* Mon Jul 15 2002 Jeremy Katz <katzj@redhat.com> 0.21-1
- fix jp106 entry in keyboard_models
- add method to get list of supported keyboard maps

* Sat Jul 13 2002 Brent Fox <bfox@redhat.com> 0.20-1
- Small change in firstboot_gui_window.py to center popup windows

* Wed Jul 10 2002 Brent Fox <bfox@redhat.com> 0.19-1
- Added a Greek keyboard to keyboard_models.py

* Wed Jul 10 2002 Alexander Larsson <alexl@redhat.com> 0.18-1
- Fixed bug in monitor resoultion support code

* Mon Jul  1 2002 Harald Hoyer <harald@redhat.de> 0.16-1
- updated Conf*.py
- updated genClass
- added ethtool

* Fri Jun 28 2002 Jeremy Katz <katzj@redhat.com> 0.15-1
- comps.py: use libxml2 for xml parsing instead of expat

* Fri Jun 28 2002 Jeremy Katz <katzj@redhat.com> 0.14-1
- only setxkbmap if $DISPLAY is set

* Thu Jun 27 2002 Jeremy Katz <katzj@redhat.com> 0.13-1
- add parser for new comps file

* Wed Jun 26 2002 Michael Fulbright <msf@redhat.com> 0.12-1
- Fix bug of uninitialized data in Mouse class

* Tue Jun 25 2002 Brent Fox <bfox@redhat.com> 0.11-3
- Allow a window title to be passed in

* Wed Jun 19 2002 Brent Fox <bfox@redhat.com> 0.9-4
- Fixed line for German keyboards in keyboard_models.py

* Tue Jun 18 2002 Brent Fox <bfox@redhat.com> 0.9-3
- Remove cancel button from firstboot_gui_window

* Tue Jun 18 2002 Brent Fox <bfox@redhat.com> 0.9-2
- Provide a way to pass keymap name back to firstboot
- Fix error in Slovakian keymap line in keyboard_models.py

* Wed Jun 12 2002 Jeremy Katz <katzj@redhat.com>
- use cz-lat2 for Czechoslovakian keybaord map (#66354)

* Tue Jun 04 2002 Michael Fulbright <msf@redhat.com>
- fixed bug referencing ddcDevice and videoram in card.

* Tue May 28 2002 Jeremy Katz <katzj@redhat.com>
- removed kbd.py, added keyboard.py

* Fri May 24 2002 Michael Fulbright <msf@redhat.com>
- Added kbd.py

* Thu May 23 2002 Alex Larsson <alexl@redhat.com>
- Added /usr/share/rhpl to files list

* Thu May 23 2002 Michael Fulbright <msf@redhat.com>
- added log.py, videocard.py, mouse.py, monitor.py, simpleconfig.py

* Wed May 22 2002 Jeremy Katz <katzj@redhat.com>
- Initial build.


