# $Id$
# Authority: dries
# Upstream: Adam J, Foxson <afoxson$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Reporter

Summary: Report test results of a package retrieved from CPAN
Name: perl-Test-Reporter
Version: 1.54
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Reporter/

Source: http://www.cpan.org/modules/by-module/Test/Test-Reporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test::Reporter reports the test results of any given distribution to the
CPAN testing service. See http://testers.cpan.org/ for details.
Test::Reporter has wide support for various perl5's and platforms.

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
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Test::Reporter*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Reporter/
%{perl_vendorlib}/Test/Reporter.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.54-1
- Updated to version 1.54.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.

