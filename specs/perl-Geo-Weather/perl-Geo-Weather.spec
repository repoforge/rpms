# $Id$
# Authority: dries
# Upstream: Mike Machado <mike$metrobeam,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Weather

Summary: Weather retrieval module
Name: perl-Geo-Weather
Version: 1.41
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Weather/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Weather-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Geo::Weather module retrieves the current weather from weather.com
when given city and state or a US zip code. Geo::Weather relies on
LWP::UserAgent to work. In order for the timeout code to work correctly,
you must be using a recent version of libwww-perl and IO::Socket.

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
%doc HISTORY README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/Weather.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.41-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.41-1
- Initial package.
