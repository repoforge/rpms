# $Id$

# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define real_name DateTime-TimeZone
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Time zone object base class and factory 
Name: perl-DateTime-TimeZone
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-TimeZone/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl-Module-Build, perl
Provides: perl(DateTime::TimeZoneCatalog)

%description
The DateTime::TimeZone modules provide a Perl interface to the Olson
time zone database.  Rather than using the database directly, we parse
the database files and turn them into a set of modules, one for each
time zone defined.  This allows for various optimizations in doing
time zone calculations.  This conversion is done with the script in
tools/parse_olson.

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
%{perl_vendorlib}/DateTime/TimeZone.pm
%{perl_vendorlib}/DateTime/TimeZone
%{perl_vendorlib}/DateTime/TimeZoneCatalog.pm

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
