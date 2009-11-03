# $Id$
# Authority: dries

Summary: Text client for GGZ gamingzone
Name: ggz-txt-client
Version: 0.0.14
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-txt-client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libggz-devel

%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries, 
games and game-related applications for client-server online gaming. Player 
rankings, game spectators, AI players and a chat bot are part of this effort.
This package contais a text client for GGZ gamingzone.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang ggz-txt
%{__mv} %{buildroot}%{_sysconfdir}/ggz.modules %{buildroot}%{_sysconfdir}/ggz.modules.txt-client

%clean
%{__rm} -rf %{buildroot}

%files -f ggz-txt.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man6/ggz-txt*
%{_sysconfdir}/ggz.modules*
%{_bindir}/ggz-txt
%{_libdir}/ggz/tttxt
%{_datadir}/applications/ggz-txt.desktop
%{_datadir}/locale/*/*/ggz-txt.*

%changelog
* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.14-1
- Updated to release 0.0.14.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
