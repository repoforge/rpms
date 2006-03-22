# $Id$
# Authority: dries
# Upstream: Mark Solomon <msolomon$seva,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-WeatherNOAA

Summary: Get official weather information from NOAA
Name: perl-Geo-WeatherNOAA
Version: 4.37
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-WeatherNOAA/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSOLOMON/Geo-WeatherNOAA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/WeatherNOAA.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.37-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 4.37-1
- Initial package.
