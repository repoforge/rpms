# $Id$
# Authority: gtenagli
# Upstream: David A. Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class-TryCatch

Summary: TryCatch Exception objects
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
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Module::Build) >= 0.2701
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.17

%description
Syntactic try/catch sugar for use with Exception::Class.

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
