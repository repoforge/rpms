# $Id$
# Authority: dag
# Upstream: Rafaël Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-LongString

Summary: Tests strings for equality, with more helpful failures
Name: perl-Test-LongString
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-LongString/

Source: http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Test-LongString-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Builder) >= 0.12
#BuildRequires: perl(Test::Builder::Tester) >= 1.04
BuildRequires: perl(Test::Builder::Tester)
Requires: perl(Test::Builder) >= 0.12
#Requires: perl(Test::Builder::Tester) >= 1.04
Requires: perl(Test::Builder::Tester)

%filter_from_requires /^perl*/d
%filter_setup

Requires: perl

%description
This module provides some drop-in replacements for the string
comparison functions of Test::More, but which are more suitable
when you test against long strings.  If you've ever had to search
for text in a multi-line string like an HTML document, or find
specific items in binary data, this is the module for you.

This package contains the following Perl module:

    Test::LongString

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man3/Test::LongString.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/LongString.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
