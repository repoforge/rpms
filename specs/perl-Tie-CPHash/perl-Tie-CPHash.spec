# $Id$
# Authority: dries
# Upstream: Christopher J. Madsen <cjm$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-CPHash

Summary: Case preserving but case insensitive hash table
Name: perl-Tie-CPHash
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-CPHash/

Source: http://search.cpan.org/CPAN/authors/id/C/CJ/CJM/Tie-CPHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides a case preserving but case insensitive hash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/CPHash.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.001-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.001-1
- Initial package.
