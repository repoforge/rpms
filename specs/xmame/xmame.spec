# $Id: xmame.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

#define rcver rc2
%define targets %{?!_without_mame:mame} %{?!_without_mess:mess}

Summary: The X Multi Arcade Machine Emulator
Name: xmame
Version: 0.79.1
Release: %{?rcver:0.%{rcver}.}1.fr
Source0: http://x.mame.net/download/xmame-%{version}%{?rcver:-%{rcver}}.tar.bz2
Source1: xmame.wrapper
Source10: http://www.mame.net/roms/polyplay.zip
Source11: http://www.mame.net/roms/robby.zip
Source12: http://www.mame.net/roms/gridlee.zip
Source20: http://cheat.retrogames.com/cheat.zip
# http://www.mameworld.net/highscore/ 8.2 - 18/10/2003
Source21: http://www.mameworld.net/highscore/uhsdat82.zip
# http://fandemame.emu-france.com/ 0.79c - 12/02/2004
Source22: http://fandemame.emu-france.com/files/history079c.zip
# http://www.mameworld.net/mameinfo/ 0.79u1 - 09/02/2004
Source23: http://www.mameworld.net/mameinfo/update/Mameinfo079u1.zip
# http://www.mameworld.net/catlist/ 0.79u1 - 13/02/2004
Source30: http://www.mameworld.net/catlist/files/catver.zip
License: MAME
URL: http://x.mame.net/
Group: Applications/Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: %{name}-bin = %{version}
BuildRequires: unzip, XFree86-devel, zlib-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%ifarch %ix86
%{!?_without_asm68000:BuildRequires: nasm >= 0.98}
%{!?_without_mips3:BuildRequires: nasm >= 0.98}
%endif

%description
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

The main package contains the docs, data files, and three free games so that
you have your X-Mame ready to run in no time! You will still need to pick
a package containing the main xmame binary though, from either the basic
x11 version, the SDL version or the special OpenGL xgl version.

Available rpmbuild rebuild options :
--without mame mess x11 xgl SDL asm68000 mips3 alsa esound opts quietbuild


%package x11
Summary: X-Mame arcade game emulator compiled for X11 DGA or XV display
Group: Applications/Emulators
Provides: %{name}-bin = %{version}
Requires: zlib
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}

%description x11
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

This version has been compiled for X11 DGA and XV displays.


%package SDL
Summary: X-Mame arcade game emulator compiled for SDL display
Group: Applications/Emulators
Provides: %{name}-bin = %{version}
Requires: SDL, zlib
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}
BuildRequires: SDL-devel

%description SDL
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

This version has been compiled for SDL display.


%package xgl
Summary: X-Mame arcade game emulator compiled for OpenGL display
Group: Applications/Emulators
Provides: %{name}-bin = %{version}
Requires: zlib, libjpeg
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}
BuildRequires: Mesa-devel, libjpeg-devel

%description xgl
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

This version has been compiled for OpenGL display.


%package roms
Summary: Freely available ROMs to use with xmame
Group: Applications/Emulators
License: Freeware
URL: http://www.mame.net/downmisc.html
Requires: %{name}-bin

%description roms
This the the *nix port of the almost legendary mame. Mame is an arcade
machine emulator, started in 1997 by Nicola Salmoria. It started out as a
series of emulators for individual games. This series of emulators was
combined into a single multi-game emulator.

This package contains 3 arcade games that are freely available:
- Gridlee © 1983 Videa.
- Poly-Play © 1985 VEB Polytechnik Karl-Marx-Stadt.
- Robby Roto © 1981 Bally Midway, © 1999 Jay Fenton.


%package -n xmess
Summary: The Multi Emulator Super System
Group: Applications/Emulators

%description -n xmess
This is the *nix port of MESS. MESS is a free emulator which emulates a
large variety of different systems, including old Atari, Apple, BBC,
Commodore, MSX, ZX Spectrum computers. For full list of supported systems
see http://www.mess.org/


%package -n xmess-x11
Summary: The Multi Emulator Super System compiled for X11 DGA or XV display
Group: Applications/Emulators
Requires: zlib
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}

%description -n xmess-x11
This is the *nix port of MESS. MESS is a free emulator which emulates a
large variety of different systems, including old Atari, Apple, BBC,
Commodore, MSX, ZX Spectrum computers. For full list of supported systems
see http://www.mess.org/

This version has been compiled for X11 DGA or XV display.


%package -n xmess-SDL
Summary: The Multi Emulator Super System compiled for SDL display
Group: Applications/Emulators
Requires: SDL, zlib
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}
BuildRequires: SDL-devel

%description -n xmess-SDL
This is the *nix port of MESS. MESS is a free emulator which emulates a
large variety of different systems, including old Atari, Apple, BBC,
Commodore, MSX, ZX Spectrum computers. For full list of supported systems
see http://www.mess.org/

