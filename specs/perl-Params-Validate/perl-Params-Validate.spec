# $Id: $

# Authority: dries
# Upstream:

%define real_name Params-Validate
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Validation of method parameters
Name: perl-Params-Validate
Version: 0.74
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Attribute/Params/Validate.pm
%{perl_vendorarch}/Params/Validate*
%{perl_vendorarch}/auto/Params/Validate/Validate.*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/Params/Validate/.packlist

%changelog
* Sun Jun 6 2004 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Initial package.
