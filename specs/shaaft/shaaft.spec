# $Id$
# Authority: dries

# Screenshot: http://criticalmass.sourceforge.net/images-shaaft/shaaft02.jpg


Summary: OpenGL 3D falling block game
Name: shaaft
Version: 0.5.0
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://criticalmass.sourceforge.net/shaaft.php

Source: http://dl.sf.net/criticalmass/Shaaft-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, zlib-devel
BuildRequires: libpng-devel, gcc-c++, desktop-file-utils

%description
Shaaft is an OpenGL 3D falling block game similar to Blockout. It currently
runs on Linux and Windows. There is still a lot missing. No menu system,
forgets highscore, some of the sound effects need work (Clearing a single
plane sounds like a f*rt. Try clearing >1 plane, though...), etc. That said,
I find it is very playable. Enjoy!

%prep
%setup -n Shaaft-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Shaaft
Comment=OpenGL 3D falling block game
Exec=shaaft
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
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
%{_datadir}/applications/*.desktop
%{_datadir}/Shaaft/resource.dat

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org>
- Initial package.
