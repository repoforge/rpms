# $Id$
# Authority: dries
# Upstream: Boris Zentner <bzm$2bz,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IP-PurePerl

Summary: Look up country by IP Address
Name: perl-Geo-IP-PurePerl
Version: 1.23
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IP-PurePerl/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-IP-PurePerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Look up country by IP Address.

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
%doc COPYING Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man1/geoip-lookup.1*
%doc %{_mandir}/man3/Geo::IP::PurePerl.3pm*
%{_bindir}/geoip-lookup
%dir %{perl_vendorlib}/Geo/
%dir %{perl_vendorlib}/Geo/IP/
#%{perl_vendorlib}/Geo/IP/PurePerl/
%{perl_vendorlib}/Geo/IP/PurePerl.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
