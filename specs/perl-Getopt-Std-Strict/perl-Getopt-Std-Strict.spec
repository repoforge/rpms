# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Std-Strict

Summary: Getopt-Std-Strict module for perl
Name: perl-Getopt-Std-Strict
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Std-Strict/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/Getopt-Std-Strict-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Getopt::Std) >= 1.05
BuildRequires: perl(Test::Simple) >= 0.74
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge

### Remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Getopt-Std-Strict module for perl

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
%doc MANIFEST META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Getopt/Std/

%changelog
* Sun Feb 20 2011 Denis Fateyev <denis@fateyev.com> - 1.01-1
- Initial package.

