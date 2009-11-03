# $Id$
# Authority: dries
# Upstream: Hakan Ardo <hakan$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Expr

Summary: Parses mathematical expressions
Name: perl-Math-Expr
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Expr/

Source: http://www.cpan.org/modules/by-module/Math/Math-Expr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%doc COPYING MANIFEST README TODO
%doc %{_mandir}/man3/Math::Expr.3pm*
%doc %{_mandir}/man3/Math::Expr::*.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Expr/
%{perl_vendorlib}/Math/Expr.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
