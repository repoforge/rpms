# $Id$
# Authority: dries
# Upstream: Steve A Fink <sfink$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Calc-Units

Summary: Human-readable unit-aware calculator
Name: perl-Math-Calc-Units
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Calc-Units/

Source: http://search.cpan.org/CPAN/authors/id/S/SF/SFINK/Math-Calc-Units-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Human-readable unit-aware calculator.

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
%{_bindir}/ucalc
%{perl_vendorlib}/Math/Calc/Units.pm
%{perl_vendorlib}/Math/Calc/Units

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
