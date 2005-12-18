# $Id$
# Authority: dries

Summary: Utilities for GGZ gamingzone
Name: ggz-utils
Version: 0.0.12
Release: 1
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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/ggz-cmd
%{_bindir}/ggzcommgen
%{_bindir}/metaserv
%{_bindir}/telggz
%dir %{_datadir}/metaserv/
%config(noreplace) %{_datadir}/metaserv/metaservconf.xml

%changelog
* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
