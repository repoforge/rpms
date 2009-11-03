# $Id$
# Authority: dag
# Upstream: Dave Cross <dave$mag-sol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Number-Fraction

Summary: Perl extension to model fractions
Name: perl-Number-Fraction
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Number-Fraction/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Number-Fraction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Perl extension to model fractions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL
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
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.12-1
- Updated to version 1.12.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Initial package. (using DAR)
