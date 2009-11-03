# $Id$
# Authority: dag
# Upstream: shy <shyder_perl$phreaker,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acpi

Summary: Perl module to get information from ACPI
Name: perl-Acpi
Version: 0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acpi/

Source: http://www.cpan.org/authors/id/S/SH/SHY/acpi/Acpi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acpi is a Perl module to get information from ACPI.

This package contains the following Perl modules:

    Acpi::Battery
    Acpi::Fan
    Acpi::Field
    Acpi::Temperature

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
%doc META.yml README
%doc %{_mandir}/man3/Battery.3pm*
%doc %{_mandir}/man3/Fan.3pm*
%doc %{_mandir}/man3/Field.3pm*
%doc %{_mandir}/man3/Temperature.3pm*
%{perl_vendorlib}/Acpi/

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
