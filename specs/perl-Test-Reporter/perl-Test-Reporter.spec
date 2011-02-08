# $Id$
# Authority: dries
# Upstream: David Golden <dagolden@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Reporter

Summary: Report test results of a package retrieved from CPAN
Name: perl-Test-Reporter
Version: 1.57
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Reporter/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Test-Reporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FileHandle)
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Sys::Hostname)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More) 
BuildRequires: perl(Time::Local)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl >= 5.006
Requires: perl(Carp)
Requires: perl(Cwd)
Requires: perl(Data::Dumper)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(FileHandle)
Requires: perl(Net::SMTP)
Requires: perl(Sys::Hostname)
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More) 
Requires: perl(Time::Local)
Requires: perl(base)
Requires: perl(constant)
Requires: perl >= 5.006

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Test::Reporter reports the test results of any given distribution to the
CPAN testing service. See http://testers.cpan.org/ for details.
Test::Reporter has wide support for various perl5's and platforms.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man1/cpantest.1*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Reporter/
%{perl_vendorlib}/Test/Reporter.pm
%{_bindir}/cpantest

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.57-1
- Updated to version 1.57.

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

