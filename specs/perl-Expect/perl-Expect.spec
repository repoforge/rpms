# $Id$
# Authority: dries
# Upstream: Roland Giersig <RGiersig$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Expect

Summary: Expect for perl
Name: perl-Expect
Version: 1.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Expect/

Source: http://www.cpan.org/modules/by-module/Expect/Expect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a version of expect written in perl.

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

### Clean up docs
find examples/ tutorial/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/ tutorial/
%doc %{_mandir}/man3/Expect.3pm*
#%{perl_vendorlib}/Expect/
%{perl_vendorlib}/Expect.pm
%{perl_vendorlib}/Expect.pod

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-2
- Removed bad dependency (found by Martijn Lievaart, thanks!)

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
