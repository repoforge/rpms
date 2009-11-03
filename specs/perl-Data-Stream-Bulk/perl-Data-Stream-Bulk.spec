# $Id$
# Authority: shuff
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Stream-Bulk

Summary: N at a time iteration API
Name: perl-%{real_name}
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Stream-Bulk/

Source: http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/Data-Stream-Bulk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(namespace::clean) >= 0.08
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::use::ok)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose)
Requires: perl(namespace::clean) >= 0.08
Requires: perl(Sub::Exporter)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module tries to find middle ground between one at a time and all at once
processing of data sets.

The purpose of this module is to avoid the overhead of implementing an
iterative api when this isn't necessary, without breaking forward compatibility
in case that becomes necessary later on.

The API optimizes for when a data set typically fits in memory and is returned
as an array, but the consumer cannot assume that the data set is bounded.

The API is destructive in order to minimize the chance that resultsets are
leaked due to improper usage.

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
%doc Changes META.yml MANIFEST SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Data/Stream/
%{perl_vendorlib}/Data/Stream/*

%changelog
* Thu Oct 29 2009 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
