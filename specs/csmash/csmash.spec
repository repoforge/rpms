# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: 3D tabletennis game
Name: csmash
Version: 0.6.6
Release: 4%{?dist}
License: GPL
Group: Amusements/Games
URL: http://cannonsmash.sourceforge.net/
Source: http://dl.sf.net/cannonsmash/%{name}-%{version}.tar.gz
Patch: csmash-0.6.6-64bit-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: Mesa-devel, libjpeg-devel, zlib-devel, gtk2-devel >= 2.0.0
BuildRequires: SDL-devel >= 1.2.0, SDL_mixer-devel, SDL_image-devel
BuildRequires: gcc-c++, desktop-file-utils

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to
represent various strategy of tabletennis on computer game.
This program requires OpenGL and SDL. If your machine doesn't have 3D
accelaration video card, this program runs very slowly.


%prep
%setup
%patch -p0 -b .64bit


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Cannon Smash
Comment=3D tabletennis game
Exec=csmash
Icon=%{_datadir}/games/%{name}/images/PenAttack.jpg
Terminal=false
Type=Application
Categories=Application;Game;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS ChangeLog README README.en
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/games/%{name}


%changelog
* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-4
- Add 64bit-fixes patch from Mandrake Linux to fix x86_64 build.

* Thu Sep 16 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-3
- Added missing zlib-devel build dep for YDL4.
- Removed explicit deps, they're all picked up automatically.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-2
- Rebuild for Fedora Core 2.

* Thu Feb 12 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-1
- Update to 0.6.6, now uses gtk2.
- Fix a typo in the desktop file and added icon.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.6.5-2
- Rebuild for Fedora Core 1... the configure problem is gone :-/

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.

* Sat Feb  9 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

