# $Id$
# Authority: dag
# Upstream: Nigel Wetters Gourlay <nigel$wetters,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IP-Country

Summary: Classes for fast lookup of country codes from IP addresses for Perl
Name: perl-IP-Country
Version: 2.18
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IP-Country/

Source: http://search.cpan.org/CPAN/authors/id/N/NW/NWETTERS/IP-Country-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Geography::Countries)
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
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/ip2cc
%{_libdir}/perl5/vendor_perl/*/IP/

%changelog
* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 2.17-0
- Updated to release 2.17.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 2.14-0
- Updated to release 2.14.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 2.08-0
- Initial package. (using DAR)
