# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

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

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge
#define prever rc4

Summary: Multiplayer 'Tron' 3D racing game
Name: armagetronad
Version: 0.2.8.2.1
Release: 1%{?prever:.%{prever}}%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.armagetronad.net/
Source: http://dl.sf.net/armagetronad/armagetronad-%{version}%{?prever:_%{prever}}.src.tar.bz2
Patch0: armagetronad-0.2.8_beta3-gcc4.patch
Patch1: armagetronad-0.2.8_beta4-desktop.patch
Patch2: armagetronad-0.2.8.2-uninstall.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libstdc++-devel, zlib-devel, libpng-devel, libjpeg-devel
BuildRequires: SDL_image-devel, SDL_mixer-devel, SDL-devel, esound-devel
BuildRequires: libxml2-devel, /usr/bin/find, unzip, gcc-c++, which
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif
Obsoletes: armagetron <= 0.2.6.1
Provides: armagetron = %{version}-%{release}

%description
There is not much to be said about the game: you ride a lightcycle,
a kind of motorbike that can't be stoppen and leaves a wall where
it goes. You can make turns of 90 degrees and can accelerate by
driving close to walls. Make your enemies hit a wall while avoiding
the same fate.

Available rpmbuild rebuild options :
--without : freedesktop xorg


%prep
%setup -n armagetronad-%{version}%{?prever:_%{prever}}
%patch0 -p1 -b .gcc4
%patch1 -p1 -b .desktop
%patch2 -p1 -b .uninstall


%build
%configure \
    --enable-music \
    --disable-sysinstall \
    --disable-uninstall \
    --disable-games
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%makeinstall

# Put the docs where we include them with %%doc
%{__mv} %{buildroot}%{_datadir}/doc/armagetronad/html _docs

# Yeah, add icons for the menu entry!
# New freedesktop locations
%{__install} -D -p -m 0644 desktop/icons/large/armagetronad.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/armagetronad.png
%{__install} -D -p -m 0644 desktop/icons/medium/armagetronad.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/armagetronad.png
%{__install} -D -p -m 0644 desktop/icons/small/armagetronad.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/armagetronad.png
# Legacy location (put 32 x 32 in there)
%{__install} -D -p -m 0644 desktop/icons/medium/armagetronad.png \
    %{buildroot}%{_datadir}/pixmaps/armagetronad.png

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    desktop/armagetronad.desktop
%else
%{__install} -D -p -m 0644 desktop/armagetronad.desktop \
    %{buildroot}/etc/X11/applnk/Games/armagetronad.desktop
%endif

# Workaround for 0.2.8_beta3 not finding the config files in /etc/
%{__ln_s} /etc/armagetronad %{buildroot}%{_datadir}/armagetronad/config


%clean
%{__rm} -rf %{buildroot}


%post
gtk-update-icon-cache || :

%postun
gtk-update-icon-cache || :


%files
%defattr(-, root, root, 0755)
%doc _docs/*
%dir %{_sysconfdir}/armagetronad/
%config(noreplace) %{_sysconfdir}/armagetronad/*
%{_bindir}/armagetronad
%dir %{_datadir}/armagetronad/
%{_datadir}/armagetronad/config
%exclude %{_datadir}/armagetronad/desktop/
%{_datadir}/armagetronad/language/
%{_datadir}/armagetronad/models/
%{_datadir}/armagetronad/resource/
%exclude %{_datadir}/armagetronad/scripts/
%{_datadir}/armagetronad/sound/
%{_datadir}/armagetronad/textures/
%{_datadir}/icons/hicolor/*/armagetronad.png
%{_datadir}/pixmaps/armagetronad.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-armagetronad.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Games/armagetronad.desktop}


%changelog
* Tue Aug 22 2006 Matthias Saou <http://freshrpms.net/> 0.2.8.2.1-1
- Update to 0.2.8.2.1.

* Wed Jun 28 2006 Matthias Saou <http://freshrpms.net/> 0.2.8.2-1
- Update to 0.2.8.2.
- Include patch to fix the uninstall lines in Makefile.in.
- Add "which" build requirement.

* Mon Mar 27 2006 Matthias Saou <http://freshrpms.net/> 0.2.8.1-1
- Update to 0.2.8.1.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.8.0-0.3.rc4
- Update to 0.2.8.0_rc4.

* Tue Jan 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.8-0.2.beta4
- Update to 0.2.8_beta4.
- Add modular xorg build conditional.
- Update desktop patch.

* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 0.2.8-0.1.beta3
- Update to 0.2.8_beta3.
- Update gcc4 patch (only one line left now).
- Add new libxml2-devel build dependency.
- Use included desktop icons, no longer convert the .ico file.
- Use included desktop file, but patch it first (fixes + enhancements).
- Add gtk-update-icon-cache scriplets.
- Enable music.
- Disable the "games path".
- Add "config" symlink to workaround the config files not found (ugly, but...).

* Fri Apr 22 2005 Matthias Saou <http://freshrpms.net/> 0.2.7.1-2
- Added gcc4 patch (sf.net bug 1187292).

* Thu Mar 10 2005 Matthias Saou <http://freshrpms.net/> 0.2.7.1-1
- Update to armagetron advanced 0.2.7.1.
- Obsolete armagetron <= 0.2.6.1.
- No longer overwrite the default wrapper script.

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.2.6.0-1
- Update to "unstable" 0.2.6.0.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 0.2.5.2-3
- Rebuild for Fedora Core 2.
- Split off the moviepack files into their own noarch package.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.2.5.2-2
- Added missing XFree86-Mesa-libGLU build dep :-(
- Rebuild for Fedora Core 1 at last.

* Wed Oct 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.5.2.
- Removed %%{prever} stuff.

* Sun Jul 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.5.

* Thu Jul 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.

* Sun Jul  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.3.

* Mon Jun 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.2.
- The build is now more standard, no more manual copying of files.
- PPC include workaround removed, not needed anymore.
- Major spec file updates.

* Sat Jun 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.pre3.

* Mon Jun  2 2003 Matthias Saou <http://freshrpms.net/>
- s/Games/Game for the desktop file, doh!

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sat Mar 15 2003 Matthias Saou <http://freshrpms.net/>
- Remove CVS directories from the docs.
- Added --without freedesktop option in order to rebuild for 7.x.
- Added YellowDog 2.3 include path workaround.

* Sat Feb 15 2003 Matthias Saou <http://freshrpms.net/>
- Applied Ben Liblit's changes at last!
- Install language files.
- Change wrapper to save settings to ~/.armagetron/

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Tue Jul  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.0.pre_020624.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Fri Apr 19 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt without the NVIDIA libGLcore.so.1 dependency (doh!).

* Tue Nov 20 2001 Matthias Saou <http://freshrpms.net/>
- Added a simple shell script to have the menu entry work with KDE.
- Added a separate package for the "moviepack"... that thing is cool :-)
- Changed the binary to sgid "games" so that high scores are saved.
- Added an icon for the menu entry.

* Mon Nov 19 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.4.9.
- Spec file cleanup.

* Thu Jan  4 2001 Tim Powers <timp@redhat.com>
- defattr was in wrong place in files list, leaving files owned by the
  build system, fixed

* Tue Nov 28 2000 Karsten Hopp <karsten@redhat.de>
- initial RPM

