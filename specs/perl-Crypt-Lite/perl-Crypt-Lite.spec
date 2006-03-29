# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-Lite

Summary: Easy to use symmetric data encryption and decryption
Name: perl-Crypt-Lite
Version: 0.82.06
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Lite/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Easy to use symmetric data encryption and decryption

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Lite.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Lite/

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.82.06-1
- Initial package. (using DAR)
