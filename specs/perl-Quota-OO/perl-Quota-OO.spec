# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quota-OO
%define real_version 0.000001

Summary: Perl module for Object Oriented Quota Management and reporting
Name: perl-Quota-OO
Version: 0.0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quota-OO/

Source: http://www.cpan.org/modules/by-module/Quota/Quota-OO-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Quota-OO is a Perl module for Object Oriented Quota Management
and reporting.

This package contains the following Perl module:

    Quota::OO

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
%doc %{_mandir}/man3/Quota::OO.3pm*
%dir %{perl_vendorlib}/Quota/
%{perl_vendorlib}/Quota/._OO.pm
%{perl_vendorlib}/Quota/OO.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
