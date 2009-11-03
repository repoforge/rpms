# $Id$
# Authority: dries
# Upstream: Matteo Corti <matteo$corti,gmail,com>

Summary: Rolls dices
Name: roll
Version: 1.1.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://matteocorti.ch/software/roll.html

Source: http://matteocorti.ch/software/roll/roll-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
roll is a command-line program that rolls a user-defined dice sequence
and displays the result. The die are defined using dN, where N is the
number of sides. They can be rolled multiple times by prepending the
number of repetitions (e.g., 3d6) and used in simple mathematical
expressions (e.g., 2d8+4).

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/roll.1*
%{_bindir}/roll

%changelog
* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.4-1
- Updated to release 1.1.4.

* Tue Jan 29 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.3-1
- Updated to release 1.1.3.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Fri Mar 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Initial package.
