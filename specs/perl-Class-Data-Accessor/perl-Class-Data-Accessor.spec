# $Id$
# Authority: dag
# Upstream: Based on the creative stylings of Damian Conway, Michael G Schwern,

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Data-Accessor

Summary: Inheritable, overridable class and instance data accessor creation
Name: perl-Class-Data-Accessor
Version: 0.04002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Data-Accessor/

Source: http://www.cpan.org/modules/by-module/Class/Class-Data-Accessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
Inheritable, overridable class and instance data accessor creation.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Class::Data::Accessor.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Data/
%{perl_vendorlib}/Class/Data/Accessor.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 0.04002-1
- Updated to release 0.04002.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.04001-1
- Initial package. (using DAR)
