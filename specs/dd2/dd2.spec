# $Id$
# Authority: dries
# Upstream: Juan J. Martínez <jjm$usebox,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Shoot'em up arcade game
Name: dd2
Version: 0.2.1
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.usebox.net/jjm/dd2/

Source: http://www.usebox.net/jjm/dd2/releases/dd2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils

%description
This is a little shoot'em up arcade game for one or two players. It aims to
be an 'old school' arcade game with low resolution graphics, top-down scroll
action, energy based gameplay and different weapons with several levels of
power.

%prep
%setup

%{__cat} <<EOF >dd2.desktop
[Desktop Entry]
Name=Dodgin' Diamond 2
Comment=Shoot'em up arcade game
Icon=redhat-games.png
Exec=dd2
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;ArcadeGame;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}/usr/share/doc/dd2/

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 dd2.desktop \
		%{buildroot}%{_datadir}/gnome/apps/Games/dd2.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		dd2.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/dd2/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/dd2.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/net-dd2.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1.2
- Rebuild for Fedora Core 5.

* Mon Jul 12 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Updated to release 0.2.1.

* Sat May 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
