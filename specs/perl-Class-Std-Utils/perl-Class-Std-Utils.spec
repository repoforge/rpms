# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Std-Utils
%define real_version 0.000003

Summary: Utility subroutines for building "inside-out" objects
Name: perl-Class-Std-Utils
Version: 0.0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Std-Utils/

Source: http://www.cpan.org/modules/by-module/Class/Class-Std-Utils-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Utility subroutines for building "inside-out" objects.

%prep
%setup -n %{real_name}-v%{version}

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
%doc %{_mandir}/man3/Class::Std::Utils.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Std/
#%{perl_vendorlib}/Class/Std/Utils/
%{perl_vendorlib}/Class/Std/Utils.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Updated to release 0.0.3.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.0.2-1
- Initial package. (using DAR)
