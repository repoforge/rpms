# $Id$
# Authority: dries
# Upstream: Danny Van de Pol <daniel,van_de_pol$alcatel,be>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Geometry-GPC

Summary: Perl wrapper for Alan Murta's gpc library
Name: perl-Math-Geometry-GPC
Version: 1.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Geometry-GPC/

Source: http://search.cpan.org/CPAN/authors/id/D/DV/DVDPOL/Math-Geometry-GPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is a autoloadable interface module for gpc, a popular library
for polygon clipping operations.  With this library you can perform
DIFFERENCE, INTERSECTION, XOR and UNION operations on polygons.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Math/Geometry/GPC.pm
%{perl_vendorarch}/auto/Math/Geometry/GPC

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
