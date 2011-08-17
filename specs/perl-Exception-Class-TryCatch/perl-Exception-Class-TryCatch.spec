# $Id$
# Authority: gtenagli
# Upstream: David A. Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class-TryCatch

Summary: Syntactic try/catch sugar for use with Exception::Class
Name: perl-Exception-Class-TryCatch
Version: 1.12
Release: 1%{?dist}
License: Apache License, Version 2.0
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exception-Class-TryCatch/

Source: http://www.cpan.org/modules/by-module/Exception/Exception-Class-TryCatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Exception::Class) >= 1.2
BuildRequires: perl(Module::Build) >= 0.2701
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.17
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Exception::Class) >= 1.2

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Exception::Class::TryCatch provides syntactic sugar for use with
Exception::Class using the familiar keywords try and catch. Its primary
objective is to allow users to avoid dealing directly with $@ by ensuring that
any exceptions caught in an eval are captured as Exception::Class objects,
whether they were thrown objects to begin with or whether the error resulted
from die. This means that users may immediately use isa and various
Exception::Class methods to process the exception.

In addition, this module provides for a method to push errors onto a hidden
error stack immediately after an eval so that cleanup code or other error
handling may also call eval without the original error in $@ being lost.


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
%doc %{_mandir}/man3/Exception::Class::TryCatch.3pm*
%dir %{perl_vendorlib}/Exception/
%dir %{perl_vendorlib}/Exception/Class/
#%{perl_vendorlib}/Exception/Class/TryCatch/
%{perl_vendorlib}/Exception/Class/TryCatch.pm
%{perl_vendorlib}/Exception/Class/TryCatch.pod

%changelog
* Wed Aug 10 2011 Giacomo Tenaglia <Giacomo.Tenaglia@cern.ch> - 1.12-1
- Initial package.
