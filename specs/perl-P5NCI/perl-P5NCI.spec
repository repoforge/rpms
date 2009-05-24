# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name P5NCI

Summary: Perl extension for loading shared libraries and their functions
Name: perl-P5NCI
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/P5NCI/

Source: http://www.cpan.org/authors/id/C/CH/CHROMATIC/P5NCI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::CBuilder) >= 0.03
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)

%description
Perl extension for loading shared libraries and their functions.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/P5NCI.3pm*
%doc %{_mandir}/man3/P5NCI::*3pm*
%{perl_vendorarch}/auto/P5NCI/
%{perl_vendorarch}/P5NCI/
%{perl_vendorarch}/P5NCI.pm

%changelog
* Sun May 24 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.31-1
- Added a missing BuildRequires: perl-Module-Build

* Sat May 23 2009 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
