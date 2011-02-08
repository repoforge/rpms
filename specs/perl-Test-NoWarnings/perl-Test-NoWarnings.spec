# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk@cpan.org>

### EL6 ships with perl-Test-NoWarnings-0.084-5.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-NoWarnings

Summary: Perl module to make sure you didn't emit any warnings while testing
Name: perl-Test-NoWarnings
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-NoWarnings/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-NoWarnings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::Builder) >= 0.86
BuildRequires: perl(Test::Builder)
#BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::More)
#BuildRequires: perl(Test::Tester) >= 0.107
BuildRequires: perl(Test::Tester)
BuildRequires: perl >= 5.006
#Requires: perl(Test::Builder) >= 0.86
Requires: perl(Test::Builder)
#Requires: perl(Test::More) >= 0.47
Requires: perl(Test::More)
#Requires: perl(Test::Tester) >= 0.107
Requires: perl(Test::Tester)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Test-NoWarnings is a Perl module to make sure you didn't emit
any warnings while testing.

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
%doc %{_mandir}/man3/Test::NoWarnings.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/NoWarnings/
%{perl_vendorlib}/Test/NoWarnings.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.02-1
- Updated to version 1.02.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 1.00-1
- Updated to version 1.00.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.084-1
- Updated to release 0.084.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.083-1
- Initial package. (using DAR)
