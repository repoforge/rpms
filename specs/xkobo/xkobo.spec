# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define real_version 1.11+w01

Summary: Space arcade game
Name: xkobo
Version: 1.11
Release: 3
License: GPL
Group: Amusements/Games
URL: http://seki.math.hokudai.ac.jp:20080/xkobo-current.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.redhead.dk/download/pub/Xkobo/xkobo-%{real_version}.tar.gz
Patch0: xkobo-1.11+w01-imake.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Xkobo is a arcade video game for X11. The goal is to
destroy the enemi bases. But the enemi will fire at
you and send fighter spacecrafts to get you. You'll
have hours and hours of fun with this game.

%prep
%setup -n %{name}-%{real_version}
%patch0 -p1

%{__cat} <<EOF >xkobo.desktop
[Desktop Entry]
Name=Xkobo
Comment=Destroy enemy ships and enemy constructions
Exec=xkobo
Icon=redhat-games.png
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
EOF

%build
xmkmf -a
%{__make} %{?_smp_mflags} xkobo

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m2755 xkobo %{buildroot}%{_bindir}/xkobo
%{__install} -D -m0644 xkobo.man %{buildroot}%{_mandir}/man6/xkobo.6
%{__install} -d -m0775 %{buildroot}%{_localstatedir}/lib/games/xkobo/

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 xkobo.desktop %{buildroot}%{_datadir}/gnome/apps/Games/xkobo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xkobo.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/xkobo.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/net-xkobo.desktop}

%defattr(-, root, games, 0775)
%{_localstatedir}/lib/games/xkobo/

%changelog
* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 1.11-3
- Added desktop-file.
- Fixed group ownership/permissions of highscoredir. (Konrad Kosmowski)

* Fri Dec 27 2002 Dag Wieers <dag@wieers.com> - 1.11-1
- Added documentation and license.

* Fri May 03 2002 Kenneth 'Redhead' Nielsen <kn@redhead.dk> - 1.11
- Found that Wolfgang Jährling <wolfgang@pro-linux.de> had added some 
  more levels and enemies to xkobo. 

* Wed May 01 2002 Kenneth 'Redhead' Nielsen <kn@redhead.dk>
- Added a patch to accommodate the new strong type checking in todays
  compilers. 
- Changed the source location, since Akira seems to have gone of the net.

* Tue Sep 22 1998 Kjetil Wiekhorst Jørgensen <jorgens@pvv.org> [1.11-1]
- upgraded to version 1.11
