# $Id$

# Authority: dag

# Upstream: Nigel Wetters <nigel@wetters.net>
# Distcc: 0

%define rname IP-Country

Summary: Classes for fast lookup of country codes from IP addresses for Perl
Name: perl-IP-Country
Version: 2.17
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IP-Country/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 2.17-0
- Updated to release 2.17.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 2.14-0
- Updated to release 2.14.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 2.08-0
- Initial package. (using DAR)
