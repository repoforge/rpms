# $Id$
# Authority: shuff
# Upstream: Filipe Dutra <mopy$cpan,org>
## ExcludeDist: el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-Temperature

Summary: Convert Temperatures
Name: perl-%{real_name}
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-Temperature/

Source: http://search.cpan.org/CPAN/authors/id/M/MO/MOPY/Convert-Temperature-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.8


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Utility functions to convert between Fahrenheit, Celsius, Kelvin, Rankine, and
Reaumur temperature scales in Perl.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Convert/
%{perl_vendorlib}/Convert/*

%changelog
* Tue Nov 03 2009 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
