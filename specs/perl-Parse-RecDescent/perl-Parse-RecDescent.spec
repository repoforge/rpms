# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-RecDescent

Summary: Generate Recursive-Descent Parsers
Name: perl-Parse-RecDescent
Version: 1.962.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-RecDescent/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-RecDescent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
RecDescent incrementally generates top-down recursive-descent text
parsers from simple yacc-like grammar specifications.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Parse/RecDescent.p*

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.962.2-1
- Updated to version 1.962.2.

* Sun May  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.94-1
- Initial package.
