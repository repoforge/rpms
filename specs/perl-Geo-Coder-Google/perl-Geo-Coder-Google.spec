# $Id: $
# Authority: dries
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Coder-Google

Summary: Google Maps Geocoding API 
Name: perl-Geo-Coder-Google
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Coder-Google/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Coder-Google-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Geo::Coder::Google provides a geocoding functionality using Google Maps API.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Geo::Coder::Google.3pm*
%dir %{perl_vendorlib}/Geo/
%dir %{perl_vendorlib}/Geo/Coder/
#%{perl_vendorlib}/Geo/Coder/Google/
%{perl_vendorlib}/Geo/Coder/Google.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Thu Feb 28 2008 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
