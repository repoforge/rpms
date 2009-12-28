# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime

Summary: Date and time objects
Name: perl-DateTime
Version: 0.53
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(DateTime::Locale) >= 0.41
BuildRequires: perl(DateTime::TimeZone) >= 0.59
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Validate) >= 0.76
BuildRequires: perl(Pod::Man) >= 1.14
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.34
BuildRequires: perl(Time::Local) >= 1.04
Requires: perl(DateTime::Locale) >= 0.41
Requires: perl(DateTime::TimeZone) >= 0.59
Requires: perl(Params::Validate) >= 0.76
Requires: perl(Scalar::Util)
Requires: perl(Time::Local) >= 1.04

%filter_from_requires /^perl*/d
%filter_setup

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
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS Changes LICENSE MANIFEST META.yml README SIGNATURE TODO leaptab.txt
%doc %{_mandir}/man3/DateTime.3pm*
%doc %{_mandir}/man3/DateTime::*.3pm*
%{perl_vendorarch}/DateTime.pm
%{perl_vendorarch}/DateTimePP.pm
%{perl_vendorarch}/DateTimePPExtra.pm
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/auto/DateTime/

%changelog
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 0.53-1
- Updated to version 0.53.

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
