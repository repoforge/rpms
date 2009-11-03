# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Classgen-classgen

Summary: Simplifies creation, manipulation and usage of complex objects
Name: perl-Class-Classgen-classgen
Version: 3.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Classgen-classgen/

Source: http://www.cpan.org/authors/id/M/MS/MSCHLUE/Class-Classgen-classgen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simplifies creation, manipulation and usage of complex objects.

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
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man1/classgen.1*
%doc %{_mandir}/man3/Class::Classgen::*.3pm*
%{_bindir}/classgen
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Classgen/

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 3.03-1
- Initial package. (using DAR)
