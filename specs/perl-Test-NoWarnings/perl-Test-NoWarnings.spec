# $Id$
# Authority: dag
# Upstream: Fergal Daly <fergal$esatclear,ie>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-NoWarnings

Summary: Perl module to make sure you didn't emit any warnings while testing
Name: perl-Test-NoWarnings
Version: 0.084
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-NoWarnings/

Source: http://www.cpan.org/modules/by-module/Test/Test-NoWarnings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Test-NoWarnings is a Perl module to make sure you didn't emit
any warnings while testing.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Test::NoWarnings.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/NoWarnings/
%{perl_vendorlib}/Test/NoWarnings.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.084-1
- Updated to release 0.084.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.083-1
- Initial package. (using DAR)
