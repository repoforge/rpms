# $Id: $

# Authority: dries
# Upstream: 

Summary: Mash the monsters with stone blocks
Name: monstermasher
Version: 1.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.cs.aau.dk/~olau/monster-masher/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cs.aau.dk/~olau/monster-masher/source/monster-masher-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, gtk+-devel

# Screenshot: http://www.cs.aau.dk/~olau/monster-masher/level-23.jpg
# ScreenshotURL: http://www.cs.aau.dk/~olau/monster-masher/screenshots.html

%description
Monster Masher is an action game for the Gnome desktop environment. The
basic idea is that you, as levitation worker gnome, has to clean the caves
for monsters that want to roll over you. You do the cleaning by mashing the
monsters with stone blocks.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.

