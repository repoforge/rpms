# $Id$
# Authority: dag

### EL6 ships with perl-Class-Data-Inheritable-0.08-3.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Data-Inheritable

Summary: Inheritable, overridable class data
Name: perl-Class-Data-Inheritable
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Data-Inheritable/

Source: http://www.cpan.org/modules/by-module/Class/Class-Data-Inheritable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Inheritable, overridable class data.

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
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README doc/
%doc %{_mandir}/man3/Class::Data::Inheritable.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Data/
#%{perl_vendorlib}/Class/Data/Inheritable/
%{perl_vendorlib}/Class/Data/Inheritable.pm


%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
