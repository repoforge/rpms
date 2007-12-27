# $Id$
# Authority: dries
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-DBSchema

Summary: Interface to database schemas
Name: perl-DBIx-DBSchema
Version: 0.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-DBSchema/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-DBSchema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/DBIx::DBSchema.3pm*
%doc %{_mandir}/man3/DBIx::DBSchema::*.3pm*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/DBSchema/
%{perl_vendorlib}/DBIx/DBSchema.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
