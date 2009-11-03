# $Id$
# Authority: dag
# Upstream: Fergal Daly <fergal$esatclear,ie>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Deep

Summary: Perl module implements an extremely flexible deep comparison
Name: perl-Test-Deep
Version: 0.106
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Deep/

Source: http://www.cpan.org/modules/by-module/Test/Test-Deep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::Util) >= 1.09
BuildRequires: perl(Scalar::Util) >= 1.09
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings) >= 0.02
BuildRequires: perl(Test::Tester) >= 0.04


%description
perl-Test-Deep is a Perl module implements an extremely flexible deep comparison.

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
%doc CHANGES MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Test::Deep.3pm*
%doc %{_mandir}/man3/Test::Deep::NoTest.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Deep/
%{perl_vendorlib}/Test/Deep.pm
%{perl_vendorlib}/Test/Deep.pod

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.106-1
- Updated to version 0.106.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.104-1
- Updated to version 0.104.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.100-1
- Updated to release 0.100.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.099-1
- Updated to release 0.099.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.096-1
- Initial package. (using DAR)
