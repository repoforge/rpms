# $Id$
# Authority: dries
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Util-Calc

Summary: DateTime calculation utilities
Name: perl-DateTime-Util-Calc
Version: 0.13002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-Calc/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Util-Calc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Module::Build)
BuildRequires: perl(Math::BigInt::GMP)
BuildRequires: perl(Math::BigInt::FastCalc)
BuildRequires: perl(Math::Round)
BuildRequires: perl(DateTime)
BuildRequires: perl(Test::More)
Requires: perl >= 1:5.6.1

%description
A perl module with additional DateTime calculation utilities.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST META.yml
%doc %{_mandir}/man3/DateTime::Util::Calc.3pm*
#%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Util/
%{perl_vendorlib}/DateTime/Util/Calc.pm

%changelog
* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 0.13002-1
- Updated to release 0.13002.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
