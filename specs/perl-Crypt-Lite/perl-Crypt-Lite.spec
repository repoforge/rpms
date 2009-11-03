# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-Lite

Summary: Easy to use symmetric data encryption and decryption
Name: perl-Crypt-Lite
Version: 0.82.11
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Lite/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Easy to use symmetric data encryption and decryption

%prep
%setup -n %{rname}-%{version}

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
%doc MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/Lite.pm
#%dir %{perl_vendorarch}/auto/Crypt/
#%{perl_vendorarch}/auto/Crypt/Lite/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.82.11-1
Updated to release 0.82.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.82.06-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.82.06-1
- Initial package. (using DAR)
