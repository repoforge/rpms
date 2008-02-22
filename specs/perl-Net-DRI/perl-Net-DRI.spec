# $Id$
# Authority: dries
# Upstream: Patrick Mevzek <netdri$dotandco,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DRI

Summary: Interface to Domain Name Registries/Registrars/Resellers
Name: perl-Net-DRI
Version: 0.85
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DRI/

Source: http://www.cpan.org/modules/by-module/Net/Net-DRI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Net::DRI is a Perl library which offers a uniform API to access services
from domain name registries, registrars, and resellers. It is an
object-oriented framework that can be easily extended to handle various
protocols (such as RRP, EPP, or custom protocols) and various transports
methods (such as TCP, TLS, SOAP, or email).

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST META.yml README TODO eg/
%doc %{_mandir}/man3/Net::DRI.3pm*
%doc %{_mandir}/man3/Net::DRI::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/DRI/
%{perl_vendorlib}/Net/DRI.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
