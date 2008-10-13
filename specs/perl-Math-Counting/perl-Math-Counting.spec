# $Id$
# Authority: dries
# Upstream: Gene Boggs <gene$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Counting

Summary: Combinatorial counting operations
Name: perl-Math-Counting
Version: 0.0801
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Counting/

Source: http://www.cpan.org/modules/by-module/Math/Math-Counting-%{version}.tar.gz
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
find %{buildroot} -name .svn -type d -exec %{__rm} -rf {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST MANIFEST.SKIP META.yml
%doc %{_mandir}/man3/Math::Counting.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/Counting/
%{perl_vendorlib}/Math/Counting.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.0801-1
- Updated to release 0.0801.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.0704-1
- Updated to release 0.0704.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
