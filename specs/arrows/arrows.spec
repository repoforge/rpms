# $Id$
# Authority: dag

%define _bindir %{_prefix}/X11R6/bin

Summary: Neat little maze game
Name: arrows
Version: 0.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://noreason.ca/?file=software

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://noreason.ca/data/arrows-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
It's a maze game of sorts. Guide the spinning blue thing through
the maze of arrows, creating and destroying arrows as necessary
to collect the green things.

%prep
%setup

%{__cat} <<EOF >arrows.desktop
[Desktop Entry]
Name=Arrows
Comment=Follow the arrows to reach the exit
Icon=redhat-games.png
Exec=%{_bindir}/arrows
Terminal=false
Type=Application
Categories=GNOME;Application;Game;ArcadeGame;
EOF

%build
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 arrows %{buildroot}%{_bindir}/arrows

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Wed Jan 14 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Fixed %{_bindir} for games.

* Tue Jan 13 2004 Dag Wieers <dag@wieers.com> - 0.6-0
- Initial package. (using DAR)
