# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

### EL6 includes perl-DateTime-TimeZone in perl-DateTime-1:0.5300-1.el6
# ExclusiveDist: el2 el3 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-TimeZone

Summary: Time zone object base class and factory
Name: perl-DateTime-TimeZone
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-TimeZone/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Singleton) >= 1.03
BuildRequires: perl(Cwd) >= 3
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Validate) >= 0.72
BuildRequires: perl(Pod::Man) >= 1.14
Requires: perl(Class::Singleton) >= 1.03
Requires: perl(Cwd) >= 3
Requires: perl(Params::Validate) >= 0.72
Requires: perl(Pod::Man) >= 1.14

%filter_from_requires /^perl*/d
%filter_setup


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
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build
./Build test

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST MANIFEST.base META.yml README SIGNATURE
%doc %{_mandir}/man3/DateTime::TimeZone.3pm*
%doc %{_mandir}/man3/DateTime::TimeZone::*.3pm*
%dir %{perl_vendorlib}/DateTime/
%{perl_vendorlib}/DateTime/TimeZone/
%{perl_vendorlib}/DateTime/TimeZone.pm

### Exclude to disable Win32 dependencies
%exclude %{_mandir}/man3/DateTime::TimeZone::Local::Win32.3pm*
%exclude %{perl_vendorlib}/DateTime/TimeZone/Local/Win32.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.10-1
- Updated to version 1.10.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.98-1
- Updated to version 0.98.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.93-1
- Updated to version 0.93.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 0.91-1
- Updated to version 0.91.

* Sat Nov 29 2008 Dag Wieers <dag@wieers.com> - 0.8301-1
- Updated to release 0.8301.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.7701-1
- Updated to release 0.7701.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.6904-1
- Switch to upstream version.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.69.4-2
- Excluded Win32 dependencies by excluding module. (Ralph Angenendt)

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.69.4-1
- Updated to release 0.6904.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.69.2-1
- Updated to release 0.6902.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

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
