# $Id$
# Authority: dries
# Upstream: Andrew Turner <turner$mikomi,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Abstract

Summary: DBI SQL abstraction
Name: perl-DBIx-Abstract
Version: 1.006
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Abstract/

Source: http://search.cpan.org/CPAN/authors/id/T/TU/TURNERA/DBIx-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides methods for doing manipulating database tables This
module provides methods retreiving and storing data in SQL databases.
It provides methods for all of the more important SQL commands (like
SELECT, INSERT, REPLACE, UPDATE, DELETE).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/Abstract.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.006-1
- Updated to release 1.006.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.005-1
- Initial package.
