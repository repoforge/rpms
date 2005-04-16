# $Id$
# Authority: dries
# Upstream: Kurt Kincaid <sifukurt$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Solitaire

Summary: Solitaire encryption
Name: perl-Crypt-Solitaire
Version: 2.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Solitaire/

Source: http://search.cpan.org/CPAN/authors/id/S/SI/SIFUKURT/Crypt-Solitaire-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides Solitaire encryption.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/Solitaire.pm
%{perl_vendorlib}/auto/Crypt/Solitaire

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
