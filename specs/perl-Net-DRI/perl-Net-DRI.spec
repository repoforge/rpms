# $Id$
# Authority: dries
# Upstream: Patrick Mevzek <patrick$deepcore,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DRI

Summary: Uniform API to access domain registries, registrars and resellers
Name: perl-Net-DRI
Version: 0.80
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DRI/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMEVZEK/Net-DRI-%{version}.tar.gz
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
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Net::DRI*
%{perl_vendorlib}/Net/DRI.pm
%{perl_vendorlib}/Net/DRI/

%changelog
* Fri Apr 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
