# $Id$
# Authority: shuff
# Upstream: Rick Measham <rickm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Duration
%define real_version 1.03

Summary: Format and parse DateTime::Durations
Name: perl-%{real_name}
Version: 1.03a
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Duration/

Source: http://search.cpan.org/CPAN/authors/id/R/RI/RICKM/DateTime-Format-Duration-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(DateTime) >= 0.30
BuildRequires: perl(DateTime::Duration)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(DateTime) >= 0.30
Requires: perl(DateTime::Duration)

Provides: perl(DateTime::Format::Duration) = %{version}

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module formats and parses DateTime::Duration objects as well as other
durations representations.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes MANIFEST README LICENSE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/*

%changelog
* Thu Feb 11 2010 Steve Huff <shuff@vecna.org> - 1.03a-1
- Initial package.
