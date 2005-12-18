# $Id$
# Authority: dries
# Upstream: Schuyler Erle <schuyler$nocat,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Dymaxion

Summary: Plot latitude/longitude on a Fuller Dymaxion(tm) map
Name: perl-Geo-Dymaxion
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Dymaxion/

Source: http://search.cpan.org/CPAN/authors/id/S/SD/SDERLE/Geo-Dymaxion-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Inline

%description
"Geo::Dymaxion" allows you to draw points on Dymaxion(tm) maps using
latitude and longitude data, which turns out to be quite difficult and
requires some tricky trigonometry. This module strives to hide away all
the ugly math and allow you to concentrate on drawing your map.

The Dymaxion(tm), or Fuller, projection was invented by R. Buckminster
Fuller in 1954, and is "the only flat map of the entire surface of the
Earth which reveals our planet as one island in one ocean, without any
visually obvious distortion of the relative shapes and sizes of the land
areas, and without splitting any continents." See
http://www.bfi.org/map.htm for more details.

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
%{perl_vendorarch}/Geo/Dymaxion.pm
%{perl_vendorarch}/auto/Geo/Dymaxion/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
