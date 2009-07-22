# $Id$
# Authority: dries
# Upstream: Danny Van de Pol <daniel,van_de_pol$alcatel,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Geometry-Planar

Summary: Collection of planar geometry functions
Name: perl-Math-Geometry-Planar
Version: 1.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Geometry-Planar/

Source: http://www.cpan.org/modules/by-module/Math/Math-Geometry-Planar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides a set of 2D polygon, line and line segment operations.
The module also uses the GPC module for polygon clipping operations.

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
%{perl_vendorlib}/Math/Geometry/Planar.pm

%changelog
* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 1.17-1
- Updated to version 1.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.

