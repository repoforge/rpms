# $Id$
# Authority: dag
# Upstream: Simon Cozens

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Inflect-Number

Summary: Perl module to force number of words to singular or plural
Name: perl-Lingua-EN-Inflect-Number
Version: 1.1
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Inflect-Number/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-Inflect-Number-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lingua-EN-Inflect-Number is a Perl module to force number of words
to singular or plural.

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
%doc %{_mandir}/man3/Lingua::EN::Inflect::Number.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/EN/
%dir %{perl_vendorlib}/Lingua/EN/Inflect/
#%{perl_vendorlib}/Lingua/EN/Inflect/Number/
%{perl_vendorlib}/Lingua/EN/Inflect/Number.pm

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
