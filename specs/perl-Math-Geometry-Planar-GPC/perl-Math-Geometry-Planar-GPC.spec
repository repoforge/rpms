# $Id$
# Authority: dag
# Upstream: Danny Van de Pol <daniel,van_de_pol$alcatel,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Geometry-Planar-GPC

Summary: Perl module that implements a wrapper for Alan Murta's gpc library
Name: perl-Math-Geometry-Planar-GPC
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Geometry-Planar-GPC/

Source: http://www.cpan.org/modules/by-module/Math/Math-Geometry-Planar-GPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Math-Geometry-Planar-GPC is a Perl module that implements a wrapper for
Alan Murta's gpc library.

This package contains the following Perl module:

    Math::Geometry::Planar::GPC

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Math::Geometry::Planar::GPC.3pm*
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/Geometry/
%dir %{perl_vendorarch}/Math/Geometry/Planar/
%{perl_vendorarch}/Math/Geometry/Planar/GPC.pm
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Geometry/
%dir %{perl_vendorarch}/auto/Math/Geometry/Planar/
%{perl_vendorarch}/auto/Math/Geometry/Planar/GPC/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
