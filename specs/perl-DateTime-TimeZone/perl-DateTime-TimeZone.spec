# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-TimeZone

Summary: Time zone object base class and factory
Name: perl-DateTime-TimeZone
Version: 0.46
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-TimeZone/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-TimeZone-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/DateTime/TimeZone.pm
%{perl_vendorlib}/DateTime/TimeZone.pm
%{perl_vendorlib}/DateTime/TimeZone/
%{perl_vendorlib}/DateTime/TimeZoneCatalog.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
