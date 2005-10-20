# $Id$

# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>


%define real_name Params-Validate
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Validation of method parameters
Name: perl-Params-Validate
Version: 0.77
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Source: http://www.cpan.org/modules/by-module/Params/Params-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Params/Validate/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorarch}/Attribute/Params/Validate.pm
%{perl_vendorarch}/Params/Validate*
%{perl_vendorarch}/auto/Params/Validate/Validate.*

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Updated to release 0.77.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.76-1
- Updated to release 0.76.

* Sun Jun 6 2004 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Initial package.
