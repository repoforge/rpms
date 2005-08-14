# $Id$

# Authority: dries
# Upstream: Calle Laakkonen <calle,laakkonen$saunalahti,fi>
# Screenshot: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/screenshot7.jpg
# ScreenshotURL: http://www.saunalahti.fi/~laakkon1/linux/luola/index.php#screenshots

Summary: Levels for Luola
Name: luola-levels
Version: 1.2.9
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.saunalahti.fi/~laakkon1/linux/luola/index.php

Source0: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/stdlevels.tar.gz
Source1: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/nostalgy.tar.gz
Source2: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/demolevel.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# Dist: nodist

%description
Luola is a 2D arcade game where you fly a small V shaped ship in different
kinds of levels. It's genre "Luolalentely" (Cave-flying) is (or was) very
popular here in Finland. Though cavern-flying games are not originally
Finnish, nowdays most of them are.

This package contains the levels of Luola.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/luola/levels
%{__tar} -xzvf %{SOURCE0} -C %{buildroot}%{_datadir}/luola/levels
%{__tar} -xzvf %{SOURCE1} -C %{buildroot}%{_datadir}/luola/levels
%{__tar} -xzvf %{SOURCE2} -C %{buildroot}%{_datadir}/luola/levels

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/luola/levels/*

%changelog
* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.9-1
- Update to release 1.2.9.

* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Update to release 1.2.7.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
