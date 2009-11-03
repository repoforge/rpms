# $Id$
# Authority: dries
# Upstream: <lincity-users$lists,sourceforge,net>

# Screenshot: http://lincity.sf.net/screenshots/power.png
# ScreenshotURL: http://lincity.sf.net/screenshots/index.html


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

Summary: City simulation game
Name: lincity
Version: 1.13.1
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://lincity.sourceforge.net/

Source: http://dl.sf.net/lincity/lincity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libpng-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_modxorg:BuildRequires: libX11-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Lincity is a city simulation game. Build your city up from a primitive
village to an advanced civilization. Build a sustainable economy, or build
rockets to escape from a pollution ridden and resource starved planet.

%prep
%setup

%{__cat} <<EOF >lincity.desktop
[Desktop Entry]
Name=Lincity
Comment=Build and manage your own city
Exec=xlincity
Version=1.0
Type=Application
Encoding=UTF-8
Categories=Application;Game;ArcadeGame;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 lincity.desktop %{buildroot}%{_datadir}/gnome/apps/Games/lincity.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		lincity.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT README TODO
%doc %{_mandir}/man6/*
%{_bindir}/xlincity
%{_datadir}/lincity/
%{!?_without_freedesktop:%{_datadir}/applications/net-lincity.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/lincity.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.13.1-1.2
- Rebuild for Fedora Core 5.

* Tue Jul 13 2004 Dries Verachtert <dries@ulyssis.org> 1.13.1-1
- Update to version 1.13.1.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-2
- added a desktop file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.12.0-1
- first packaging for Fedora Core 1
