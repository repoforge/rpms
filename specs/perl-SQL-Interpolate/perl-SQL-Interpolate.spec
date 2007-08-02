# $Id$
# Authority: dries
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Interpolate

Summary: Interpolate Perl variables into SQL statements
Name: perl-SQL-Interpolate
Version: 0.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Interpolate/

Source: http://search.cpan.org//CPAN/authors/id/D/DM/DMANURA/SQL-Interpolate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Interpolate Perl variables into SQL statements.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

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
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
