# $Id$
# Authority: dries
# Upstream: <rekless$fastmail,fm>

# Screenshot: http://skystreets.kaosfusion.com/screenshot3.png
# ScreenshotUrl: http://skystreets.kaosfusion.com/

# ExcludeDist: fc1

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Clone of skyroads, jump and speed along platforms to reach the goal
Name: skystreets
Version: 0.2.3
Release: 1
License: GPL
Group: Amusements/Games
URL: http://skystreets.kaosfusion.com/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://skystreets.kaosfusion.com/skystreets-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: imlib-devel, imlib, gcc-c++, SDL-devel, SDL_image-devel
BuildRequires: libtiff-devel, libtiff, libjpeg, zlib
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU, XFree86-Mesa-libGL }
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU, xorg-x11-Mesa-libGL}
Requires: SDL, SDL_image, libtiff, imlib

%description
A modernised remake of the popular old game, Skyroads, by Bluemoon software.
The objective is to go along the tracks, and try to reach the objective
before either your fuel or oxygen run out, whilst trying to get as fast a
time as possible. Some obstacles require more thought or tact. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/usr/share/applications
cat > %{buildroot}/usr/share/applications/skystreets.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=SkyStreets
Exec=/usr/bin/skystreets
Categories=Application;Game;ArcadeGame
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/skystreets
%{_datadir}/skystreets
%{_datadir}/applications/skystreets.desktop

%changelog
* Wed Mar 31 2004 Dries Verachtert <dries@ulyssis.org> 0.2.3-1
- initial packaging
