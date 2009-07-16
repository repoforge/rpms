# $Id$
# Authority: dries
# Upstream: Pierre Denis <pdenis$fotango,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Hook

Summary: Add hooks on methods from other classes
Name: perl-Class-Hook
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Hook/

Source: http://www.cpan.org/modules/by-module/Class/Class-Hook-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Time::HiRes)

%description
Class::Hook enables you to trace methods calls from your code to other
classes.

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
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/FOO.pm
%{perl_vendorlib}/Class/Hook.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
