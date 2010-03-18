# $Id$
# Authority: shuff
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Check-ISA

Summary: DWIM, correct checking of an object's class
Name: perl-%{real_name}
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Check-ISA/

Source: http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/Check-ISA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::use::ok)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Sub::Exporter)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides several functions to assist in testing whether a value is
an object, and if so asking about its class.

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
%doc Changes MANIFEST SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Check/
%{perl_vendorlib}/Check/*

%changelog
* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial version.
