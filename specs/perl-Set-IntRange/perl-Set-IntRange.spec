# $Id$

# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define real_name Set-IntRange
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Sets of Integers
Name: perl-Set-IntRange
Version: 5.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-IntRange/

Source: http://www.cpan.org/modules/by-module/Set/Set-IntRange-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Bit::Vector) >= 7.1
Requires: perl(Bit::Vector) >= 7.1

%filter_from_requires /^perl*/d
%filter_setup


%description
This module allows you to work with sets of integers.

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
%doc README.txt
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Set/IntRange.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 5.2-1
- Updated to version 5.2.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 5.1-1.2
- Rebuild for Fedora Core 5.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 5.1-1
- Initial package.

