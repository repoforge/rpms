# $Id$
# Authority: cmr
# Upstream: Xavier Guimard <x,guimard$free,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Portal

Summary: The authentication portal part of Lemonldap::NG Web-SSO
Name: perl-Lemonldap-NG-Portal
Version: 0.88
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Portal/

Source: http://www.cpan.org/modules/by-module/Lemonldap/Lemonldap-NG-Portal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The authentication portal part of Lemonldap::NG Web-SSO.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/Lemonldap::NG::Portal.3pm*
%doc %{_mandir}/man3/Lemonldap::NG::Portal*.3pm*
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/NG/
%dir %{perl_vendorlib}/auto/Lemonldap/NG/Portal/_i18n/autosplit.ix
%dir %{perl_vendorlib}/auto/Lemonldap/NG/Portal/_i18n/error_en.al
%dir %{perl_vendorlib}/auto/Lemonldap/NG/Portal/_i18n/error_fr.al
%dir %{perl_vendorlib}/auto/Lemonldap/NG/Portal/_i18n/error_ro.al
%{perl_vendorlib}/Lemonldap/NG/Portal/
%{perl_vendorlib}/Lemonldap/NG/Portal.pm

%changelog
* Sat Jul 04 2009 Unknown - 0.88-1
- Initial package. (using DAR)
