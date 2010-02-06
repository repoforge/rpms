# $Id$
# Authority: dries
# Upstream: Florian Ragwitz <rafl@debian.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-C3

Summary: Pragma for the C3 method resolution order algorithm
Name: perl-Class-C3
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-C3/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Class-C3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Algorithm::C3) >= 0.06
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util) >= 1.10
BuildRequires: perl(Test::More) >= 0.47
Requires: perl(Algorithm::C3) >= 0.06
Requires: perl(Scalar::Util) >= 1.10

%filter_from_requires /^perl*/d
%filter_setup

%description
Pragma for the C3 method resolution order algorithm.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Class::C3.3pm*
%doc %{_mandir}/man3/Class::C3::next.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/C3/
%{perl_vendorlib}/Class/C3.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
