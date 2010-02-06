# $Id$
# Authority: dries
# Upstream: J. J. Merelo <jmerelo$geneura,ugr,es>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Evolutionary

Summary: Perl extension for performing paradigm-free evolutionary algorithms
Name: perl-Algorithm-Evolutionary
Version: 0.72
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Evolutionary/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMERELO/Algorithm-Evolutionary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Algorithm::Permute) >= 0.01
BuildRequires: perl(B::Deparse) >= 0.56
BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Clone::Fast)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(GD) >= 2.17
BuildRequires: perl(Math::Random) >= 0.63
BuildRequires: perl(Memoize)
BuildRequires: perl(Object::Array)
BuildRequires: perl(Pod::Escapes)
BuildRequires: perl(Statistics::Basic) >= 1.6
BuildRequires: perl(String::Random)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Simple) >= 0.44
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Tree::DAG_Node) >= 1.04
BuildRequires: perl(XML::LibXML) >= 1.5
BuildRequires: perl(XML::Parser)
BuildRequires: perl(XML::Parser::Style::EasyTree) >= 0.01
BuildRequires: perl(YAML)
BuildRequires: perl(constant)
BuildRequires: perl(version)
Requires: perl(Algorithm::Permute) >= 0.01
Requires: perl(B::Deparse) >= 0.56
Requires: perl(Bit::Vector)
Requires: perl(Clone::Fast)
Requires: perl(GD) >= 2.17
Requires: perl(Math::Random) >= 0.63
Requires: perl(Memoize)
Requires: perl(Object::Array)
Requires: perl(Pod::Escapes)
Requires: perl(Statistics::Basic) >= 1.6
Requires: perl(String::Random)
Requires: perl(Test::More)
Requires: perl(Test::Pod)
Requires: perl(Test::Simple) >= 0.44
Requires: perl(Time::HiRes)
Requires: perl(Tree::DAG_Node) >= 1.04
Requires: perl(XML::LibXML) >= 1.5
Requires: perl(XML::Parser)
Requires: perl(XML::Parser::Style::EasyTree) >= 0.01
Requires: perl(YAML)
Requires: perl(constant)
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup


%description
Perl extension for performing paradigm-free evolutionary algorithms.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc Changes LICENSE MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/Algorithm::Evolutionary.3pm*
%doc %{_mandir}/man3/Algorithm::Evolutionary::*.3pm*
%doc %{_mandir}/man1/canonical-genetic-algorithm.pl.1.gz
%doc %{_mandir}/man1/rectangle-coverage.pl.1.gz
%doc %{_mandir}/man1/tide_bitstring.pl.1.gz
%doc %{_mandir}/man1/tide_float.pl.1.gz
%dir %{perl_vendorlib}/Algorithm/
%{perl_vendorlib}/Algorithm/Evolutionary/
%{perl_vendorlib}/Algorithm/Evolutionary.pm
%{_bindir}/canonical-genetic-algorithm.pl
%{_bindir}/rectangle-coverage.pl
%{_bindir}/tide_bitstring.pl
%{_bindir}/tide_float.pl





%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.72-1
- Updated to version 0.72.

* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.71-1
- Updated to version 0.71.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.56-1
- Updated to release 0.56.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
