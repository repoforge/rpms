# $Id$
# Authority: dries

# problem: the game plays the oggs as a wav with sdl -> doesn't work
# i've send a description of the problem to the author but he didn't respond 
# to the last mail

Summary: OpenGL Jump&Run game where you have to flee an exploding nuclear bomb
Name: atomorun
Version: 1.1_pre2
Release: 2
License: GPL
Group: Amusements/Games
URL: http://atomorun.whosme.de/index.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://atomorun.whosme.de/downloads/atomorun-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, libtiff-devel

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.

%prep
%setup -n atomorun-1.1_pre2

%{__cat} <<EOF >atomorun.desktop
[Desktop Entry]
Name=Atomorun
Comment=Drive a tank through battle and beat your opponents
Exec=atomorun
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/atomorun
%{_datadir}/atomorun/
%exclude %{_prefix}/doc/atomorun/

%changelog
* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.1pre2-2
- Cosmetic cleanup.

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.1pre2-2
- spec file cleanup

* Sun Dec 21 2003 Dries Verachtert <dries@ulyssis.org> 1.1pre2-1
- first packaging for Fedora Core 1
