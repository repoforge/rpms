# $Id$
# Authority: dries
# Upstream: Rafaël Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-CoreList

Summary: Get the list of modules shipped with versions of perl
Name: perl-Module-CoreList
Version: 2.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-CoreList/

Source: http://www.cpan.org/modules/by-module/Module/Module-CoreList-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
This module gets the list of modules shipped with versions of perl.

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
%doc %{_mandir}/man1/corelist.1*
%doc %{_mandir}/man3/Module::CoreList.3pm*
%{_bindir}/corelist
%dir %{perl_vendorlib}/Module/
#%{perl_vendorlib}/Module/CoreList/
%{perl_vendorlib}/Module/CoreList.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 2.12-1
- Updated to release 2.12.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Wed Jan 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.98-1
- Updated to release 1.98.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.97-1
- Updated to release 1.97.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.95-1
- Initial package.
