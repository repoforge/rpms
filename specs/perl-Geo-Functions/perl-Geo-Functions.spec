# $Id$
# Authority: dag
# Upstream: Michael R. Davis <michaelrdavis$perl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Functions

Summary: Perl module for standard Geo:: functions
Name: perl-Geo-Functions
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Functions/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Functions-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Geo-Functions is a Perl module for standard Geo:: functions.

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
%doc CHANGES LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Geo::Functions.3pm*
%dir %{perl_vendorlib}/Geo/
#%{perl_vendorlib}/Geo/Functions/
%{perl_vendorlib}/Geo/Functions.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
