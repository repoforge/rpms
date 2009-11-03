# $Id$
# Authority: dag
# Upstream: Domizio Demichelis <perl,4pro,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OOTools

Summary: Collection of pragmas to create constructors and lvalues
Name: perl-OOTools
Version: 2.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OOTools/

Source: http://www.cpan.org/modules/by-module/Object/OOTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-OOTools is a collection of pragmas to easily create constructors methods
and lvalue accessor methods at compile time.

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
%doc %{_mandir}/man3/Class::Error.3pm*
%doc %{_mandir}/man3/Class::Util.3pm*
%doc %{_mandir}/man3/Class::constr.3pm*
%doc %{_mandir}/man3/Class::groups.3pm*
%doc %{_mandir}/man3/Class::props.3pm*
%doc %{_mandir}/man3/Object::groups.3pm*
%doc %{_mandir}/man3/Object::props.3pm*
%doc %{_mandir}/man3/Package::groups.3pm*
%doc %{_mandir}/man3/Package::props.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Error.pm
%{perl_vendorlib}/Class/Util.pm
%{perl_vendorlib}/Class/constr.pm
%{perl_vendorlib}/Class/groups.pm
%{perl_vendorlib}/Class/props.pm
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/groups.pm
%{perl_vendorlib}/Object/props.pm
%dir %{perl_vendorlib}/Package/
%{perl_vendorlib}/Package/groups.pm
%{perl_vendorlib}/Package/props.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.21-1
- Initial package. (using DAR)
