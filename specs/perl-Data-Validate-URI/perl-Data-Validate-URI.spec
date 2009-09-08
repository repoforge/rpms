# $Id$
# Authority: shuff
# Upstream: Richard Sonnen <sonnen$richardsonnen,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Validate-URI

Summary: Common URL validation methods
Name: perl-Data-Validate-URI
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Validate-URI/

Source: http://www.cpan.org/modules/by-module/Data/Data-Validate-URI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Validate::Domain)
BuildRequires: perl(Data::Validate::IP)
Requires: perl
Requires: perl(Data::Validate::Domain)
Requires: perl(Data::Validate::IP)

%description
This module collects common URI validation routines to make input
validation, and untainting easier and more readable.

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
%doc Changes MANIFEST META.yml README INSTALL
%doc %{_mandir}/man3/Data::Validate::URI.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Validate/
%dir %{perl_vendorlib}/auto/Data/
%dir %{perl_vendorlib}/auto/Data/Validate/
%dir %{perl_vendorlib}/auto/Data/Validate/URI/
%{perl_vendorlib}/Data/Validate/URI.pm
%{perl_vendorlib}/auto/Data/Validate/URI/*

%changelog
* Wed Aug 26 2009 Steve Huff <shuff@vecna.org> - 0.05-1
- Initial package. (using DAR)
