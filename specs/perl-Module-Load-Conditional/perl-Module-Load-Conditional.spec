# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

### EL6 ships with perl-Module-Load-Conditional-0.30-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Load-Conditional

Summary: Looking up module information / loading at runtime
Name: perl-Module-Load-Conditional
Version: 0.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Load-Conditional/

Source: http://www.cpan.org/modules/by-module/Module/Module-Load-Conditional-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(Module::CoreList) >= 2.22
BuildRequires: perl(Module::Load) >= 0.11
BuildRequires: perl(Params::Check)
BuildRequires: perl(Test::More)
BuildRequires: perl(version) >= 0.69
Requires: perl(Locale::Maketext::Simple)
Requires: perl(Module::CoreList) >= 2.22
Requires: perl(Module::Load) >= 0.11
Requires: perl(Params::Check)
Requires: perl(Test::More)
Requires: perl(version) >= 0.69

%filter_from_requires /^perl*/d
%filter_setup

%description
Allows you to query the state of modules on your system. It can
tell you if you have certain modules installed without attempting
to C<use> them and can do smart loading of modules.
Also it can tell you what *other* modules a certain module
requires.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Module::Load::Conditional.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Load/
%{perl_vendorlib}/Module/Load/Conditional.pm

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.34-1
- Updated to version 0.34.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.30-1
- Updated to version 0.30.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