This version has been compiled for SDL display.


%package -n xmess-xgl
Summary: The Multi Emulator Super System compiled for OpenGL display
Group: Applications/Emulators
Requires: zlib, libjpeg
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}
BuildRequires: Mesa-devel, libjpeg-devel

%description -n xmess-xgl
This is the *nix port of MESS. MESS is a free emulator which emulates a
large variety of different systems, including old Atari, Apple, BBC,
Commodore, MSX, ZX Spectrum computers. For full list of supported systems
see http://www.mess.org/

This version has been compiled for OpenGL display.


%prep
%setup -q -n %{name}-%{version}%{?rcver:-%{rcver}}


%build
test -e Makefile || cp -a makefile.unix Makefile
# Comment out the defaults, to enable overriding with the env variables
perl -pi -e 's/^CFLAGS/# CFLAGS/g' Makefile
perl -pi -e 's/^MY_CPU/# MY_CPU/g' Makefile

# Make the package build verbose by default (to see opts etc.)
%{?_without_quietbuild: perl -pi -e 's/^QUIET/# QUIET/g' src/unix/unix.mak}

# The default, if not overwritten below
export PREFIX=%{_prefix}
export CFLAGS="%{optflags}"
export JOY_I386=1
%{!?_without_alsa:export SOUND_ALSA=1}
%{!?_without_esound:export SOUND_ESOUND=1}

# Optimization flags, CPU type and defaults for the makefile
%ifarch %ix86
    export MY_CPU="i386"
    %{!?_without_opts: export CFLAGS="%{optflags} -O3 -Wall"}
    %{!?_without_asm68000: export X86_ASM_68000=1}
    %{!?_without_mips3: export X86_MIPS3_DRC=1}
%endif

%ifarch ppc
    export MY_CPU="risc"
    %{!?_without_opts: export CFLAGS="%{optflags} -O3 -Wall"}
%endif

%ifarch sparc sparcv8 sparcv9 sparc64
    export MY_CPU="risc"
    # Sparc platform fails to compile with -O2, so override it.
    %{!?_without_opts: export CFLAGS="%{optflags} -O -fomit-frame-pointer -funroll-loops -fstrength-reduce -ffast-math -finline-functions -fforce-mem -fforce-addr -fthread-jumps -fcse-follow-jumps -fcse-skip-blocks -frerun-cse-after-loop -felide-constructors -fexpensive-optimizations -fdelayed-branch -fschedule-insns -fschedule-insns2 -pipe"}
%endif

# Prepare all the extra .dat files
mkdir datfiles
for file in %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}; do
    unzip -o -d datfiles/ $file
done

# Now, do all the building (this is long!)
for target in %{targets}; do
    %{!?_without_x11: make %{?_smp_mflags} DISPLAY_METHOD=x11 X11_DGA=1 X11_XV=1} TARGET=$target
    %{!?_without_SDL: make %{?_smp_mflags} DISPLAY_METHOD=SDL SOUND_SDL=1} TARGET=$target
    %{!?_without_xgl: make %{?_smp_mflags} DISPLAY_METHOD=xgl} TARGET=$target
#   %{!?_without_xgl: make %{?_smp_mflags} DISPLAY_METHOD=xgl GLCFLAGS="-D_X11_ -DGLU_VERSION_1_2"} TARGET=$target
    # The MAME chd manager
    %{?!_without_mame: make %{?_smp_mflags} chdman}
done


%install
rm -rf %{buildroot}

for target in %{targets}; do
    make install-man \
        INSTALL_USER=`id -un` \
        INSTALL_GROUP=`id -gn` \
        MANDIR=%{buildroot}%{_mandir}/man6 \
        TARGET=$target
done

mkdir -p %{buildroot}%{_bindir}
for target in %{targets}; do
    install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/x${target}
    %{!?_without_x11: install -m 755 x${target}.x11 %{buildroot}%{_bindir}/}
    %{!?_without_SDL: install -m 755 x${target}.SDL %{buildroot}%{_bindir}/}
    %{!?_without_xgl: install -m 755 x${target}.xgl %{buildroot}%{_bindir}/}
done
%{?!_without_mame: install -m 755 chdman %{buildroot}%{_bindir}/}

