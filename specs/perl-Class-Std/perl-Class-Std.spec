# $Id$
# Authority: ae
# Upstream: Damian Conway <damian$conway,org>

### Package included in extras beginning with fc5
##ExclusiveDist: fc1 fc2 fc3 fc4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Std
%define real_version 0.000009

Summary: Implementation of a "Std" class
Name: perl-Class-Std
Version: 0.0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Std/

Source: http://www.cpan.org/modules/by-module/Class/Class-Std-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides tools that help to implement the 
"inside out object" class structure in a convenient and standard way.

Portions of the following code and documentation from 
"Perl Best Practices" copyright (c) 2005 by O'Reilly Media, Inc. 
and reprinted with permission.

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
%doc %{_mandir}/man3/Class::Std.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Std/
%{perl_vendorlib}/Class/Std.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Updated to release 0.0.9.

* Fri Jun 29 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.0.8-1
- Initial package.
