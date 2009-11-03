# $Id$

# Authority: dries
# Upstream: Calle Laakkonen <calle,laakkonen$saunalahti,fi>
# Screenshot: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/screenshot7.jpg
# ScreenshotURL: http://www.saunalahti.fi/~laakkon1/linux/luola/index.php#screenshots

Summary: Levels for Luola
Name: luola-levels
Version: 1.3.2
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.luolamies.org/software/luola/

Source0: http://www.luolamies.org/software/luola/stdlevels.tar.gz
Source1: http://www.luolamies.org/software/luola/nostalgia-1.0.tar.gz
#Source2: http://www.luolamies.org/software/luola/demolevel.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: luola
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
#%{__tar} -xzvf %{SOURCE2} -C %{buildroot}%{_datadir}/luola/levels

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/luola/levels/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-2
- Fixed the urls.
- 'demolevel' removed, no working url found.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Aug 15 2005 C.Lee Taylor <leet@leenx.co.za> - 1.2.9-2
- Requires luola now.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.9-1
- Update to release 1.2.9.

* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Update to release 1.2.7.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
