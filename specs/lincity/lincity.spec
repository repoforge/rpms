# $Id$
# Authority: dries
# Upstream: <lincity-users@lists.sf.net>
# Screenshot: http://lincity.sf.net/screenshots/power.png
# ScreenshotURL: http://lincity.sf.net/screenshots/index.html

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: City simulation game
Name: lincity
Version: 1.13.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://lincity.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/lincity/lincity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, XFree86-devel

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

%if %{dfi}
	%{__install} -D -m0644 lincity.desktop %{buildroot}%{_datadir}/gnome/apps/Games/lincity.desktop
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
%{_datadir}/lincity
%if %{dfi}
	%{_datadir}/gnome/apps/Games/*.desktop
%else   
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Tue Jul 13 2004 Dries Verachtert <dries@ulyssis.org> 1.13.1-1
- Update to version 1.13.1.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-2
- added a desktop file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.12.0-1
- first packaging for Fedora Core 1
