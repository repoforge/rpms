# $Id$
# Authority: dries
# Upstream: David E. Wheeler <david@justatheory.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Pod

Summary: Checks for POD errors in files
Name: perl-Test-Pod
Version: 1.42
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Pod/

Source: http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Test-Pod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Pod::Simple) >= 3.07
BuildRequires: perl(Test::Builder::Tester) >= 1.02
BuildRequires: perl(Test::More)
Requires: perl(File::Spec)
Requires: perl(Pod::Simple) >= 3.07
Requires: perl(Test::Builder::Tester) >= 1.02
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module allows you to check for POD errors in files.

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Pod.pm

%changelog
* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 1.42-1
- Updated to version 1.42.

* Fri Jan 15 2010 Christoph Maser <cmr@financial.com> - 1.41-1
- Updated to version 1.41.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
