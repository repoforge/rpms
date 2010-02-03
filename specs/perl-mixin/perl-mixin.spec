# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name mixin

Summary: Mix-in inheritance, an alternative to multiple inheritance
Name: perl-mixin
Version: 0.07
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/mixin/

Source: http://www.cpan.org/authors/id/M/MS/MSCHWERN/mixin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More) >= 0.4
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(base)
Requires: perl(base)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module allows mix-in inheritance, an alternative to multiple
inheritance.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build
./Build test

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/mixin.pm
%{perl_vendorlib}/mixin/with.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
