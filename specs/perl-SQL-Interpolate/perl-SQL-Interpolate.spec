# $Id$
# Authority: dries
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Interpolate

Summary: Interpolate Perl variables into SQL statements
Name: perl-SQL-Interpolate
Version: 0.41
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Interpolate/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Interpolate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Interpolate Perl variables into SQL statements.

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
%doc Changes README
%doc %{_mandir}/man3/SQL::Interpolate*
%doc %{_mandir}/man3/DBIx::Interpolate*
%{perl_vendorlib}/SQL/Interpolate.pm
%{perl_vendorlib}/SQL/Interpolate/
%{perl_vendorlib}/DBIx/Interpolate.pm

%changelog
* Wed Jul  1 2009 Christoph Maser <cmr@financial.com> - 0.41-1
- Updated to version 0.41.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
