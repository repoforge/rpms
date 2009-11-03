# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quantum-Usrn

Summary: Perl module to calculate square root of not
Name: perl-Quantum-Usrn
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quantum-Usrn/

Source: http://www.cpan.org/modules/by-module/Quantum/Quantum-Usrn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Quantum-Usrn is a Perl module to calculate square root of not.
Name: perl-Quantum-Usrn

This package contains the following Perl module:

    Quantum::Usrn

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
%doc MANIFEST
%doc %{_mandir}/man3/Quantum::Usrn.3pm*
%dir %{perl_vendorlib}/Quantum/
%{perl_vendorlib}/Quantum/Usrn.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
