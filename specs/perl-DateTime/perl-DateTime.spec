# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

### EL6 ships with perl-DateTime-1:0.5300-1.el6
%{?el6:# Tag: rfx}
%{?el6:%define _with_epoch 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime
%define real_version 0.70

Summary: Date and time objects
Name: perl-DateTime
Version: %{real_version}00
%{?_with_epoch:Epoch: 1}
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{real_version}-%{release}-root

BuildRequires: perl >= 5.8.1
BuildRequires: perl(DateTime::Locale) >= 0.41
BuildRequires: perl(DateTime::TimeZone) >= 1.09
BuildRequires: perl(Math::Round)
BuildRequires: perl(Module::Build) >= 0.3601
BuildRequires: perl(Params::Validate) >= 0.76
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Time::Local) >= 1.04
Requires: perl(DateTime::Locale) >= 0.41
Requires: perl(DateTime::TimeZone) >= 1.09
Requires: perl(Math::Round)
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
%setup -n %{real_name}-%{real_version}

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
%doc CREDITS Changes LICENSE MANIFEST META.json META.yml README 
%doc SIGNATURE TODO leaptab.txt
%doc %{_mandir}/man?/*
%{perl_vendorarch}/DateTime.pm
%{perl_vendorarch}/DateTimePP.pm
%{perl_vendorarch}/DateTimePPExtra.pm
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/auto/DateTime/

%changelog
* Mon Jun 13 2011 Steve Huff <shuff@vecna.org> - 1:0.7000-1
- Updated to version 0.70.
- Added Epoch in el6 because RH did.

* Wed Mar 23 2011 Yury V. Zaytsev <yury@shurup.com> - 0.5300-2
- Version bump to supersede 0.4305 (thanks to Matthew Vale!)

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
