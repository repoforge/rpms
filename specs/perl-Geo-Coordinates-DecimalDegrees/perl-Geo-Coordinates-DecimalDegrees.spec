# $Id$
# Authority: dries
# Upstream: Walt Mankowski <waltman$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Coordinates-DecimalDegrees

Summary: Convert between degrees/minutes/seconds and decimal degrees
Name: perl-Geo-Coordinates-DecimalDegrees
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Coordinates-DecimalDegrees/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Coordinates-DecimalDegrees-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Convert between degrees/minutes/seconds and decimal degrees.

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
%doc Changes INSTALL MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Geo::Coordinates::DecimalDegrees.3pm*
%dir %{perl_vendorlib}/Geo/
%dir %{perl_vendorlib}/Geo/Coordinates/
#%{perl_vendorlib}/Geo/Coordinates/DecimalDegrees/
%{perl_vendorlib}/Geo/Coordinates/DecimalDegrees.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
