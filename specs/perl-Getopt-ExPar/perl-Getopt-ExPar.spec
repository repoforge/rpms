# $Id$
# Authority: dries
# Upstream: Harlin L. Hamilton Jr. <harlinh$cadence,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-ExPar

Summary: Extended Parameters command line parser
Name: perl-Getopt-ExPar
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-ExPar/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-ExPar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Extended Parameters, Getopt::ExPar, is written as a possible alternative
to current getopt packages.  Based, for the most part, on Stephen Lidie's
Getopt::EvaP package, this has several features that go beyond EvaP's
capabilities.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/rwasics_apps/gnu/bin/perl|/usr/bin/perl|g;' *.pl *.pm

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
%{perl_vendorlib}/Getopt/ExPar.pm
%{perl_vendorlib}/Getopt/Reference_Parser.pm
%{perl_vendorlib}/Getopt/expar_test.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
