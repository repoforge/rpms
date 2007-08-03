# $Id$

# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetAddr-IP

Summary: Manages IPv4 and IPv6 addresses and subnets
Name: perl-NetAddr-IP
Version: 4.004
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetAddr-IP/

Source: http://www.cpan.org/modules/by-module/NetAddr/NetAddr-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Manages IPv4 and IPv6 addresses and subnets.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod \
		%{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README TODO
%doc %{_mandir}/man?/NetAddr::IP*
%dir %{perl_vendorarch}/NetAddr/
%{perl_vendorarch}/NetAddr/IP.pm
%{perl_vendorarch}/NetAddr/IP/
%{perl_vendorarch}/auto/NetAddr/

%changelog
* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 4.004-1
- Updated to release 4.004.
- Buildarch isn't noarch anymore (thanks to Peter Bieringer)

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.028-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 3.028-1
- Updated to release 3.028.

* Sat Mar 03 2004 Dag Wieers <dag@wieers.com> - 3.20-1
- Initial package. (using DAR)
