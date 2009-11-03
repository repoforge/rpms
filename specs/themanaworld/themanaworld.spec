# $Id$
# Authority: dries

Summary: Innovative free MMORPG with 2D graphics
Name: themanaworld
Version: 0.0.23
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://themanaworld.org/

Source: http://dl.sf.net/themanaworld/tmw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, guichan-devel, physfs-devel, gcc-c++
BuildRequires: curl-devel, libxml2-devel, SDL_image-devel
BuildRequires: SDL_mixer-devel, SDL_net-devel, libpng-devel

%description
The Mana World (TMW) is a serious effort to create an innovative free and
open source MMORPG. It uses 2D graphics and aims to create a large and
diverse interactive world. The game aims to be a unique place for people to
interact not only by fighting each other but to play life, form a community
within the community, or just simply chat. Although the game is never-ending
and a linear story cannot be applied, it should have enough background to
describe and predefine tribes, kingdoms, and the environment overall.
Fullfilled quests should lead to certain events depending on them being
solved. Quests should also encourage teamwork.

%prep
%setup -n tmw-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man6/tmw.6*
%{_bindir}/tmw
%{_datadir}/pixmaps/tmw.png
%{_datadir}/applications/tmw.desktop
%{_datadir}/tmw/

%changelog
* Thu May 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.23-1
- Updated to release 0.0.23.

* Sat Dec 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.21.1-1
- Updated to release 0.0.21.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.18-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.18-1
- Updated to release 0.0.18.

* Thu Oct 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.17-1
- Initial package.
