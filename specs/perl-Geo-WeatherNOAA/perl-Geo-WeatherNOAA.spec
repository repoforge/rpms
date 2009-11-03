# $Id$
# Authority: dries
# Upstream: Mark Solomon <msolomon$seva,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-WeatherNOAA

Summary: Get official weather information from NOAA
Name: perl-Geo-WeatherNOAA
Version: 4.38
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-WeatherNOAA/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-WeatherNOAA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module enable one to easily get official weather information from
NOAA, their "Zone Reports" and hourly "state roundups."

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/WeatherNOAA.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 4.38-1
- Updated to release 4.38.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.37-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 4.37-1
- Initial package.
