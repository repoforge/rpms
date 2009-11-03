# $Id$
# Authority: dries
# Upstream: Christopher J, Madsen <perl$cjmweb,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-CPHash

Summary: Case preserving but case insensitive hash table
Name: perl-Tie-CPHash
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-CPHash/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-CPHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FindBin)
BuildRequires: perl(Module::Build) >= 0.21
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.005

%description
This module provides a case preserving but case insensitive hash.

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
%doc %{_mandir}/man3/Tie::CPHash.3pm*
%dir %{perl_vendorlib}/Tie/
#%{perl_vendorlib}/Tie/CPHash/
%{perl_vendorlib}/Tie/CPHash.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.001-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.001-1
- Initial package.
