# $Id$
# Authority: dries
# Upstream: Danny Van de Pol <daniel,van_de_pol$alcatel,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Geometry-GPC

Summary: Perl wrapper for Alan Murta's gpc library
Name: perl-Math-Geometry-GPC
Version: 1.03
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Geometry-GPC/

Source: http://www.cpan.org/modules/by-module/Math/Math-Geometry-GPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a autoloadable interface module for gpc, a popular library
for polygon clipping operations.  With this library you can perform
DIFFERENCE, INTERSECTION, XOR and UNION operations on polygons.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/Geometry/
%{perl_vendorarch}/Math/Geometry/GPC.pm
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Geometry/
%{perl_vendorarch}/auto/Math/Geometry/GPC/

%changelog
* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
