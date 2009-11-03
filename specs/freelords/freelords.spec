# $Id$
# Authority: dries
# Upstream: Ulf Lorenz <ulf82$users,sf,net>

Summary: Turn-based strategy game
Name: freelords
Version: 0.3.7
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://freelords.sourceforge.net/

Source: http://dl.sf.net/freelords/freelords-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: paragui-devel, gcc-c++, SDL-devel, gettext, pkgconfig
BuildRequires: SDL_image-devel, libsigc++-devel, SDL_mixer-devel

%description
Freelords is a rewrite of the well-known Warlords II. It mainly resembles
Warlords, but also extends the game, e.g. units have hit points and the
save, and configuration files have an easy-to-read XML format.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall FREELORDS_DATADIR=%{buildroot}%{_datadir}/freelords
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/freelords
%{_bindir}/freelords_editor
%{_bindir}/freelords_server
%{_datadir}/applications/freelords.desktop
%{_datadir}/freelords/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.7-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.7-1
- Updated to release 0.3.7.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.6-1
- Initial package.
