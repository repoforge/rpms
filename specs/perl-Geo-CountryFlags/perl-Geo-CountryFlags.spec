# $Id$
# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-CountryFlags

Summary: Fetch images of country flags
Name: perl-Geo-CountryFlags
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-CountryFlags/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-CountryFlags-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker), perl(File::SafeDO), perl(LWP::Simple)

%description
This package contains methods for fetching images of country flags.

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
%doc Changes MANIFEST MANIFEST.SKIP MANIFEST.in META.yml
%doc %{_mandir}/man3/Geo::CountryFlags.3pm*
%doc %{_mandir}/man3/Geo::CountryFlags::*.3pm*
%dir %{perl_vendorlib}/Geo/
%{perl_vendorlib}/Geo/CountryFlags/
%{perl_vendorlib}/Geo/CountryFlags.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
