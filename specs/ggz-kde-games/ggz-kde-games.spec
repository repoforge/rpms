# $Id$
# Authority: dries

Summary: KDE games for GGZ gamingzone
Name: ggz-kde-games
Version: 0.0.14
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-kde-games-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libggz-devel

%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries, 
games and game-related applications for client-server online gaming. Player 
rankings, game spectators, AI players and a chat bot are part of this effort.

This package contains games for GGZ based on KDE.

%prep
%setup
# otherwise: ai.c:383: error: syntax error before ‘/’ token
%{__perl} -pi -e "s|//.*||g;" koenig/ai.c

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__mv} %{buildroot}%{_sysconfdir}/ggz.modules %{buildroot}%{_sysconfdir}/ggz.modules.kde-games

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man6/muehle-ai*
%{_sysconfdir}/ggz.modules*
%{_libdir}/ggz/
%{_datadir}/applications/*.desktop
%{_datadir}/apps/ggz.kreversi/
%{_datadir}/apps/kconnectx/
%{_datadir}/apps/koenig/
%{_datadir}/apps/ktictactux/
%{_datadir}/config/*rc
%{_docdir}/HTML/en/muehle/
%{_datadir}/ggz/
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/locale/*/*/*.mo

%changelog
* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.14-1
- Updated to release 0.0.14.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
