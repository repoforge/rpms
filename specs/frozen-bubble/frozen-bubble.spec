# $Id$
# Authority: matthias
# Upstream: <contact$frozen-bubble,org>

%define desktop_vendor rpmforge

Summary: Frozen Bubble arcade game
Name: frozen-bubble
Version: 2.2.0
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.frozen-bubble.org/

Source: http://www.frozen-bubble.org/data/frozen-bubble-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl-SDL >= 2.1.3, SDL_mixer-devel, SDL_Pango-devel, glib2-devel, perl(ExtUtils::MakeMaker)
BuildRequires: gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: perl-SDL >= 2.1.3

%description
Full-featured, colorful animated penguin eyecandy, 100 levels of 1p game,
hours and hours of 2p game, 3 professional quality 20-channels musics, 15
stereo sound effects, 7 unique graphical transition effects and a level
editor.

%package server
Summary: Frozen Bubble network game dedicated server
Group: System Environment/Daemons

%description server
Frozen Bubble network game dedicated server. The server is already included
with the game in order to be launched automatically for LAN games, so you
only need to install this package if you want to run a full-time dedicated
Frozen Bubble network game dedicated server.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
    OPTIMIZE="%{optflags}" \
    CFLAGS="%{optflags} `pkg-config glib-2.0 --cflags`" \
    LIBS="`pkg-config glib-2.0 --libs`" \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libexecdir} \
    DATADIR=%{_datadir}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libexecdir} \
    DATADIR=%{_datadir} \
    DESTDIR=%{buildroot}
%find_lang %{name}

# Install server init script and default configuration
%{__install} -D -p -m 0755 server/init/fb-server \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/fb-server
%{__install} -D -p -m 0755 server/init/fb-server.conf \
    %{buildroot}%{_sysconfdir}/fb-server.conf

# Instal meny entry icon
%{__install} -D -p -m 0644 icons/frozen-bubble-icon-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/frozen-bubble.png

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Frozen Bubble
Comment=Arcade game where you need to launch bubbles and group them by color
Exec=frozen-bubble
Icon=frozen-bubble.png
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    %{name}.desktop
%else
%{__install} -Dp -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

# Clean up the installed perl files
find %{buildroot} -name '*.bs' -o -name .packlist -o -name 'perllocal.pod' \
    | xargs %{__rm} -rf

%post server
/usr/sbin/useradd -r -s /bin/nologin -d %{_libexecdir}/frozen-bubble fbubble || :
/sbin/chkconfig --add fb-server

%preun server
if [ $1 -eq 0 ]; then
    /sbin/service fb-server stop
    /sbin/chkconfig --del fb-server
fi

%postun server
/usr/sbin/userdel fbubble || :
if [ $1 -ge 1 ]; then
    /sbin/service fb-server condrestart
fi

%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TIPS
%{_bindir}/frozen-bubble
%{_bindir}/frozen-bubble-editor
%{_libexecdir}/frozen-bubble/
%{_datadir}/frozen-bubble/
%{_datadir}/pixmaps/frozen-bubble.png
%{_mandir}/man6/*
%{perl_sitearch}/auto/*
%{perl_sitearch}/*.pm
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

%files server
%defattr(-, root, root, 0755)
%doc server/init/README
%config(noreplace) %{_sysconfdir}/fb-server.conf
%{_sysconfdir}/rc.d/init.d/fb-server
%{_libexecdir}/frozen-bubble/

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0-1

* Thu Oct 26 2006 Matthias Saou <http://freshrpms.net/> 2.0.0-0
- Update to 2.0.0 pre-release.
- Split out the server in its own sub-package, which can be installed alone.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.0-9
- Release bump to drop the disttag number in FC5 build.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-8
- Replaced patch from one found on the sdl.perl list :
  http://www.nntp.perl.org/group/perl.sdl.devel/972

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-7
- Added perl-SDL.patch to fix running against recent releases.
- Remove .bs and .packlist temp perl files from the packaged files.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-6
- Updated the source location.
- Rebuild for Fedora Core 2.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-6
- Spec file cleanups : More macros, fixed desktop entry description.

* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-5
- Rebuild for Fedora Core 1 as the perl-SDL package is fixed at last.
- Added SDL_mixer build dep.
- Remove Autoreq disabling and add a nicer fix for the perl(Gimp) dep.

* Tue Apr  1 2003 Matthias Saou <http://freshrpms.net/>
- Replace the __find_requires with AutoReq: as it works better.
- Remove .xvpics from installed files.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Feb 18 2003 Matthias Saou <http://freshrpms.net/>
- Added missing man pages, thanke to Michal Ambroz.

* Mon Feb 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0 (at last!).
- New menu entry.

* Thu Feb  7 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Thu Feb  7 2002 Matthias Saou <http://freshrpms.net/>
- Spec file modifications for a Red Hat Linux release.

* Wed Feb  6 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.1-1mdk
- first mdk rpm

