# $Id$
# Authority: dries

# problem: the game plays the oggs as a wav with sdl -> doesn't work
# i've send a description of the problem to the author but he didn't respond
# to the last mail

# ExcludeDist: fc1

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_alsa 1}
%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh8:%define _without_alsa 1}
%{?rh7:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}
%{?rh6:%define _without_alsa 1}
%{?yd3:%define _without_alsa 1}

%define prever pre2

Summary: OpenGL Jump&Run game where you have to flee an exploding nuclear bomb
Name: atomorun
Version: 1.1
Release: %{?prever:0.%{prever}.}2.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://atomorun.whosme.de/index.php

Source: http://atomorun.whosme.de/downloads/atomorun-%{version}%{?prever:_%{prever}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel
BuildRequires: libtiff-devel, libvorbis-devel
BuildRequires: libvorbis-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.

%prep
%setup -n %{name}-%{version}%{?prever:_%{prever}}

%{__cat} <<EOF >atomorun.desktop
[Desktop Entry]
Name=Atomorun
Comment=Drive a tank through battle and beat your opponents
Exec=atomorun
Type=Application
Terminal=false
Categories=Application;Game;
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/atomorun
%{_datadir}/atomorun/
%exclude %{_prefix}/doc/atomorun/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-%{?prever:0.%{prever}.}2.2
- Rebuild for Fedora Core 5.

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 1.1-0.pre2.1
- Further cleanups.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.1pre2-2
- Cosmetic cleanup.

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.1pre2-2
- spec file cleanup

* Sun Dec 21 2003 Dries Verachtert <dries@ulyssis.org> 1.1pre2-1
- first packaging for Fedora Core 1
