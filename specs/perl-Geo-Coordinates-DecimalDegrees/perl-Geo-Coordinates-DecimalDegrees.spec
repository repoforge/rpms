# $Id$
# Authority: dries
# Upstream: Walter Mankowski <waltman$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Coordinates-DecimalDegrees

Summary: Convert between degrees/minutes/seconds and decimal degrees
Name: perl-Geo-Coordinates-DecimalDegrees
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Coordinates-DecimalDegrees/

Source: http://search.cpan.org//CPAN/authors/id/W/WA/WALTMAN/Geo-Coordinates-DecimalDegrees-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Convert between degrees/minutes/seconds and decimal degrees.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Geo::Coordinates::DecimalDegrees*
%{perl_vendorlib}/Geo/Coordinates/DecimalDegrees.pm
%dir %{perl_vendorlib}/Geo/Coordinates/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
