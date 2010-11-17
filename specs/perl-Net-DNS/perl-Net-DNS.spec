# $Id$
# Authority: dag
# Upstream: Olaf Kolkman <olaf$net-dns,org>

### EL6 ships with perl-Net-DNS-0.65-2.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-Net-DNS-0.59-3.el5
%{?el5:# Tag: rfx}
### EL4 ships with perl-Net-DNS-0.48-2.el4
%{?el4:# Tag: rfx}
### EL3 ships with perl-Net-DNS-0.31-4.el3
%{?el3:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS

Summary: Perl DNS resolver module
Name: perl-Net-DNS
Version: 0.66
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS/

Source: http://www.cpan.org/authors/id/O/OL/OLAF/Net-DNS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Net::DNS is a DNS resolver implemented in Perl.  It allows the
programmer to perform nearly any type of DNS query from a Perl
script.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    --no-online-tests
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO contrib/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/DNS/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/DNS/
%{perl_vendorarch}/Net/DNS.pm

### Remove this file because it generates an rpm dependency for Win32::Registry
%exclude %{perl_vendorarch}/Net/DNS/Resolver/Win32.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.66-1
- Updated to version 0.66.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.65-1
- Updated to version 0.65.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Updated to release 0.57.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Updated to release 0.48.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.38-0
- Updated to release 0.38.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.33-0
- Initial package. (using DAR)
