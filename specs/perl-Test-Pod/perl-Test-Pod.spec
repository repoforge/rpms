# $Id$
# Authority: dries
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Pod

Summary: Checks for POD errors in files
Name: perl-Test-Pod
Version: 1.26
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Pod/

Source: http://www.cpan.org/modules/by-module/Test/Test-Pod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to check for POD errors in files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Pod.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
