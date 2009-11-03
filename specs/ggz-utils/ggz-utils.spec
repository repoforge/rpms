# $Id$
# Authority: dries

Summary: Utilities for GGZ gamingzone
Name: ggz-utils
Version: 0.0.14
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libggz-devel, gcc-c++, gettext, ggz-client-libs-devel

%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries,
games and game-related applications for client-server online gaming. Player
rankings, game spectators, AI players and a chat bot are part of this effort.

This pacakge contains some utilities for GGZ gaming zone.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/ggz-cmd
%{_bindir}/ggzcommgen
%{_bindir}/ggzmetaserv
%{_bindir}/telggz
%dir %{_datadir}/ggzmetaserv/
%config(noreplace) %{_datadir}/ggzmetaserv/metaservconf.xml

%changelog
* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.14-1
- Updated to release 0.0.14.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
