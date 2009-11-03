# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SNMP-Multi

Summary: Perform SNMP operations on multiple hosts simultaneously
Name: perl-SNMP-Multi
Version: 2.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SNMP-Multi/

Source: http://www.cpan.org/modules/by-module/SNMP/SNMP-Multi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perform SNMP operations on multiple hosts simultaneously.

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
%doc ChangeLog INSTALL MANIFEST META.yml examples/
%doc %{_mandir}/man3/SNMP::Multi.3pm*
%dir %{perl_vendorlib}/SNMP/
#%{perl_vendorlib}/SNMP/Multi/
%{perl_vendorlib}/SNMP/Multi.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
