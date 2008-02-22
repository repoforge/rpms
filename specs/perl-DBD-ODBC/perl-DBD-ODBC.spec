# $Id$
# Authority: dag
# Upstream: Jeff Urlwin <jurlwin$bellatlantic,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-ODBC

Summary: Perl DBD module for interfacing with ODBC databases
Name: perl-DBD-ODBC
Version: 1.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-ODBC/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-ODBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(DBI) >= 1.21
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: unixODBC-devel > 2.2.5
Requires: perl(DBI) >= 1.21, unixODBC > 2.2.5

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README README.RH9 README.adabas README.af README.hpux README.informix README.unicode
%doc %{_mandir}/man3/DBD::ODBC.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/ODBC.pm
%{perl_vendorarch}/DBD/ODBC/
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/ODBC/

%changelog
* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sat Aug 18 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Added patch to build on x86_64. (Stefan Radman)

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
