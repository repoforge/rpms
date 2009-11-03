# $Id$
# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Locations

Summary: Magic insertion points in your data
Name: perl-Data-Locations
Version: 5.4
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Locations/

Source: http://www.cpan.org/modules/by-module/Data/Data-Locations-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Magic insertion points in your data.

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
%doc README.txt
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/Locations.pm
%dir %{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/auto/Data/Locations/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 5.4-1
- Initial package.
