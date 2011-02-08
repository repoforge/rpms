# $Id$
# Authority: shuff
# Upstream: Father Chrysostomos <sprout$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Util

Summary: Utility functions for fiddling with tied variables
Name: perl-%{real_name}
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Util/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/Tie-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(B)
BuildRequires: perl(constant)
BuildRequires: perl(Exporter) >= 5.57
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(overload)
BuildRequires: perl(Scalar::Util) >= 1.09
BuildRequires: perl(Symbol)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: perl(warnings)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(B)
Requires: perl(constant)
Requires: perl(Exporter) >= 5.57
Requires: perl(overload)
Requires: perl(Scalar::Util) >= 1.09
Requires: perl(Symbol)
Requires: perl(constant)
Requires: perl(overload)
Requires: perl(warnings)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a few subroutines for examining and modifying tied
variables, including those that hold weak references to the objects to which
they are tied (weak ties).

It also provides tie constructors in the to:: namespace, so that you can tie
variables to existing objects, like this:

  tie $var, to => $obj;
  weak_tie @var, to => $another_obj; # for a weak tie

It also allows one to tie a variable to a package, instead of an object.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Tie/
%{perl_vendorlib}/Tie/*

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.03-1
- Updated to version 0.03.

* Wed May 05 2010 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial package.
