# $Id$

# Authority: dries
# Upstream: Martin Kutter <martin,kutter$sourceforge,net>

%define real_name SOAP-WSDL
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: WSDL-driven message preprocessor for SOAP::Lite
Name: perl-SOAP-WSDL
Version: 1.20
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-WSDL/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A WSDL-driven message preprocessor for SOAP::Lite.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SOAP/WSDL.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
