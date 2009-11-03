# $Id$
# Authority: dag
# Upstream: Marvin Humphrey <marvin$rectangular,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name KinoSearch

Summary: Search engine library
Name: perl-KinoSearch
Version: 0.165
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/KinoSearch/

Source: http://www.cpan.org/authors/id/C/CR/CREAMYG/KinoSearch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Lingua::StopWords)
BuildRequires: perl(Lingua::Stem::Snowball)

Requires: perl >= 2:5.8.3

%description
Search engine library.

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
%doc ApacheLicense2.0.txt Changes MANIFEST META.yml README
%doc %{_mandir}/man3/KinoSearch.3pm*
%doc %{_mandir}/man3/KinoSearch::*.3pm*
%{perl_vendorarch}/auto/KinoSearch/
%{perl_vendorarch}/KinoSearch/
%{perl_vendorarch}/KinoSearch.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.165-1
- Updated to version 0.165.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.163-1
- Updated to release 0.163.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.162-1
- Initial package. (using DAR)
