# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SNMP
%define real_version 1.1001

Summary: Perl module that implements a POE interface to Net::SNMP
Name: perl-POE-Component-SNMP
Version: 1.10.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SNMP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-SNMP-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-POE-Component-SNMP is a Perl module that implements a POE interface
to Net::SNMP.

%prep
%setup -n %{real_name}-%{real_version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml NOTES README eg/
%doc %{_mandir}/man3/POE::Component::SNMP.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SNMP/
%{perl_vendorlib}/POE/Component/SNMP.pm

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.10.01-1
- Updated to version 1.10.01.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
