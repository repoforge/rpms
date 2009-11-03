# $Id$
# Authority: dag
# Upstream: Michael R. Davis

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Constants

Summary: Perl module with standard Geo:: constants
Name: perl-Geo-Constants
Version: 0.06
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Constants/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Constants-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Geo-Constants is a Perl module with standard Geo:: constants.

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
%doc %{_mandir}/man3/Geo::Constants.3pm*
%dir %{perl_vendorlib}/Geo/
%{perl_vendorlib}/Geo/Constants.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
