# $Id$
# Authority: dries
# Upstream: Kim Ryan <kimryan%20nospam$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-SubCountry

Summary: Convert state, county, province etc names to/from code
Name: perl-Locale-SubCountry
Version: 1.34
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-SubCountry/

Source: http://search.cpan.org/CPAN/authors/id/K/KI/KIMRYAN/Locale-SubCountry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to convert the full name for a countries administrative
region to the code commonly used for postal addressing. The reverse lookup
can also be done.  Sub country codes are defined in "ISO 3166-2:1998,
Codes for the representation of names of countries and their subdivisions".

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
%{perl_vendorlib}/Locale/SubCountry.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.34-1
- Initial package.
