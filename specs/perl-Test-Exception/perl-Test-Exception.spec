# $Id$
# Authority: dries
# Upstream: Adrian Howard <adrianh$quietstars,com>

### EL6 ships with perl-Test-Exception-0.27-4.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Exception

Summary: Test exception based code
Name: perl-Test-Exception
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Exception/


Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADIE/Test-Exception-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Sub::Uplevel) >= 0.18
BuildRequires: perl(Test::Builder) >= 0.7
#BuildRequires: perl(Test::Builder::Tester) >= 1.07
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.7
BuildRequires: perl(Test::Simple) >= 0.7
Requires: perl(Sub::Uplevel) >= 0.18
Requires: perl(Test::Builder) >= 0.7
#Requires: perl(Test::Builder::Tester) >= 1.07
Requires: perl(Test::Builder::Tester)
Requires: perl(Test::Harness) >= 2.03
Requires: perl(Test::More) >= 0.7
Requires: perl(Test::Simple) >= 0.7

%filter_from_requires /^perl*/d
%filter_setup


%description
This module provides a few convenience methods for testing exception
based code. It is built with Test::Builder and plays happily with
Test::More and friends.

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
%doc %{_mandir}/man3/Test::Exception.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Exception/
%{perl_vendorlib}/Test/Exception.pm

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser@gmx.de> - 0.31-1
- Updated to version 0.31.

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 0.29-1
- Updated to version 0.29.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
