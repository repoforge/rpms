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

Source: http://atomorun.whosme.de/downloads/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: gcc, SDL-devel, SDL_mixer-devel, SDL_image-devel, sed
Requires: SDL, SDL_mixer, SDL_image

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n atomorun-1.1_pre2

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
sed -i "s/^DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}\//g" $(find . -type f | egrep "Makefile$")
make install-strip
rm -Rf $RPM_BUILD_ROOT/usr/doc/atomorun 
mkdir -p ${RPM_BUILD_ROOT}/usr/share/applications
cat > ${RPM_BUILD_ROOT}/usr/share/applications/atomorun.desktop <<EOF
[Desktop Entry]
Name=Atomorun
Comment=A 3D multi-player tank battle game.
Exec=atomorun
Terminal=0
Type=Application
Encoding=UTF-8
Categories=Game;Application;X-Red-Hat-Extra;
EOF

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
${_bindir}/atomorun
/usr/share/atomorun/atom.ogg
/usr/share/atomorun/explode.ogg
/usr/share/atomorun/ingame_music.ogg
/usr/share/atomorun/jump.ogg
/usr/share/atomorun/menu_change.ogg
/usr/share/atomorun/pixmaps/acid.png
/usr/share/atomorun/pixmaps/acidfog.png
/usr/share/atomorun/pixmaps/atomorun_icon.png
/usr/share/atomorun/pixmaps/atomorun_winicon.ico
/usr/share/atomorun/pixmaps/b.png
/usr/share/atomorun/pixmaps/font.png
/usr/share/atomorun/pixmaps/g.png
/usr/share/atomorun/pixmaps/g_top.png
/usr/share/atomorun/pixmaps/menu.png
/usr/share/atomorun/pixmaps/skybox.png
/usr/share/atomorun/walk.ogg
/usr/share/atomorun/wind.ogg


%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.1pre2-2
- spec file cleanup

* Sun Dec 21 2003 Dries Verachtert <dries@ulyssis.org> 1.1pre2-1
- first packaging for Fedora Core 1
