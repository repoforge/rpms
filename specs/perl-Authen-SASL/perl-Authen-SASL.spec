# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%{?el3:%define _without_gssapi 1}
%{?rh9:%define _without_gssapi 1}
%{?rh7:%define _without_gssapi 1}
%{?el2:%define _without_gssapi 1}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-SASL

Summary: Interface to SASL
Name: perl-Authen-SASL
Version: 2.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-SASL/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-SASL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Digest::HMAC_MD5)
%{!?_without_gssapi:BuildRequires: perl(GSSAPI)}

%description
This module permits authentication with SASL.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc api.txt Changes example_pl
%{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Authen/
%{perl_vendorlib}/Authen/SASL.pm
%{perl_vendorlib}/Authen/SASL.pod
%{perl_vendorlib}/Authen/SASL/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.

