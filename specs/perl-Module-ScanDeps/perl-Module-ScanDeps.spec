# $Id$
# Authority: dries
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-ScanDeps

Summary: Recursively scan Perl code for dependencies
Name: perl-Module-ScanDeps
Version: 0.82
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-ScanDeps/

Source: http://www.cpan.org/modules/by-module/Module/Module-ScanDeps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Module::ScanDeps, a module to recursively
scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects,
PAR and App::Packer.  Please see their respective documentations on CPAN
for further information.

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
%doc AUTHORS Changes MANIFEST META.yml README
%doc %{_mandir}/man1/scandeps.pl.1*
%doc %{_mandir}/man3/Module::ScanDeps.3pm*
%doc %{_mandir}/man3/Module::ScanDeps::DataFeed.3pm*
%{_bindir}/scandeps.pl
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/ScanDeps/
%{perl_vendorlib}/Module/ScanDeps.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.78-1
- Updated to release 0.78.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.77-1
- Updated to release 0.77.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Updated to release 0.74.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.70-1
- Updated to release 0.70.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.69-1
- Updated to release 0.69.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.66-1
- Updated to release 0.66.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.60-1
- Updated to release 0.60.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Updated to release 0.57.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
