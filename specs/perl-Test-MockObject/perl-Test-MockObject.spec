# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

### EL6 ships with perl-Test-MockObject-1.09-3.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-MockObject

Summary: Highly polymorphic testing object
Name: perl-Test-MockObject
Version: 1.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-MockObject/

Source: http://www.cpan.org/modules/by-module/Test/Test-MockObject-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test::MockObject is a highly polymorphic testing object, capable of looking
like all sorts of objects.  This makes white-box testing much easier, as you
can concentrate on what the code being tested sends to and receives from the
mocked object, instead of worrying about faking up your own data.  (Another
option is not to test difficult things.  Now you have no excuse.)


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::MockObject.3pm*
%doc %{_mandir}/man3/Test::MockObject::Extends.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/MockObject/
%{perl_vendorlib}/Test/MockObject.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
