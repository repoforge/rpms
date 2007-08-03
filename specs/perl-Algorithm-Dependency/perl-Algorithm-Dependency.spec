# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Dependency

Summary: Perl module for implementing various dependency trees 
Name: perl-Algorithm-Dependency
Version: 1.102
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Dependency/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Dependency-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Test::More) >= 0.47, perl(File::Spec) >= 0.80
BuildRequires: perl(Test::ClassAPI) >= 0.6, perl(Params::Util) >= 0.06
BuildRequires: perl(List::Util) >= 1.11
Requires: perl

%description
Algorithm-Dependency is a perl module for implementing various
dependency trees.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Algorithm/
%{perl_vendorlib}/Algorithm/Dependency/
%{perl_vendorlib}/Algorithm/Dependency.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.102-1
- Initial package. (using DAR)