# We don't want all the docs
mkdir -p doc2/{xmame/html,xmess}
pushd src/unix/doc
    cp -a {*.html,*.css,img} ../../../doc2/xmame/html/
    cp -a changes.* dga2.txt multiplayer-readme.txt \
        xmame-doc.txt xmamerc.dist mame/* ../../../doc2/xmame/
    cp -a xmessrc.dist mess/* ../../../doc2/xmess/
popd


%if %{?_without_mame:0}%{!?_without_mame:1}
# Add all directories
mkdir -p %{buildroot}%{_datadir}/xmame/{artwork,roms,samples,snap}

# Install the ROMs
install -m 644 %{SOURCE10} %{SOURCE11} %{SOURCE12} \
    %{buildroot}%{_datadir}/xmame/roms/

# The extra dat files
install -m 664 datfiles/*.dat %{buildroot}%{_datadir}/xmame/

# Install the OpenGL cabinets
%{!?_without_xgl: cp -a src/unix/cab %{buildroot}%{_datadir}/xmame/}
%endif


%if %{?_without_mess:0}%{!?_without_mess:1}
# Add all directories
mkdir -p %{buildroot}%{_datadir}/xmess/{artwork,bios,crc,samples,snap,software}
%endif


# Uncompress catver.ini (will be in the docs)
unzip -o %{SOURCE30}
#unzip -o catver.zip


%clean
rm -rf %{buildroot}


%if %{?_without_mame:0}%{!?_without_mame:1}
%files
%defattr(-, root, root)
%doc README doc2/xmame/* contrib/tools/romalizer contrib/tools/mame-cd 
%doc catver.ini
%{_bindir}/chdman
%{_bindir}/xmame
%dir %attr(2775, root, games) %{_datadir}/xmame
%dir %attr(2775, root, games) %{_datadir}/xmame/artwork
%dir %attr(2775, root, games) %{_datadir}/xmame/roms
%dir %attr(2775, root, games) %{_datadir}/xmame/samples
%dir %attr(2775, root, games) %{_datadir}/xmame/snap
%{_datadir}/xmame/*.dat
%{_mandir}/man6/xmame.6*
%endif

%if %{?_without_x11:0}%{!?_without_x11:%{?_without_mame:0}%{!?_without_mame:1}}
%files x11
%attr(2755, root, games) %{_bindir}/xmame.x11
%endif

%if %{?_without_SDL:0}%{!?_without_SDL:%{?_without_mame:0}%{!?_without_mame:1}}
%files SDL
%attr(2755, root, games) %{_bindir}/xmame.SDL
%endif

%if %{?_without_xgl:0}%{!?_without_xgl:%{?_without_mame:0}%{!?_without_mame:1}}
%files xgl
%attr(2755, root, games) %{_bindir}/xmame.xgl
%attr(-, root, root) %{_datadir}/xmame/cab
%endif

%if %{?_without_mame:0}%{!?_without_mame:1}
%files roms
%attr(664, root, games) %{_datadir}/xmame/roms/*.zip
%endif


%if %{?_without_mess:0}%{!?_without_mess:1}
%files -n xmess
%defattr(-, root, root)
%doc README doc2/xmess/*
%dir %attr(2775, root, games) %{_datadir}/xmess
%dir %attr(2775, root, games) %{_datadir}/xmess/artwork
%dir %attr(2775, root, games) %{_datadir}/xmess/bios
%dir %attr(2775, root, games) %{_datadir}/xmess/crc
%dir %attr(2775, root, games) %{_datadir}/xmess/samples
%dir %attr(2775, root, games) %{_datadir}/xmess/snap
%dir %attr(2775, root, games) %{_datadir}/xmess/software
%{_bindir}/xmess
%{_mandir}/man6/xmess.6.*
%endif

%if %{?_without_x11:0}%{!?_without_x11:%{?_without_mess:0}%{!?_without_mess:1}}
%files -n xmess-x11
%attr(2755, root, games) %{_bindir}/xmess.x11
%endif

%if %{?_without_SDL:0}%{!?_without_SDL:%{?_without_mess:0}%{!?_without_mess:1}}
%files -n xmess-SDL
%attr(2755, root, games) %{_bindir}/xmess.SDL
%endif

%if %{?_without_xgl:0}%{!?_without_xgl:%{?_without_mess:0}%{!?_without_mess:1}}
%files -n xmess-xgl
%attr(2755, root, games) %{_bindir}/xmess.xgl
%endif


%changelog
* Fri Feb 20 2004 Matthias Saou <http://freshrpms.net/> 0.79.1-1.fr
- Update to 0.79.1, with the usual related files too.

* Thu Feb 12 2004 Matthias Saou <http://freshrpms.net/> 0.78.1-3.fr
- Added xmame-0.78.1-fix.patch to fix PPC build.

* Fri Jan 16 2004 Matthias Saou <http://freshrpms.net/> 0.78.1-1.fr
- Update to 0.78.1.
- Updated all related files too.
- Added chdman to the mame build.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.77.1-1.fr
- Update to 0.77.1.
- Updated all related files too, catver is up-to-date at last.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.76.1-2.fr
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

