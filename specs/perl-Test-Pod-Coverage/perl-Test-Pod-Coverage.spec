# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

### EL6 ships with perl-Test-Pod-Coverage-1.08-8.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Pod-Coverage

Summary: Checks for POD Coverage in your distribution
Name: perl-Test-Pod-Coverage
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Pod-Coverage/

Source: http://www.cpan.org/modules/by-module/Test/Test-Pod-Coverage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module allows you to check for pod coverage in your distribution.

This package contains the following Perl module:

    Test::Pod::Coverage

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Test::Pod::Coverage.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Pod/
#%{perl_vendorlib}/Test/Pod/Coverage/
%{perl_vendorlib}/Test/Pod/Coverage.pm

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 1.08-1
- Initial package.
