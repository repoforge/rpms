# $Id$
# Authority: dries
# Upstream: Gene Boggs <gene$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Counting

Summary: Combinatorial counting operations
Name: perl-Math-Counting
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Counting/

Source: http://search.cpan.org/CPAN/authors/id/G/GE/GENE/Math-Counting-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains functions for combinatorial counting operations.

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
%doc CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Counting.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
