# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Params-Validate

Summary: Validate method/function parameters
Name: perl-Params-Validate
Version: 0.94
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Params-Validate/

Source: http://www.cpan.org/modules/by-module/Params/Params-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
#BuildRequires: perl(Attribute::Handlers) >= 0.79
BuildRequires: perl(Attribute::Handlers)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Pod::Man) >= 1.14
BuildRequires: perl(Scalar::Util) >= 1.10
BuildRequires: perl(Test::More)
#Requires: perl(Attribute::Handlers) >= 0.79
Requires: perl(Attribute::Handlers)
Requires: perl(Scalar::Util) >= 1.10
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

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
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Attribute::Params::Validate.3pm*
%doc %{_mandir}/man3/Params::Validate.3pm*
%doc %{_mandir}/man3/Params::ValidatePP.3pm*
%doc %{_mandir}/man3/Params::ValidateXS.3pm*
%dir %{perl_vendorarch}/auto/Params/
%{perl_vendorarch}/auto/Params/Validate/
%dir %{perl_vendorarch}/Attribute/
%dir %{perl_vendorarch}/Attribute/Params/
%{perl_vendorarch}/Attribute/Params/Validate.pm
%dir %{perl_vendorarch}/Params/
%{perl_vendorarch}/Params/Validate.pm
%{perl_vendorarch}/Params/ValidatePP.pm
%{perl_vendorarch}/Params/ValidateXS.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.94-1
- Updated to version 0.94.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.89-1
- Updated to release 0.89.

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
