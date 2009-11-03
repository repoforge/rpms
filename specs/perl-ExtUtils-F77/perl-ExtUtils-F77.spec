# $Id$
# Authority: dries
# Upstream: Karl Glazebrook <karlglazebrook$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-F77

Summary: Simple interface to F77 libs
Name: perl-ExtUtils-F77
Version: 1.16
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-F77/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-F77-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module tries to figure out how to link C programs with
Fortran subroutines on your system. Basically one must add a list
of Fortran runtime libraries. The problem is their location
and name varies with each OS/compiler combination!

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
%doc CHANGES COPYING MANIFEST META.yml README
%doc %{_mandir}/man3/ExtUtils::F77.3pm*
%dir %{perl_vendorlib}/ExtUtils/
#%{perl_vendorlib}/ExtUtils/F77/
%{perl_vendorlib}/ExtUtils/F77.pm
%{perl_vendorlib}/ExtUtils/._F77.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
