# $Id$
# Authority: dag
# Upstream: Dave Cross <dave$dave,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Number-Fraction

Summary: Perl extension to model fractions
Name: perl-Number-Fraction
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Number-Fraction/

Source: http://www.cpan.org/modules/by-module/Number/Number-Fraction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension to model fractions.

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
%doc %{_mandir}/man3/Number::Fraction.3pm*
%dir %{perl_vendorlib}/Number/
#%{perl_vendorlib}/Number/Fraction/
%{perl_vendorlib}/Number/Fraction.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Initial package. (using DAR)
