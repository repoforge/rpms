# $Id$
# Authority: dries
# Upstream: J. J. Merelo <jmerelo$geneura,ugr,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Evolutionary

Summary: Perl extension for performing paradigm-free evolutionary algorithms
Name: perl-Algorithm-Evolutionary
Version: 0.56
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Evolutionary/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Evolutionary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Algorithm::Permute) >= 0.01
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Math::Random) >= 0.63
BuildRequires: perl(String::Random)
BuildRequires: perl(XML::Parser::EasyTree) >= 0.01

%description
Perl extension for performing paradigm-free evolutionary algorithms.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Algorithm::Evolutionary.3pm*
%doc %{_mandir}/man3/Algorithm::Evolutionary::*.3pm*
%dir %{perl_vendorlib}/Algorithm/
%{perl_vendorlib}/Algorithm/Evolutionary/
%{perl_vendorlib}/Algorithm/Evolutionary.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.56-1
- Updated to release 0.56.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
