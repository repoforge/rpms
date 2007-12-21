# $Id$
# Authority: dries
# Upstream: Martin Kutter <martin,kutter$sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-WSDL

Summary: WSDL-driven message preprocessor for SOAP::Lite
Name: perl-SOAP-WSDL
Version: 1.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-WSDL/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker), perl(Module::Build)

%description
A WSDL-driven message preprocessor for SOAP::Lite.

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
%doc CHANGES HACKING MANIFEST META.yml README
%doc %{_mandir}/man3/SOAP::WSDL.3pm*
%dir %{perl_vendorlib}/SOAP/
#%{perl_vendorlib}/SOAP/WSDL/
%{perl_vendorlib}/SOAP/WSDL.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
