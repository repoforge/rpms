# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el5:%define _without_glide3 1}

%{?el4:%define _without_glide3 1}
%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_glide3 1}
%{?el3:%define _without_modxorg 1}

#define rcver cvs
%define targets %{?!_without_mame:mame} %{?!_without_mess:mess}

%{!?_without_opengl:%define opengl 1}
# Glide3 is only available on x86 and x86_64 (as of Oct 2005 - 0.100)
%ifarch %{ix86} x86_64
%{!?_without_glide3:%define glide3 1}
%endif

Summary: The X Multi Arcade Machine Emulator
Name: xmame
Version: 0.106
Release: 1%{?rcver:.%{rcver}}
Source0: http://x.mame.net/download/xmame-%{version}.tar.bz2
# http://cheat.retrogames.com/ 0.106 - 14/05/2006
Source20: http://cheat.retrogames.com/cheat.zip
# http://www.mameworld.net/highscore/ 0.105 - 10/04/2006
Source21: http://www.mameworld.net/highscore/uhsdat0105.zip
# http://www.arcade-history.com/ 1.06q - 26/05/2006
Source22: http://www.arcade-history.com/download/history1_06q.zip
# http://www.mameworld.net/mameinfo/ 0.106 - 14/05/2006
Source23: http://www.mameworld.net/mameinfo/update/Mameinfo0106.zip
# http://www.mameworld.net/catlist/ 0.99u2 - 12/09/2005
Source30: http://www.mameworld.net/catlist/files/catver.zip
Patch0: xmame-0.100-libgl.patch
License: MAME
URL: http://x.mame.net/
Group: Applications/Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: %{name}-x11 <= 0.87
Obsoletes: %{name}-xgl <= 0.87
BuildRequires: unzip, p7zip, zlib-devel, expat-devel
%{!?_without_modxorg:BuildRequires: libXt-devel, libXv-devel, libXext-devel}
%{!?_without_modxorg:%{?opengl:BuildRequires: mesa-libGLU-devel, libjpeg-devel}}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_without_modxorg:%{?opengl:BuildRequires: Mesa-devel, libjpeg-devel}}
%{?glide3:BuildRequires: Glide3-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
%ifarch %{ix86} x86_64
%{!?_without_mips3drc:BuildRequires: nasm >= 0.98}
%endif

%description
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

This version has been compiled with X11, XV, OpenGL and Glide3 displays.

Available rpmbuild rebuild options :
--without mame mess mips3drc ppcdrc effmmx opengl glide3
          alsa esound arts lirc opts quietbuild
--with dga


%package -n xmess
Summary: The Multi Emulator Super System
Group: Applications/Emulators
Obsoletes: xmess-x11 <= 0.87
Obsoletes: xmess-xgl <= 0.87

%description -n xmess
This is the *nix port of MESS. MESS is a free emulator which emulates a
large variety of different systems, including old Atari, Apple, BBC,
Commodore, MSX, ZX Spectrum computers. For full list of supported systems
see http://www.mess.org/.


%prep
%setup
%patch0 -p1 -b .libgl
# Cleanup CVS stuff
find . -type d -name CVS | xargs %{__rm} -rf


%build
%{__rm} -f makefile Makefile; %{__cp} -ap makefile.unix Makefile

# For CVS snapshots, these are empty instead of symlinks, so fix that
for dir in contrib doc; do
    if test -d ${dir}; then
        %{__rm} -rf ${dir}
        %{__ln_s} src/unix/${dir}
    fi
done

# Comment out the defaults, to enable overriding with the env variables
%{__perl} -pi -e 's/^CFLAGS/# CFLAGS/g' Makefile
%{__perl} -pi -e 's/^LD/# LD/g' Makefile
%{__perl} -pi -e 's/^MY_CPU/# MY_CPU/g' Makefile

# Replace lib with lib64 when required
%{__perl} -pi -e 's|/usr/X11R6/lib$|/usr/X11R6/%{_lib}|g' Makefile

# Use glibc libm
%{__perl} -pi -e 's/^SEPARATE_LIBM/# SEPARATE_LIBM/g' Makefile

# Disable stripping on install, to get proper debuginfo
%{__perl} -pi -e 's/^ASM_STRIP/ASM_STRIP = true/g' Makefile

# Make the package build verbose by default (to see opts etc.)
%{?_without_quietbuild: %{__perl} -pi -e 's/^QUIET/# QUIET/g' src/unix/unix.mak}

# The default, if not overwritten below
export PREFIX=%{_prefix}
export CFLAGS="%{optflags} -fno-merge-constants"
export LD='$(CC) -Wl'
export JOY_STANDARD=1
export JOY_PAD=1
export LIGHTGUN_ABS_EVENT=1
%{!?_without_alsa:   export SOUND_ALSA=1}
%{!?_without_esound: export SOUND_ESOUND=1}
%{!?_without_arts:   export SOUND_ARTS_SMOTEK=1}
%{!?_without_arts:   export SOUND_ARTS_TEIRA=1}
%{!?_without_lirc:   export LIRC=1}
%{?_with_dga:        export X11_DGA=1}

# Optimization flags, CPU type and defaults for the makefile
%ifarch %{ix86}
    export MY_CPU="i386"
    %{!?_without_opts: export CFLAGS="-O3 -g -pipe -march=i386 -mtune=pentium4 -Wall -fno-merge-constants"}
    %{!?_without_mips3drc: export X86_MIPS3_DRC=1}
    %{!?_without_ppcdrc:   export X86_PPC_DRC=1}
    %{!?_without_effmmx:   export EFFECT_MMX_ASM=1}
%endif

%ifarch i686
    %{!?_without_opts: export CFLAGS="-O3 -g -pipe -march=pentium4 -msse2 -mfpmath=sse -Wall -fno-merge-constants"}
%endif

%ifarch athlon
    %{!?_without_opts: export CFLAGS="-O3 -g -pipe -march=athlon-4 -msse2 -mfpmath=sse -Wall -fno-merge-constants"}
%endif

%ifarch ppc
    export MY_CPU="risc"
    export LD='$(CC) -Wl,--relax'
    %{!?_without_opts: export CFLAGS="-O3 -g -pipe -Wall -mlongcall -fno-merge-constants"}
%endif

%ifarch x86_64
    export MY_CPU="amd64"
    %{!?_without_opts: export CFLAGS="-O3 -g -pipe -march=k8 -m64 -Wall -fno-merge-constants"}
    # If you enable X86_MIPS3_DRC, you'll get "Segmentation fault" (0.88)
    #{!?_without_mips3drc: export X86_MIPS3_DRC=1}
    # If you enable EFFECT_MMX_ASM, you'll get "Illegal instruction" for
    # the 6tap2x effect (0.88)
    #{!?_without_effmmx:   export EFFECT_MMX_ASM=1}
%endif

# Now, do all the building (this is long!)
for target in %{targets}; do
    %{__make} %{?_smp_mflags} \
        %{?opengl:X11_OPENGL=1} %{?glide3:X11_GLIDE=1} TARGET=${target}
done


%install
%{__rm} -rf %{buildroot} _docs _datfiles _tmp

# Prepare all the extra .dat files
%{__mkdir} _datfiles _tmp
for file in %{SOURCE20} %{SOURCE21} %{SOURCE22}; do
    %{__unzip} -o -d _datfiles/ ${file}
done
for file in %{SOURCE23}; do
    %{__unzip} -o -d _tmp ${file}
    7za x -o_datfiles/ _tmp/*.exe
done

for target in %{targets}; do
    %{__make} install-man \
        INSTALL_USER=`id -un` \
        INSTALL_GROUP=`id -gn` \
        MANDIR=%{buildroot}%{_mandir}/man6 \
        TARGET=${target}
done

%{__mkdir_p} %{buildroot}%{_bindir}
for target in %{targets}; do
    %{__install} -p -m 0755 x${target}.x11 %{buildroot}%{_bindir}/x${target}
done
%{?!_without_mame: %{__install} -p -m 0755 chdman romcmp xml2info %{buildroot}%{_bindir}/}

# We don't want all the docs
%{__mkdir_p} _docs/{xmame/html,xmess}
pushd src/unix/doc
    %{__cp} -ap {*.html,*.css,img} ../../../_docs/xmame/html/
    %{__cp} -ap changes.* dga2.txt multiplayer-readme.txt \
        xmame-doc.txt xmamerc.dist mame/* ../../../_docs/xmame/
    %{__cp} -ap xmessrc.dist mess/* ../../../_docs/xmess/
popd

# XMAME specific
%if %{?_without_mame:0}%{!?_without_mame:1}
# Add all directories
%{__mkdir_p} %{buildroot}%{_datadir}/xmame/{artwork,roms,samples,snap}
# The extra dat files
%{__install} -p -m 0664 _datfiles/*.dat %{buildroot}%{_datadir}/xmame/
# Install the OpenGL cabinets
%{__cp} -ap src/unix/cab %{buildroot}%{_datadir}/xmame/
# Uncompress catver.ini (will be in the docs)
%{__unzip} -o -d _docs/ %{SOURCE30}

%endif

# XMESS specific
%if %{?_without_mess:0}%{!?_without_mess:1}
# Add all directories
%{__mkdir_p} %{buildroot}%{_datadir}/xmess/{artwork,bios,crc,samples,snap,software}
%endif


%clean
%{__rm} -rf %{buildroot}


%if %{?_without_mame:0}%{!?_without_mame:1}
%files
%defattr(-, root, root, 0755)
%doc README _docs/xmame/* contrib/tools/mame-cd
%doc _docs/catver.ini
%{_bindir}/chdman
%{_bindir}/romcmp
%if 0%{?_with_dga:1}
%attr(6755, root, games) %{_bindir}/xmame
%else
%attr(2755, root, games) %{_bindir}/xmame
%endif
%{_bindir}/xml2info
%dir %attr(2775, root, games) %{_datadir}/xmame/
%dir %attr(2775, root, games) %{_datadir}/xmame/artwork/
%attr(-, root, root) %{_datadir}/xmame/cab/
%dir %attr(2775, root, games) %{_datadir}/xmame/roms/
%dir %attr(2775, root, games) %{_datadir}/xmame/samples/
%dir %attr(2775, root, games) %{_datadir}/xmame/snap/
%{_datadir}/xmame/*.dat
%{_mandir}/man6/xmame.6*
%endif

%if %{?_without_mess:0}%{!?_without_mess:1}
%files -n xmess
%defattr(-, root, root, 0755)
%doc README _docs/xmess/*
%if 0%{?_with_dga:1}
%attr(6755, root, games) %{_bindir}/xmess
%else
%attr(2755, root, games) %{_bindir}/xmess
%endif
%dir %attr(2775, root, games) %{_datadir}/xmess/
%dir %attr(2775, root, games) %{_datadir}/xmess/artwork/
%dir %attr(2775, root, games) %{_datadir}/xmess/bios/
%dir %attr(2775, root, games) %{_datadir}/xmess/crc/
%dir %attr(2775, root, games) %{_datadir}/xmess/samples/
%dir %attr(2775, root, games) %{_datadir}/xmess/snap/
%dir %attr(2775, root, games) %{_datadir}/xmess/software/
%{_mandir}/man6/xmess.6.*
%endif


%changelog
* Mon May 29 2006 Matthias Saou <http://freshrpms.net/> 0.106-1
- Update to 0.106.
- Update all related files.
- Fix mameinfo.dat inclusion again, which is now an exe/7zip file in a zip.

* Tue Apr 18 2006 Matthias Saou <http://freshrpms.net/> 0.105-1
- Update to 0.105.
- Update all related files.
- Fix mameinfo.dat inclusion, which is now an exe/7zip file.

* Fri Mar 24 2006 Mike Crawford <mike@tuxnami.org> 0.104-2
- Added DGA build conditional.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.104-2
- Release bump to drop the disttag number in FC5 build.

* Fri Feb 17 2006 Matthias Saou <http://freshrpms.net/> 0.104-1
- Update to 1.104.

* Tue Jan 17 2006 Matthias Saou <http://freshrpms.net/> 0.103-1
- Update to 0.103.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.102-2
- Add modular xorg build conditional.

* Sun Nov 27 2005 Matthias Saou <http://freshrpms.net/> 0.102-1
- Update to 0.102.

* Tue Oct 25 2005 Matthias Saou <http://freshrpms.net/> 0.101-1
- Update to 0.101.
- Include fix for MESS keyboard input.

* Fri Oct 14 2005 Matthias Saou <http://freshrpms.net/> 0.100-2
- Update Mameinfo0100u3.zip and history1_04a.zip.
- Disable Glide3 on non x86/x86_64 archs to fix ppc build.

* Mon Sep 26 2005 Matthias Saou <http://freshrpms.net/> 0.100-1
- Update to 0.100.
- Remove explicit stripping disabling, since the default is to not strip now.
- Enable LIGHTGUN_ABS_EVENT.
- Override default LD (remove ,-s) to try and get real debuginfo at last...
- Include patch to change dlopen of libGL.so to libGL.so.1 (and libGLU too).

* Tue Aug 16 2005 Matthias Saou <http://freshrpms.net/> 0.99-1
- Update to 0.99 (final).
- Enable Glide3 for non-x86 archs again, since Hans has fixed it in Extras.

* Tue Jul 19 2005 Matthias Saou <http://freshrpms.net/> 0.98-0.1.cvs
- Update to 0.98 CVS snapshot.

* Tue Jun 14 2005 Matthias Saou <http://freshrpms.net/> 0.97-2
- Update to 0.97 (final).

* Mon Jun  6 2005 Matthias Saou <http://freshrpms.net/> 0.97-1
- Update to 0.97 (CVS).
- Enable X86_PPC_DRC by default for i386.
- Replace -mcpu with -mtune for i386.

* Wed May 11 2005 Matthias Saou <http://freshrpms.net/> 0.96-1
- Update to 0.96.

* Wed Mar 30 2005 Matthias Saou <http://freshrpms.net/> 0.95-1
- Update to 0.95.

* Wed Mar 16 2005 Matthias Saou <http://freshrpms.net/> 0.94-1
- Update to 0.94.
- Completely remove asm68000, it's now totally unmaintained and broken.
- Include 64bit fixes for seibuspi and wecleman by F.J. McCloud.
- Add Mads Villadsen's proposed lirc support.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 0.92-1
- Remove wrong -march for powerpc.
- Add LDFLAGS override for ppc to fix YDL4 build, thanks to Stig Sørensen.

* Thu Feb 24 2005 Matthias Saou <http://freshrpms.net/> 0.92-1
- Update to 0.92.
- Remove EXPAT Makefile change, the default is to use external lib now.
- Change ASM_STRIP to true, further attempt to get a real debuginfo package.

* Wed Jan 19 2005 Matthias Saou <http://freshrpms.net/> 0.90-1
- Update to 0.90.

* Thu Dec  9 2004 Matthias Saou <http://freshrpms.net/> 0.89-1
- Update to 0.89 final.
- Remove no longer needed libGL patch.

* Fri Nov 12 2004 Matthias Saou <http://freshrpms.net/> 0.88-1
- Update to 0.88 final.
- Disable stripping to get proper debuginfo packages... nope :-/

* Mon Nov  8 2004 Matthias Saou <http://freshrpms.net/> 0.88-0.cvs.1
- Remove CVS dirs from the source.
- Add libgl patch to change .so names so that devel packages aren't required
  at runtime.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 0.88-0.cvs.1
- Update to current CVS, all my bugs are fixed!
- Release as 0.88 cvs.

* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 0.87cvs-3
- Update all related files for 0.88.
- This is still versionned 0.87cvs, but it has 0.88 core.
- Disable EFFECT_MMX_ASM for x86_64, it fails too.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 0.87cvs-2
- Disable X86_ASM_68000 on x86_64, it bombs out otherwise.
- Disable X86_MIPS3_DRC on x86_64, it segfaults otherwise.
- Replace invalid "3dfx" macro name with "glide3".

* Sun Oct 24 2004 Matthias Saou <http://freshrpms.net/> 0.87cvs-1
- Removed specific sparc opts, please report if broken.
- Removed xgl target, as the OpenGL support is now built in the x11 one.
- Moved the main mame/mess binary into the main pakage, remove wrapper.
- Reworked gcc options, added some for i686 and athlon rebuilds.
- Renamed mmxasm build option to effmmx to be more explicit.
- Disable SDL build for now, as this way, we only have one pakage left!
- Removed x11 DGA, does anyone use that anymore?
- Added Glide3 support to the x11 target.
- Added -fno-merge-constants cflag to workaround unsorted coinage errors.

* Sun Oct  3 2004 Matthias Saou <http://freshrpms.net/> 0.87-1
- Update to 0.87, with the usual related files too.
- Now enable both aRts drivers are they can co-exist.
- Remove explicit binary requires.
- Enable X86_ASM_68000, seems to compile properly now.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 0.86-1
- Update to 0.86, with the usual related files too.
- Split off the roms to a separate source package.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net/> 0.85-1
- Update to 0.85, with the usual related files too.
- Added romcmp to be included, simplified the chdman and xml2info build.

* Thu Jul 22 2004 Matthias Saou <http://freshrpms.net/> 0.84.1-2
- Add 0.84.2 preview patch to fix xmess xgl build and other improvements.

* Sat Jul 17 2004 Matthias Saou <http://freshrpms.net/> 0.84.1-1
- Update to 0.84.1, with the usual related files too.
- Added the xml2info utility to be built and included.
- Added temporary fix for \" -> " to fix make problems with xgl target.

* Sun Jun 13 2004 Matthias Saou <http://freshrpms.net/> 0.83.1-1
- Update to 0.83.1, with the usual related files too.

* Sun May 16 2004 Matthias Saou <http://freshrpms.net/> 0.82.1-1
- Update to 0.82.1, with the usual related files too.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 0.81.1-1
- Update to 0.81.1, with the usual related files too.
- Added arts support by default.

* Fri Feb 20 2004 Matthias Saou <http://freshrpms.net/> 0.79.1-1
- Update to 0.79.1, with the usual related files too.

* Thu Feb 12 2004 Matthias Saou <http://freshrpms.net/> 0.78.1-3
- Added xmame-0.78.1-fix.patch to fix PPC build.

* Fri Jan 16 2004 Matthias Saou <http://freshrpms.net/> 0.78.1-1
- Update to 0.78.1.
- Updated all related files too.
- Added chdman to the mame build.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.77.1-1
- Update to 0.77.1.
- Updated all related files too, catver is up-to-date at last.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.76.1-2
- Rebuild for Fedora Core 1.

* Sun Oct 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.76.1, updated related files too (catver is still 0.74u1 though).

* Tue Sep 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.74.1.
- Updated all related files too.

* Sat Aug 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.72.1.
- Updated all related files too.

* Sat Jul 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.71.1.
- Updated all related files too.
- Added patch to fix build with the MIPS3_DRC.

* Thu Jun 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.70.1.
- Updated all related files too.

* Fri Jun 13 2003 Matthias Saou <http://freshrpms.net/>
- Added mips3 build option.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.69.1.
- Updated all extra files.
- Changes to reflect the new doc organisation.
- Replace the default prefix, defaults should work and be coherent now.
- Removed "optional" directories from %{_datadir}/xmame.

* Fri May 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.68.1.
- Updated all the extra files to their 0.68 versions.
- Merged Panu's mess additions and new wrapper script.

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.67.2.
- Update catver and history to 0.67.
- Removed nno longer needed install patch.

* Thu Apr 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.67.1.
- Split the free (beer ;-)) roms in a sub-package at last.
- Many spec tweaks.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.66.2.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.66.1, and update all related files.
- Removed now unneeded patches.
- Fix CFLAGS and CPU_TYPE for ppc!

* Sat Feb 22 2003 Matthias Saou <http://freshrpms.net/>
- Build with new blit and xgl patches.
- Re-enable asm68000 on x86.
- Added the OpenGL cabinets to the xgl package.

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.65.1.
- Disable xgl by default (been broken for some time now).

* Fri Feb  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.64.1-rc2.
- Cleanup of the optflags to reflect upstream changes.
- Remove obsolete cpu patch.

* Fri Jan 31 2003 Matthias Saou <http://freshrpms.net/>
- Major changes : Files are now in %%{_datadir}/xmame.
- All directories are now 2775 to allow more to be done by "game" members.
- Removed "snap" link, "cab" directory and added "icons" one.
- Disable asm68000 by default as it's broken.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.64.1rc1.
- Updated all associated files and added catver to the docs!
- Added romalizer to the docs + a few cleanups.

* Mon Jan 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.62.2.
- Update history to 62b and mameinfo to 4.26.

* Tue Dec 11 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.62.1-rc3.
- Included the latest testing netmame code.

* Mon Dec  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.62.1-rc1.

* Mon Nov 25 2002 Matthias Saou <http://freshrpms.net/>
- Cleanup and Sparc fixes thanks to Ralf Ertzinger.

* Fri Nov 15 2002 Matthias Saou <http://freshrpms.net/>
- Updated history data to 62.
- Updated Mameinfo to 4.20.
- Added default ALSA support.
- Fixed missing "samples" directory.

* Thu Nov 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1 final.
- Updated highscore data to 7.95.
- Updated history data to 61f.
- Updated Mameinfo to 4.1b.

* Sun Oct 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1-pr9.
- Removed XV specific stuff, just add it to the x11 target.
- Moved binaries to %%{_bindir} in order to have them in the search path.
- New %%{_prefix}/lib/games/xmame link to work with gxmame's default config.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Updated all obsolete -malign to -falign.
- Simplified --without stuff.
- Added XV build.

* Wed Sep 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1-pr7.

* Tue Aug 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1-pr3.

* Tue Aug 13 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1-pr2.

* Thu Jul 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.1-pr1.

* Mon May 27 2002 Matthias Saou <http://freshrpms.net/>
- Mostly fixes for building on PPC, thanks to Ralf Ertzinger.

* Mon May  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.60.1.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Fri Apr 19 2002 Matthias Saou <http://freshrpms.net/>
- Looking quite good now.
- Update to 0.59.2.
- Added %post and %postun scriptlets for the /usr/bin/xmame link.

* Thu Apr 11 2002 Matthias Saou <http://freshrpms.net/>
- Spec file maturing a bit, still in constant development.

* Sun Jan 13 2002 Matthias Saou <http://freshrpms.net/>
- Spec file rewrite from scratch.

