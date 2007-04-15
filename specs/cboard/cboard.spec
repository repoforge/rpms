# $Id$
# Authority: dries
# Upstream: Ben Kibbey <bjk$luxsci,net>

Summary: Ncurses PGN editor and front end to chess engines
Name: cboard
Version: 0.3
Release: 1
License: GPL
Group: Entertainment/Games
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man6/cboard*
%{_bindir}/cboard
%{_datadir}/cboard/

%changelog
* Sun Apr 15 2007 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
