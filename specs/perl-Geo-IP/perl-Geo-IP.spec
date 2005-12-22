# $Id$
# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IP

Summary: Database which maps IP blocks on countries
Name: perl-Geo-IP
Version: 1.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IP/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/Geo-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module a simple file-based database.  This database simply contains
IP blocks as keys, and countries as values.  The data contains all
public IP addresses and should be more
complete and accurate than reverse DNS lookups.

%prep
%setup -n %{real_name}-%{version}

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
%{perl_vendorarch}/Geo/IP.pm
%{perl_vendorarch}/Geo/IP/
%{perl_vendorarch}/Geo/Mirror.pm
%{perl_vendorarch}/auto/Geo/IP/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Initial package.
