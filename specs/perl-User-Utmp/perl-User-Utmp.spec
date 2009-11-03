# $Id$
# Authority: dries
# Upstream: Michael Piotrowski <mxp$dynalabs,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name User-Utmp

Summary: Perl access to utmp- and utmpx-style databases
Name: perl-User-Utmp
Version: 1.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User-Utmp/

Source: http://www.cpan.org/modules/by-module/User/User-Utmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides a simple Perl interface to utmp- and utmpx-style
databases on UNIX systems, the most important being /etc/utmp, which
provides information about users currently logged in.  There is also
experimental support for writing utmp files.  For further details see
the POD documentation embedded in the file Utmp.pm, which will also be
installed as User::Utmp(3) manpage, and the example.pl script.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' *

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/User/
%{perl_vendorarch}/User/Utmp.pm
%{perl_vendorarch}/User/example.pl
%dir %{perl_vendorarch}/auto/User/
%{perl_vendorarch}/auto/User/Utmp/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
