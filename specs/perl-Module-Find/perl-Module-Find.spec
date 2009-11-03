# $Id$
# Authority: dries
# Upstream: Christian Renz <crenz$web42,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Find

Summary: Find and use installed modules in a (sub)category
Name: perl-Module-Find
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Find/

Source: http://www.cpan.org/authors/id/C/CR/CRENZ/Module-Find-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Module/Module-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Pod) >= 1.14
BuildRequires: perl(Test::Pod::Coverage) >= 1.04

%description
Module::Find lets you and use modules in categoris. This can be very useful
for auto-detecting driver or plug-in modules. You can differentiate between
looking in the category itself or in all subcategories.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.skip META.yml README examples/
%doc %{_mandir}/man3/Module::Find.3pm*
%dir %{perl_vendorlib}/Module/
#%{perl_vendorlib}/Module/Find/
%{perl_vendorlib}/Module/Find.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Fri Aug 11 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.05-1
- Initial packaging.
