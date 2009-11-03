# $Id$
# Authority: dries
# Upstream: Manuel Valente <mvalente$ripe,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IP

Summary: Perl extension for manipulating IPv4/IPv6 addresses
Name: perl-Net-IP
Version: 1.25
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IP/

Source: http://www.cpan.org/modules/by-module/Net/Net-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for manipulating IPv4/IPv6 addresses.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README
%doc %{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorlib}/Net/IP.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.24-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
