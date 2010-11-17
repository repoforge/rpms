# $Id$
# Authority: dag
# Upstream: Michael G Schwern <schwern$pobox,com>

### EL6 ships with perl-Test-Simple-0.92-115.el6
%{?el6:# Tag: rfx}

### From RH9 onwards perl(Test::Simple) is provided by the perl package (sigh)
## ExclusiveDist: el2 rh7

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Simple

Summary: Basic utilities for writing tests
Name: perl-Test-Simple
Version: 0.94
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Simple/

Source: http://www.cpan.org/modules/by-module/Test/Test-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Test::Harness) >= 2.03


### Obsolete wrong packages from the past
Obsoletes: perl-Test-Builder-Tester
Provides: perl-Test-Builder-Tester

%description
This is a simplified Perl testing framework for creating tests to be
run either standalone or under Test::Harness.

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
%doc Changes MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Test::*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Builder/
%{perl_vendorlib}/Test/Builder.pm
%{perl_vendorlib}/Test/More.pm
%{perl_vendorlib}/Test/Simple.pm
%{perl_vendorlib}/Test/Tutorial.pod

%changelog
* Fri Sep  4 2009 Christoph Maser <cmr@financial.com> - 0.94-1
- Updated to version 0.94.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.92-1
- Updated to version 0.92.

* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 0.90-1
- Updated to version 0.90.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 0.78-1
- Updated to release 0.78.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.75-1
- Updated to release 0.75.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.74-1
- Updated to release 0.74.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.72-1
- Updated to release 0.72.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.62-1
- Initial package. (using DAR)
