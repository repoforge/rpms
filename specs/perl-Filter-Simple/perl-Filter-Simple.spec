# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filter-Simple

Summary: Simplified source filtering
Name: perl-Filter-Simple
Version: 0.84
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filter-Simple/

Source: http://www.cpan.org/modules/by-module/Filter/Filter-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module permits simplified source filtering.

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
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Filter/
%{perl_vendorlib}/Filter/Simple.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.84-1
- Updated to version 0.84.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.82-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.82-1
- Updated to release 0.82.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Initial package.
