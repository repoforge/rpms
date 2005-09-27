# $Id$
# Authority: leet

# Upstream: Calle Laakkonen <calle$luolamies,org>
# Screenshot: http://criticalmass.sourceforge.net/images-critter/pics.v097/snap04.jpeg

%define real_name CriticalMass

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
Release: 0
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

#%if %{!?_without_freedesktop:1}0
#%{__mkdir_p} %{buildroot}%{_datadir}/applications
#desktop-file-install \
#    --vendor %{desktop_vendor} \
#    --dir %{buildroot}%{_datadir}/applications \
#    --delete-original \
#    --add-category X-Fedora \
#    --add-category Application \
#    --add-category Game \
#    %{name}.desktop
##    %{buildroot}%{_datadir}/applications/%{name}.desktop
#%else
#%{__install} -D -m 0644 %{name}.desktop \
#    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
#%endif
#	
## Convert the ICO file to png to be used as the menu entry icon
##%{__install} -d -m 0755 %{buildroot}%{_datadir}/pixmaps
#%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/icons/
%{__install} -m0744 %{name}.png %{buildroot}%{_datadir}/icons/%{name}.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=%{real_name}
Comment=SDL/OpenGL space shoot'em up game
Exec=%{name}
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%doc %{_mandir}/man?/*
%{_bindir}/*
#%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/icons/%{name}.png
#%{_datadir}/%{real_name}/resource.dat
#%{_datadir}/Critical_Mass/resource.dat
%{_datadir}/Critical_Mass/*

%changelog
* Wed Aug 31 2005 C.Lee Taylor <leet@leenx.co.za> 0.9.12-0
- Initial package
