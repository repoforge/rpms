# $Id$
# Authority: leet

# Upstream: Frank Becker <crittermail2005$telus,net>
# Screenshot: http://criticalmass.sourceforge.net/images-critter/pics.v097/snap04.jpeg
# ScreenshotURL: http://criticalmass.sourceforge.net/oldweb/screenshots.html

%define real_name CriticalMass

%{!?_dist: %{expand: %%define dist rhfc4}}

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: SDL/OpenGL space shoot'em up game
Name: critter
Version: 0.9.12
Release: 1
License: GPL
Group: Amusements/Games
URL: http://criticalmass.sourceforge.net/critter.php

Source: http://dl.sf.net/criticalmass/%{real_name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, zlib-devel
BuildRequires: libpng-devel, gcc-c++, desktop-file-utils
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game. It
currently runs on Mac OS X, Windows, and Linux. The latter is my main
development platform. Other platforms supported by SDL/OpenGL may also
work with a bit of work.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m 0755 %{buildroot}%{_datadir}/icons/
%{__install} -m 0644 %{name}.png %{buildroot}%{_datadir}/icons/%{name}.png

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=%{real_name}
Comment=SDL/OpenGL space shoot'em up game
Exec=%{name}
Icon=%{name}.png
Terminal=false
Version=%{version}
Type=Application
StartupNotify=true
Encoding=UTF-8
EOF

#Categories=Application;Game;X-Red-Hat-Extra;
#EOF

%if %{!?_without_freedesktop:1}0
%{__install} -d -m 0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-category X-Fedora \
    --add-category Application \
    --add-category Game \
    %{name}.desktop
#    %{buildroot}%{_datadir}/applications/%{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)

%doc Readme.html COPYING TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/Critical_Mass/*

%changelog
* Thu Sep 29 2005 C.Lee Taylor <leet@leenx.co.za> 0.9.12-1
- Made some minor updates and fix icon

* Wed Aug 31 2005 C.Lee Taylor <leet@leenx.co.za> 0.9.12-0
- Initial package
