# $Id$
# Authority: dries

Summary: GGZ gamingzone documentation
Name: ggz-docs
Version: 0.0.14
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-docs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libggz-devel

%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries, 
games and game-related applications for client-server online gaming. Player 
rankings, game spectators, AI players and a chat bot are part of this effort.

This package contains documentation for GGZ.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_docdir}/ggz-docs rpm-docs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc rpm-docs/*
%doc %{_infodir}/ggz-*.info*

%changelog
* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.14-1
- Updated to release 0.0.14.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
