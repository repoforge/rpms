# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: Test of skill, part puzzle game and part action game
Name: neverball
Version: 1.2.5
Release: 1
License: GPL
Group: Amusements/Games
URL: http://icculus.org/neverball/
Source: http://icculus.org/neverball/neverball-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL, SDL_image, SDL_mixer, SDL_ttf
BuildRequires: perl, desktop-file-utils, XFree86-Mesa-libGLU, zlib-devel
BuildRequires: SDL-devel, SDL_image-devel, SDL_mixer-devel, SDL_ttf-devel

%description
Tilt the floor to roll a ball through an obstacle course before time runs out.
Neverball is part puzzle game, part action game, and entirely a test of skill.

If the ball falls or time expires, a ball is lost. Collect 100 coins to save
your progress and earn an extra ball. Red coins are worth 5, blue are worth 10.


%prep
%setup


%build
# Change the location where the binary will look for the "data" directory
perl -pi -e 's|./data|%{_datadir}/%{name}|g' config.h
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# Install the binary and the "data" directory
%{__install} -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__mkdir_p} %{buildroot}%{_datadir}
%{__cp} -a data %{buildroot}%{_datadir}/%{name}

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=Test of skill, part puzzle game and part action game
Exec=%{name}
Icon=%{_datadir}/%{name}/shot-rlk/risers.jpg
Terminal=0
Type=Application
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category Application                    \
  --add-category Game                           \
  %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING MAPPING README
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/%{name}


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Update to 1.2.5.

* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Initial RPM release.

