# $Id: neverball.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

%define desktop_vendor freshrpms

Summary: A test of skill, part puzzle game and part action game
Name: neverball
Version: 1.1.0
Release: 1.fr
License: GPL
Group: Amusements/Games
URL: http://icculus.org/%{name}/
Source: http://icculus.org/%{name}/%{name}-%{version}.tar.bz2
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
%setup -q

%build
# Change the location where the binary will look for the "data" directory
perl -pi -e 's|./data|%{_datadir}/%{name}|g' config.h
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
# Install the binary and the "data" directory
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}
cp -a data %{buildroot}%{_datadir}/%{name}

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=%{summary}
Exec=%{name}
Icon=%{_datadir}/%{name}/shot-rlk/risers.jpg
Terminal=0
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category X-Red-Hat-Extra                \
  --add-category Application                    \
  --add-category Game                           \
  %{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING MAPPING README
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/%{name}

%changelog
* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-1.fr
- Initial RPM release.

