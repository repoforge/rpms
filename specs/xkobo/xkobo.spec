# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define _bindir /usr/X11R6/bin
%define real_version 1.11+w01

Summary: Space arcade game
Name: xkobo
Version: 1.11
Release: 3
Group: Amusements/Games
License: GPL
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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Xkobo
Comment=Destroy enemy ships and enemy constructions
Icon=redhat-games.png
Exec=%{_bindir}/xkobo
Terminal=false
Type=Application
Categories=GNOME;Application;Game;ArcadeGame;
EOF

%build
xmkmf -a
%{__make} %{?_smp_mflags} xkobo

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0775 %{buildroot}%{_localstatedir}/lib/games/xkobo/ \
			%{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man6/
%{__install} -m2755 xkobo %{buildroot}%{_bindir}
%{__install} -m0644 xkobo.man %{buildroot}%{_mandir}/man6/xkobo.6

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Games/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Games/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/*
%if %{dfi}
        %{_datadir}/gnome/apps/Games/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif
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
