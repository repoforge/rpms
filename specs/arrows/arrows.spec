# $Id$
# Authority: dag

%define desktop_vendor rpmforge

%define _bindir %{_prefix}/X11R6/bin

Summary: Neat little maze game
Name: arrows
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://noreason.ca/?file=software

Source: http://noreason.ca/data/arrows-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, desktop-file-utils

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
%{__install} -Dp -m0755 arrows %{buildroot}%{_bindir}/arrows

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	arrows.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/arrows
%{_datadir}/applications/%{desktop_vendor}-arrows.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Wed Jan 14 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Fixed %{_bindir} for games.

* Tue Jan 13 2004 Dag Wieers <dag@wieers.com> - 0.6-0
- Initial package. (using DAR)
