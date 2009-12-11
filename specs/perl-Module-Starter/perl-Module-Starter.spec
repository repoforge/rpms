# $Id$
# Authority: dries
# Upstream: Andy Lester <andy$petdance,com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Starter

Summary: Simple starterkit for any module
Name: perl-Module-Starter
Version: 1.54
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Starter/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Module-Starter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::Command)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage) >= 1.21
BuildRequires: perl(Test::Harness) >= 0.21
BuildRequires: perl(Test::More)
Requires: perl(ExtUtils::Command)
Requires: perl(File::Spec)
Requires: perl(Getopt::Long)
Requires: perl(Pod::Usage) >= 1.21
Requires: perl(Test::Harness) >= 0.21
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
A simple starterkit for any module.

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
%doc %{_mandir}/man1/module-starter.1*
%doc %{_mandir}/man3/Module::Starter.3pm*
%doc %{_mandir}/man3/Module::Starter::*.3pm*
%{_bindir}/module-starter
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Starter/
%{perl_vendorlib}/Module/Starter.pm

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 1.54-1
- Updated to version 1.54.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 1.52-1
- Updated to version 1.52.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.50-1
- Updated to version 1.50.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.470-1
- Updated to release 1.470.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.42-1
- Updated to release 1.42.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Updated to release 1.40.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.38-1
- Updated to release 1.38.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.34-1
- Updated to release 1.34.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
