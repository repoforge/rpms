# $Id: $

# Authority: dries
# Upstream: klnavarro$free,fr


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: 3D Space Flight Simulator
Name: stardust
Version: 0.1.10
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://startracker.free.fr/stardust/stardust_en.html

Source: http://startracker.free.fr/stardust/stardust-%{version}.tar.gz
Patch0: gcc-fc3-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: autoconf, automake, SDL-devel, zlib-devel
BuildRequires: libxml2-devel, libtiff-devel

%description
The goal of Stardust is to create a 3D-Space Fight Simulator Open Source,
portable and expandable simulating, at best, the kinematics of space flight.
Stardust will feature small dozens of starfighters, intelligent computer
enemies and network mode.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Stardust
Comment=3D Space Flight Simulator
Exec=stardust
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/games/stardust

%changelog
* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.10-1
- Updated to release 0.1.10.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.9-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Mon Aug 09 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.9-1
- Initial package.
