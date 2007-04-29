# $Id$
# Authority: dries
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-DBSchema

Summary: Interface to database schemas
Name: perl-DBIx-DBSchema
Version: 0.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-DBSchema/

Source: http://search.cpan.org/CPAN/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements an OO-interface to database schemas.  Using this module,
you can create a database schema with an OO Perl interface.  You can read the
schema from an existing database.  You can save the schema to disk and restore
it from different process.  Most importantly, DBIx::DBSchema can write SQL
CREATE statements for different databases from a single source.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/DBSchema.pm
%{perl_vendorlib}/DBIx/DBSchema/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.28-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
