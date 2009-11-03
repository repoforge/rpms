# $Id$
# Authority: dries
# Upstream: Andy Wardley <abw$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Singleton

Summary: Implementation of a "Singleton" class
Name: perl-Class-Singleton
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Singleton/

Source: http://www.cpan.org/modules/by-module/Class/Class-Singleton-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is the Class::Singleton module. A Singleton describes an
object class that can have only one instance in any system. An
example of a Singleton might be a print spooler or system
registry. This module implements a Singleton class from which
other classes can be derived. By itself, the Class::Singleton
module does very little other than manage the instantiation of a
single object. In deriving a class from Class::Singleton, your
module will inherit the Singleton instantiation method and can
implement whatever specific functionality is required.

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
%doc %{_mandir}/man3/Class::Singleton.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Singleton/
%{perl_vendorlib}/Class/Singleton.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
