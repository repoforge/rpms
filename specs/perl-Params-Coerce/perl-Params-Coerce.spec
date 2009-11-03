# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Params-Coerce

Summary: Allows your classes to do coercion of parameters
Name: perl-Params-Coerce
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Params-Coerce/

Source: http://www.cpan.org/modules/by-module/Params/Params-Coerce-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.5
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.5

%description
Allows your classes to do coercion of parameters.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Params::Coerce.3pm*
%dir %{perl_vendorlib}/Params/
%{perl_vendorlib}/Params/Coerce.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
