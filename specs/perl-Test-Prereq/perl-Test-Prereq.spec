# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Prereq

Summary: Check if Makefile.PL has the right pre-requisites
Name: perl-Test-Prereq
Version: 1.037
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Prereq/

Source: http://www.cpan.org/modules/by-module/Test/Test-Prereq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Check if Makefile.PL has the right pre-requisites.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test/Prereq.pm
%{perl_vendorlib}/Test/Prereq

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.037-1
- Updated to version 1.037.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.033-1
- Updated to release 1.033.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.031-1
- Updated to release 1.031.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.030-1
- Updated to release 1.030.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.029-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.029-1
- Updated to release 1.029.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.028-1
- Updated to release 1.028.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.027-1
- Initial package.
