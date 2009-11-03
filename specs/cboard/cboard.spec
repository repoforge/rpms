# $Id$
# Authority: dries
# Upstream: Ben Kibbey <bjk$luxsci,net>

Summary: Ncurses PGN editor and front end to chess engines
Name: cboard
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://bjk.sourceforge.net/cboard/

Source: http://dl.sf.net/bjk/cboard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
CBoard is an NCurses PGN browser, editor, and front end to chess engines that 
use the XBoard protocol. It supports human/human (local), human/engine, and 
engine/engine play, the FEN tag, annotations with RAV (limited), NAG, and 
comments, and more.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man6/cboard.6*
%{_bindir}/cboard
%{_datadir}/cboard/

%changelog
* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 0.3-2
- Fix group tag.

* Sun Apr 15 2007 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
