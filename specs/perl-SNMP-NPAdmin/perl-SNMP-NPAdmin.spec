# $Id$
# Authority: cmr
# Upstream: Robert Lehr <bozzio$the-lehrs,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SNMP-NPAdmin

Summary: Perl module named SNMP-NPAdmin
Name: perl-SNMP-NPAdmin
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SNMP-NPAdmin/

Source: http://www.cpan.org/modules/by-module/SNMP/SNMP-NPAdmin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-SNMP-NPAdmin is a Perl module.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/npadmin.1*
%doc %{_mandir}/man3/SNMP::NPAdmin.3pm*
%dir %{perl_vendorlib}/SNMP/
%{_bindir}/npadmin
%{perl_vendorlib}/SNMP/NPAdmin/MIBs/JETDIRECT3-MIB.txt
%{perl_vendorlib}/SNMP/NPAdmin/MIBs/Printer-MIB.txt
%{perl_vendorlib}/SNMP/NPAdmin/Neon.pm
%{perl_vendorlib}/SNMP/NPAdmin.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 1.0-1
- Initial package. (using DAR)
