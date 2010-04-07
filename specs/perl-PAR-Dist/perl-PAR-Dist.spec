# $Id$
# Authority: dries
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PAR-Dist

Summary: Create and manipulate PAR distributions
Name: perl-PAR-Dist
Version: 0.47
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PAR-Dist/

Source: http://www.cpan.org/modules/by-module/PAR/PAR-Dist-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
Requires: perl(File::Find)
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(File::Temp)

%filter_from_requires /^perl*/d
%filter_setup

%description
With this module, you can create and manipulate PAR distributions.

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
%doc %{_mandir}/man3/PAR::Dist.3pm*
%dir %{perl_vendorlib}/PAR/
#%{perl_vendorlib}/PAR/Dist/
%{perl_vendorlib}/PAR/Dist.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.47-1
- Updated to version 0.47.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 0.46-1
- Updated to version 0.46.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.45-1
- Updated to version 0.45.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
