# $Id: $

# Authority: dries
# Upstream: 

Summary: Shoot'em up arcade game
Name: dd2
Version: 0.2
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.usebox.net/jjm/dd2/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.usebox.net/jjm/dd2/releases/dd2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_mixer-devel

%description
This is a little shoot'em up arcade game for one or two players. It aims to
be an 'old school' arcade game with low resolution graphics, top-down scroll
action, energy based gameplay and different weapons with several levels of
power. 

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Dodgin' Diamond 2
Comment=Shoot'em up arcade game
Exec=dd2
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;ArcadeGame;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
rm -Rf %{buildroot}/usr/share/doc/dd2

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/dd2
%{_datadir}/applications/*.desktop

%changelog
* Sat May 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.

