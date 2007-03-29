# $Id$
# Authority: dries
# Upstream: Ben Tilly <ben_tilly$operamail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Fleximal

Summary: Integers with flexible representations
Name: perl-Math-Fleximal
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Fleximal/

Source: http://search.cpan.org/CPAN/authors/id/T/TI/TILLY/Math-Fleximal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
This is a module for doing integer arithmetic in arbitrary base
representations.  A representation, or "flex", is determined by
what symbols you use for +, -, and the digits.  The base that
you are working in is the number of digits you use to represent
your numbers.

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
%{perl_vendorlib}/Math/Fleximal.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
