# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Yaml2Html

Summary: Perl module to build an HTML page from a YAML-based document
Name: perl-YAML-Yaml2Html
Version: 0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Yaml2Html/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Yaml2Html-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-YAML-Yaml2Html is a Perl module to build an HTML page
from a YAML-based document.

This package contains the following Perl module:

    YAML::Yaml2Html

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
%doc %{_mandir}/man3/YAML::Yaml2Html.3pm*
%dir %{perl_vendorlib}/YAML/
#%{perl_vendorlib}/YAML/Yaml2Html/
%{perl_vendorlib}/YAML/Yaml2Html.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
