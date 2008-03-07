# $Id$
# Authority: dag
# Upstream: Nigel Wetters Gourlay <nigel$wetters,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IP-Country

Summary: Fast lookup of country codes from IP addresses
Name: perl-IP-Country
Version: 2.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IP-Country/

Source: http://www.cpan.org/modules/by-module/IP/IP-Country-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(Geography::Countries)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Finding the home country of a client using only the IP address can be difficult.
Looking up the domain name associated with that address can provide some help,
but many IP address are not reverse mapped to any useful domain, and the
most common domain (.com) offers no help when looking for country.

This module comes bundled with a database of countries where various IP addresses
have been assigned. Although the country of assignment will probably be the
country associated with a large ISP rather than the client herself, this is
probably good enough for most log analysis applications, and under test has proved
to be as accurate as reverse-DNS and WHOIS lookup.

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
%doc CHANGES INSTALL MANIFEST META.yml README
%doc %{_mandir}/man1/ip2cc.1*
%doc %{_mandir}/man3/IP::Authority.3pm*
%doc %{_mandir}/man3/IP::Country.3pm*
%doc %{_mandir}/man3/IP::Country::*.3pm*
%{_bindir}/ip2cc
%dir %{perl_vendorlib}/IP/
%{perl_vendorlib}/IP/Authority/
%{perl_vendorlib}/IP/Authority.pm
%{perl_vendorlib}/IP/Country/
%{perl_vendorlib}/IP/Country.pm

%changelog
* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Wed Feb 07 2007 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 2.17-0
- Updated to release 2.17.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 2.14-0
- Updated to release 2.14.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 2.08-0
- Initial package. (using DAR)
