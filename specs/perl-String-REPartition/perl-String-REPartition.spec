# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-REPartition

Summary: Generating regular expressions used to partition data sets
Name: perl-String-REPartition
Version: 1.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-REPartition/

Source: http://www.cpan.org/authors/id/A/AV/AVIF/String-REPartition-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Dependencies)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
String::REPartition exports a function for generating regular expressions
used to partition data sets.

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
%doc %{_mandir}/man3/String::REPartition.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/REPartition/
%{perl_vendorlib}/String/REPartition.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
