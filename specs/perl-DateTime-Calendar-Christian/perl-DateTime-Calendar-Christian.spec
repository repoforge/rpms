# $Id$

# Authority: dries
# Upstream: Eugene van der Pijll <pijll$gmx,net>

%define real_name DateTime-Calendar-Christian
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Dates in the Christian calendar
Name: perl-DateTime-Calendar-Christian
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-Christian/

Source: http://search.cpan.org/CPAN/authors/id/P/PI/PIJLL/DateTime-Calendar-Christian-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements the Christian calendar, which consists of both
the Julian and the Gregorian calendars.

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
%{perl_vendorlib}/DateTime/Calendar/Christian.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
