# $Id$
# Authority: dries
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Extract

Summary: Generic archive extracting mechanism
Name: perl-Archive-Extract
Version: 0.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Extract/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Extract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A generic archive extracting mechanism.

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
%doc %{_mandir}/man3/Archive::Extract.3pm*
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Extract.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
