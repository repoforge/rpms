# $Id$
# Authority: cmr
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-DATA-Schema

Summary: Perl module named Class-DBI-DATA-Schema
Name: perl-Class-DBI-DATA-Schema
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-DATA-Schema/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-DATA-Schema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Class-DBI-DATA-Schema is a Perl module.

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
%doc %{_mandir}/man3/Class::DBI::DATA::Schema.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%dir %{perl_vendorlib}/Class/DBI/DATA/
#%{perl_vendorlib}/Class/DBI/DATA/Schema/
%{perl_vendorlib}/Class/DBI/DATA/Schema.pm

%changelog
* Thu Jun 11 2009 Unknown - 1.00-1
- Initial package. (using DAR)
