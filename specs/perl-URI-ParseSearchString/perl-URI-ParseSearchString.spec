# $Id$
# Authority: dries
# Upstream: Spiros Denaxas <spiros$lokku,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-ParseSearchString

Summary: Parse Apache referer logs and extract search engine query strings
Name: perl-URI-ParseSearchString
Version: 3.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-ParseSearchString/

Source: http://www.cpan.org/modules/by-module/URI/URI-ParseSearchString-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More)    conflicts with perl package
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(URI)
#Requires: perl(Test::More)   conflicts with perl package
Requires: perl(Test::NoWarnings)
Requires: perl(URI)

%filter_from_requires /^perl*/d
%filter_setup

%description
Parse referer logs for search engine query strings.

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/URI::ParseSearchString.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/ParseSearchString/
%{perl_vendorlib}/URI/ParseSearchString.pm

%changelog
* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 3.2-1
- Updated to version 3.2.

* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 3.1-1
- Updated to version 3.1.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 3.0-1
- Updated to version 3.0.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Initial package.
