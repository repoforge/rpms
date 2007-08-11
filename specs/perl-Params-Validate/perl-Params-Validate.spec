# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Params-Validate

Summary: Validation of method parameters
Name: perl-Params-Validate
Version: 0.86
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Source: http://www.cpan.org/modules/by-module/Params/Params-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.  The validation can be as simple as
checking for the presence of required parameters or as complex as
validating object classes (via isa) or capabilities (via can),
checking parameter types, and using customized callbacks to ensure
data integrity.

The module has been designed to work equally well with positional or
named parameters (as a hash or hash reference).

It includes both a fast XS implementation, and a slower pure Perl
implementation that it can fall back on.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Params/Validate/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Attribute/
%dir %{perl_vendorarch}/Attribute/Params/
%{perl_vendorarch}/Attribute/Params/Validate.pm
%dir %{perl_vendorarch}/Params/
%{perl_vendorarch}/Params/Validate*
%dir %{perl_vendorarch}/auto/Params/
%dir %{perl_vendorarch}/auto/Params/Validate/
%{perl_vendorarch}/auto/Params/Validate/Validate.*

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.86-1
- Updated to release 0.86.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.84-1
- Updated to release 0.84.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Updated to release 0.78.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Updated to release 0.77.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.76-1
- Updated to release 0.76.

* Sun Jun 6 2004 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Initial package.
