# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Base36

Summary: Encoding and decoding of base36 strings
Name: perl-Math-Base36
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Base36/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Math-Base36-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Math::BigInt) >= 1.60
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.0
Requires: perl(Math::BigInt) >= 1.60
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Encoding and decoding of base36 strings.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Base36.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/Base36/
%{perl_vendorlib}/Math/Base36.pm

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
