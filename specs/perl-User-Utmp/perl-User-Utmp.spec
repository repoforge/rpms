# $Id$
# Authority: dries
# Upstream: Michael Piotrowski <mxp$dynalabs,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name User-Utmp

Summary: Perl access to utmp- and utmpx-style databases
Name: perl-User-Utmp
Version: 1.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/User-Utmp/

Source: http://search.cpan.org/CPAN/authors/id/M/MP/MPIOTR/User-Utmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/User/Utmp.pm
%{perl_vendorarch}/User/example.pl
%{perl_vendorarch}/auto/User/Utmp

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
