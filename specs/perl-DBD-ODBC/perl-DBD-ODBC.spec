# $Id$
# Authority: dag
# Upstream: Tim Bunce
# Upstream: Jeff Urlwin <jurlwin$bellatlantic,net>
# Upstream: Martin J, Evans <mjevans$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-ODBC

Summary: Perl DBD module for interfacing with ODBC databases
Name: perl-DBD-ODBC
Version: 1.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-ODBC/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-ODBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl >= 0:5.006
BuildRequires: perl(DBI) >= 1.21
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: unixODBC-devel > 2.2.5
Requires: perl >= 0:5.006
Requires: perl(DBI) >= 1.21
Requires: unixODBC > 2.2.5

%description
This module is needed to access ODBC databases from within Perl. The
module uses the unixODBC manager to connect to the database.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile.PL

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" -o %{_prefix} </dev/null
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes FAQ MANIFEST META.yml README README.RH9 README.adabas README.af README.hpux README.informix README.unicode examples/
%doc %{_mandir}/man3/DBD::ODBC.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/ODBC/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/ODBC/
%{perl_vendorarch}/DBD/ODBC.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sat Aug 18 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Added patch to build on x86_64. (Stefan Radman)

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
