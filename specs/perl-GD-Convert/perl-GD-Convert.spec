# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GD-Convert

Summary: Additional output formats for GD
Name: perl-GD-Convert
Version: 2.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD-Convert/

Source: http://www.cpan.org/modules/by-module/GD/GD-Convert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
GD::Convert is a pure perl module which provides additional output
functions for the GD module: ppm and xpm. These formats are useful if
you need to dynamically create photos for Tk. Perl/Tk lesser than
version 804 does not accept any of GD's output formats: png only via
the additional Tk::PNG module and jpeg only via the additional
Tk::JPEG module. So if you cannot compile on your system, this module
is for you.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/GD::Convert.3pm*
%dir %{perl_vendorlib}/GD/
#%{perl_vendorlib}/GD/Convert/
%{perl_vendorlib}/GD/Convert.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2.16-1
- Updated to version 2.16.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.15-1
- Updated to release 2.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.13-1
- Updated to release 2.13.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Initial package.
