# $Id$
# Authority: matthias
# Upstream: <contact@frozen-bubble.org>

%define desktop_vendor freshrpms

Summary: Frozen Bubble arcade game
Name: frozen-bubble
Version: 1.0.0
Release: 6
License: GPL
Group: Amusements/Games
URL: http://www.frozen-bubble.org/
Source: http://zarb.org/~gc/fb/frozen-bubble-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#AutoReq: no
Requires: perl-SDL >= 1.19.0, SDL, SDL_mixer >= 1.2.2
BuildRequires: perl-SDL >= 1.19.0, SDL-devel, SDL_mixer-devel >= 1.2.2
BuildRequires: desktop-file-utils, /usr/bin/find
BuildConflicts: gimp-perl, gsl, perl-PDL

%description
Full-featured, colorful animated penguin eyecandy, 100 levels of 1p game,
hours and hours of 2p game, 3 professional quality 20-channels musics, 15
stereo sound effects, 7 unique graphical transition effects and a level
editor.


%prep
%setup


%build
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}" PREFIX="%{_prefix}"


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    PREFIX=%{buildroot}%{_prefix} \
    INSTALLARCHLIB=%{buildroot}%{perl_sitearch} \
    INSTALLSITEARCH=%{buildroot}%{perl_sitearch} \
    INSTALLVENDORARCH=%{buildroot}%{perl_sitearch}
%{__rm} -f %{buildroot}%{perl_sitearch}/{build_fbsyms,perllocal.pod}
/usr/bin/find %{buildroot} -name .xvpics | xargs rm -rf

%{__install} -D -m644 icons/frozen-bubble-icon-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/frozen-bubble.png

# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Frozen Bubble
Comment=Arcade game similar to Puzzle Bobble where you need to launch bubbles and group them by color
Exec=frozen-bubble
Icon=frozen-bubble.png
Terminal=0
Type=Application
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    --add-category Application                  \
    --add-category Game                         \
    %{name}.desktop

# Quick fix in order to not have rpm pick up perl(Gimp) as a dependency
%{__chmod} -x %{buildroot}%{_prefix}/share/%{name}/gfx/shoot/create.pl


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES COPYING README
%{_prefix}/bin/*
%{_prefix}/share/%{name}
%{_prefix}/share/man/man6/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{perl_sitearch}/auto/*
%{perl_sitearch}/*.pm


%changelog
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

