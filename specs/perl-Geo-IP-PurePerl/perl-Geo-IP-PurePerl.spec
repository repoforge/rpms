# $Id$
# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IP-PurePerl

Summary: Look up country by IP Address
Name: perl-Geo-IP-PurePerl
Version: 1.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IP-PurePerl/

Source: http://search.cpan.org//CPAN/authors/id/T/TJ/TJMATHER/Geo-IP-PurePerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Look up country by IP Address.

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
%doc %{_mandir}/man3/Geo::IP::PurePerl*
%doc %{_mandir}/man1/geoip-lookup*
%{perl_vendorlib}/Geo/IP/PurePerl.pm
%dir %{perl_vendorlib}/Geo/IP/
%{_bindir}/geoip-lookup

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
