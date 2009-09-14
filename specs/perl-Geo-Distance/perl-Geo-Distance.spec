# $Id$
# Authority: dries
# Upstream: Aran Clary Deltac <aran$arandeltac,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Distance

Summary: Calculate distances
Name: perl-Geo-Distance
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Distance/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Distance-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.3
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Math::Complex)

Requires: perl >= 5.8.3

%description
This perl library aims to provide as many tools to make it as simple as possible to calculate
distances between geographic points, and anything that can be derived from that.  Currently
there is support for finding the closest locations within a specified distance, to find the
closest number of points to a specified point, and to do basic point-to-point distance
calculations.

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
%{perl_vendorlib}/Geo/Distance.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
