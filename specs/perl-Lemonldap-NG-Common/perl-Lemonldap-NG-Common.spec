# $Id$
# Authority: cmr
# Upstream: guimard <guimard$>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lemonldap-NG-Common

Summary: Common files for Lemonldap::NG infrastructure
Name: perl-Lemonldap-NG-Common
Version: 0.94
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lemonldap-NG-Common/

Source: http://www.cpan.org/modules/by-module/Lemonldap/Lemonldap-NG-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Cache::Cache) 
BuildRequires: perl(CGI) >= 3.08                   
BuildRequires: perl(Crypt::Rijndael) 
BuildRequires: perl(DBI) 
BuildRequires: perl(IO::String) 
BuildRequires: perl(Regexp::Assemble) 
BuildRequires: perl(SOAP::Lite) 
BuildRequires: perl(Storable) 


%description
Common files for Lemonldap::NG infrastructure.

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
%doc %{_mandir}/man3/Lemonldap::NG::Common*.3pm*
%dir %{perl_vendorlib}/Lemonldap/
%dir %{perl_vendorlib}/Lemonldap/NG/
%{perl_vendorlib}/Lemonldap/NG/Common/
%{perl_vendorlib}/Lemonldap/NG/Common.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.94-1
- Updated to version 0.94.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.92-1
- Initial package. (using DAR)
