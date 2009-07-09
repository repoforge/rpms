# $Id$
# Authority: dries
# Upstream: Alexander Jung <alexander,w,jung$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-X509

Summary: Object oriented X.509 certificate parser
Name: perl-Crypt-X509
Version: 0.40
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-X509/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-X509-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Crypt::X509 is an object oriented X.509 certificate parser with numerous
methods for directly extracting information from certificates.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man3/Crypt::X509.3pm*
%dir %{perl_vendorlib}/Crypt/
#%{perl_vendorlib}/Crypt/X509/
%{perl_vendorlib}/Crypt/X509.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.

