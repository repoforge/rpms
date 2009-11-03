# $Id$
# Authority: dag
# Upstream: Ken MacLeod <ken$bitsko,slc,ut,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Visitor

Summary: Iterator superclass for Class::Visitor
Name: perl-Class-Visitor
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Visitor/

Source: http://www.cpan.org/modules/by-module/Class/Class-Visitor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Iterator superclass for Class::Visitor.

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
%doc ChangeLog Changes MANIFEST README
%doc %{_mandir}/man3/Class::Iter.3pm*
%doc %{_mandir}/man3/Class::Visitor.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Visitor/
%{perl_vendorlib}/Class/Iter.pm
%{perl_vendorlib}/Class/Visitor.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
