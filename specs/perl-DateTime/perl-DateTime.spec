# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime

Summary: Date and time objects
Name: perl-DateTime
Version: 0.50
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Provides: perl(DateTimePPExtra)

%description
The DateTime.pm module aims to provide a complete, correct, and easy
to use date/time object implementation. Currently it handles many date
calculations, date math (addition and subtraction), and provides
convenient methods for retrieving portions of a date/time.

This module properly supports the Olson time zone database, meaning
that historical time zone information, and more importantly, daylight
saving time rules, can be handled transparently, simply by setting the
correct time zone. This is done by using the DateTime::TimeZone
module.

%prep
%setup -n %{real_name}-%{version}

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
%doc CREDITS Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO leaptab.txt
%doc %{_mandir}/man3/DateTime.3pm*
%doc %{_mandir}/man3/DateTime::*.3pm*
%{perl_vendorarch}/DateTime.pm
%{perl_vendorarch}/DateTimePP.pm
%{perl_vendorarch}/DateTimePPExtra.pm
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/auto/DateTime/

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.50-1
- Updated to version 0.50.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.4305-1
- Updated to release 0.4305.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.4302-1
- Updated to release 0.4302.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.41-1
- Updated to release 0.41.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.2901-1
- Updated to release 0.2901.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.29-1
- Updated to release 0.29.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
