# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-DES

Summary: Crypt-DES module for perl 
Name: perl-Crypt-DES
Version: 2.03
Release: 3
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-DES/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-DES-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Crypt-DES module for perl

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/DES.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/DES/

%changelog
* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 2.03-3
- Fixes to conform with new perl template. (C.Lee Taylor)

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.03-0
- Initial package. (using DAR)
