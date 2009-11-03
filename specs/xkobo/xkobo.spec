# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_version 1.11+w01

Summary: Space arcade game
Name: xkobo
Version: 1.11
Release: 3.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://seki.math.hokudai.ac.jp:20080/xkobo-current.html

Source: http://www.redhead.dk/download/pub/Xkobo/xkobo-%{real_version}.tar.gz
Patch0: xkobo-1.11+w01-imake.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

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
%{__install} -Dp -m2755 xkobo %{buildroot}%{_bindir}/xkobo
%{__install} -Dp -m0644 xkobo.man %{buildroot}%{_mandir}/man6/xkobo.6

%{__install} -d -m0775 %{buildroot}%{_localstatedir}/lib/games/xkobo/

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 xkobo.desktop %{buildroot}%{_datadir}/gnome/apps/Games/xkobo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xkobo.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%doc %{_mandir}/man6/xkobo.6*
%{_bindir}/xkobo
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/xkobo.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xkobo.desktop}

%defattr(-, root, games, 0775)
%{_localstatedir}/lib/games/xkobo/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-3.2
- Rebuild for Fedora Core 5.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 1.11-3
- Added desktop-file.
- Fixed group ownership/permissions of highscoredir. (Konrad Kosmowski)

* Fri Dec 27 2002 Dag Wieers <dag@wieers.com> - 1.11-1
- Added documentation and license.

* Fri May 03 2002 Kenneth 'Redhead' Nielsen <kn@redhead.dk> - 1.11
- Found that Wolfgang J�rling <wolfgang@pro-linux.de> had added some
  more levels and enemies to xkobo.

* Wed May 01 2002 Kenneth 'Redhead' Nielsen <kn@redhead.dk>
- Added a patch to accommodate the new strong type checking in todays
  compilers.
- Changed the source location, since Akira seems to have gone of the net.

* Tue Sep 22 1998 Kjetil Wiekhorst Jrgensen <jorgens@pvv.org> [1.11-1]
- upgraded to version 1.11
