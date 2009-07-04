# $Id$
# Authority: dag
# Upstream: Luis Muñoz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetAddr-IP

Summary: Manages IPv4 and IPv6 addresses and subnets
Name: perl-NetAddr-IP
Version: 4.027
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetAddr-IP/

Source: http://www.cpan.org/modules/by-module/NetAddr/NetAddr-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Manages IPv4 and IPv6 addresses and subnets.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs 
find docs/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO docs/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/NetAddr/
%{perl_vendorarch}/NetAddr/IP.pm
%{perl_vendorarch}/NetAddr/IP/
%dir %{perl_vendorarch}/auto/NetAddr/
%{perl_vendorarch}/auto/NetAddr/IP/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 4.027-1
- Updated to version 4.027.

* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 4.007-1
- Updated to release 4.007.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 4.004-1
- Updated to release 4.004.
- Buildarch isn't noarch anymore (thanks to Peter Bieringer)

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.028-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 3.028-1
- Updated to release 3.028.

* Sat Mar 03 2004 Dag Wieers <dag@wieers.com> - 3.20-1
- Initial package. (using DAR)
