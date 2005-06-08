# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filter-Simple

Summary: Simplified source filtering
Name: perl-Filter-Simple
Version: 0.80
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filter-Simple/

Source: http://www.cpan.org/modules/by-module/Filter/Filter-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module permits simplified source filtering.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Filter/
%{perl_vendorlib}/Filter/Simple.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Initial package.
