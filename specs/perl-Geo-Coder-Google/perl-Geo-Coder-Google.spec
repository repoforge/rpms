# $Id: $
# Authority: dries
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Coder-Google

Summary: Google Maps Geocoding API 
Name: perl-Geo-Coder-Google
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Coder-Google/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Geo-Coder-Google-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::Syck) >= 0.1
BuildRequires: perl(LWP) >= 5.5
BuildRequires: perl(Test::More) >= 0.32
Requires: perl(Encode)
Requires: perl(JSON::Syck) >= 0.1
Requires: perl(LWP) >= 5.5
Requires: perl(Test::More) >= 0.32

%filter_from_requires /^perl*/d
%filter_setup


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
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Thu Feb 28 2008 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
