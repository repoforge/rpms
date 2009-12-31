# $Id$
# Authority: shuff
# Upstream: Steve Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Natural

Summary: Create machine readable date/time with natural parsing logic
Name: perl-%{real_name}
Version: 0.82
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Natural/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(DateTime)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Term::ReadLine)
# BuildRequires: perl(Test::MockTime) 
BuildRequires: perl(Test::More)
BuildRequires: perl(boolean)
Requires: perl(Carp)
Requires: perl(DateTime)
Requires: perl(Exporter)
Requires: perl(List::MoreUtils)
Requires: perl(Params::Validate)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(Term::ReadLine)
Requires: perl(boolean)

Provides: %{_bindir}/dateparse

%filter_from_requires /^perl*/d
%filter_setup

%description
DateTime::Format::Natural takes a string with a human readable date/time and
creates a machine readable one by applying natural parsing logic.

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
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/Natural/
%{perl_vendorlib}/DateTime/Format/Natural.pm
%{_bindir}/*

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.82-1
- Updated to version 0.82.

* Mon Dec 07 2009 Steve Huff <shuff@vecna.org> - 0.81-1
- Initial package.
