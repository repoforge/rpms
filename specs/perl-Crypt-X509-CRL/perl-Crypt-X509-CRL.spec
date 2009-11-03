# $Id$
# Authority: dries
# Upstream: Duncan Segrest <cpan$GigaGeek,info>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-X509-CRL

Summary: Parses an X.509 certificate revocation list
Name: perl-Crypt-X509-CRL
Version: 0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-X509-CRL/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-X509-CRL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 4:5.8.8

%description
Parses an X.509 certificate revocation list.

%prep
%setup -n %{real_name}

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
%doc Changes README
%doc %{_mandir}/man3/Crypt::X509::CRL*
%{perl_vendorlib}/Crypt/X509/CRL.pm
%dir %{perl_vendorlib}/Crypt/X509/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
