# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: Frozen Bubble arcade game.
Name: frozen-bubble
Version: 1.0.0
Release: 5
License: GPL
Group: Amusements/Games
Source: http://frozenbubble.free.fr/fb/%{name}-%{version}.tar.bz2
URL: http://www.frozen-bubble.org/
BuildRoot: %{_tmppath}/%{name}-root
#AutoReq: no
Requires: perl-SDL >= 1.19.0, SDL, SDL_mixer >= 1.2.2
BuildRequires: perl-SDL >= 1.19.0, SDL-devel, SDL_mixer-devel >= 1.2.2
BuildRequires: desktop-file-utils
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
find %{buildroot} -name .xvpics | xargs rm -rf

%{__install} -D -m644 icons/frozen-bubble-icon-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/frozen-bubble.png

# Create the system menu entry
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Frozen Bubble
Comment=%{summary}
Exec=frozen-bubble
Icon=frozen-bubble.png
Terminal=0
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original   \
    --dir %{buildroot}%{_datadir}/applications                      \
    --add-category X-Red-Hat-Extra                                  \
    --add-category Application                                      \
    --add-category Game                                             \
    %{name}.desktop

# Quick fix in order to not have rpm pick up perl(Gimp) as a dependency
chmod -x %{buildroot}%{_prefix}/share/%{name}/gfx/shoot/create.pl

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
* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-5.fr
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

