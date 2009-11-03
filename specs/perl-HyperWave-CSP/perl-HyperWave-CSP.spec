# $Id$
# Authority: dries
# Upstream: Ricky Buchanan <rb$tertius,net,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HyperWave-CSP

Summary: Communicate with a HyperWave server
Name: perl-HyperWave-CSP
Version: 0.03.1
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HyperWave-CSP/

Source: http://www.cpan.org/modules/by-module/HyperWave/HyperWave-CSP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is not finished. However, some of it -does- work.  Everything in
the examples directory works more or less, and should give you an idea of how
it can be used.

CSP stands for Client-Server-Protocol which is the official name
for the native HyperWave Protocol.  That also leaves space in the
namespace for somebody to write a module for the server-server
protocol.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HyperWave/CSP.pm
%{perl_vendorlib}/HyperWave/CSP

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03.1-1
- Initial package.
