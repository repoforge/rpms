# $Id$
# Authority: dries
# Upstream: Hakan Ardo <hakan$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Expr

Summary: Parses mathematical expressions
Name: perl-Math-Expr
Version: 0.2
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Expr/

Source: http://www.cpan.org/modules/by-module/Math/Math-Expr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Parses mathematical expressions into a tree structure. The expressions
may contain integers, real numbers, alphanumeric variable names,
alphanumeric function names and most other characters might be used
as operators. The operators can consist of multiple characters.
The only limitation is that a variable or function name may not start
on a digit, and not all chars are accepted in operation names.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Expr.pm
%{perl_vendorlib}/Math/Expr

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
