# $Id: csmash.spec,v 1.1 2004/02/26 12:32:02 thias Exp $

%define desktop_vendor freshrpms

Summary: A 3D tabletennis game.
Name: csmash
Version: 0.6.6
Release: 1.fr
License: GPL
Group: Amusements/Games
Source: http://dl.sf.net/cannonsmash/%{name}-%{version}.tar.gz
URL: http://cannonsmash.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
Requires: Mesa, libjpeg, gtk2 >= 2.0.0
Requires: SDL >= 1.2.0, SDL_mixer, SDL_image
BuildRequires: Mesa-devel, libjpeg-devel, gtk2-devel >= 2.0.0
BuildRequires: SDL-devel >= 1.2.0, SDL_mixer-devel, SDL_image-devel
BuildRequires: gcc-c++, desktop-file-utils

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to 
represent various strategy of tabletennis on computer game. 
This program requires OpenGL and SDL. If your machine doesn't have 3D
accelaration video card, this program runs very slowly.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Create the system menu entry
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Cannon Smash
Comment=%{summary}
Exec=%{name}
Icon=%{_datadir}/games/%{name}/images/PenAttack.jpg
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

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING CREDITS ChangeLog README README.en
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/games/%{name}

%changelog
* Thu Feb 12 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-1.fr
- Update to 0.6.6, now uses gtk2.
- Fix a typo in the desktop file and added icon.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.6.5-2.fr
- Rebuild for Fedora Core 1... the configure problem is gone :-/

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.

* Sat Feb  9 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

