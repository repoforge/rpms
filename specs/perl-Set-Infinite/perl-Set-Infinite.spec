# $Id$

# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$pucrs,br>

%define real_name Set-Infinite
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Sets of intervals
Name: perl-Set-Infinite
Version: 0.61
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Infinite/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/Set-Infinite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl

%description
This module contains functions for sets of intervals.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/Infinite.pm
%{perl_vendorlib}/Set/Infinite/*.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
