# $Id$

# Authority: dries
# Upstream: Kenneth Albanowski <kjahds$kjahds,com>

%define real_name Sort-Versions
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Module for sorting of revision-like numbers
Name: perl-Sort-Versions
Version: 1.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SortVersions/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-category/13_Internationalization_Locale/Sort/Sort-Versions-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows easy sorting (via comparisons) of mixed text and numeric
strings, similar to the complex "version numbers" that many revision control
packages and shared library systems use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Sort/Versions.pm

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.

