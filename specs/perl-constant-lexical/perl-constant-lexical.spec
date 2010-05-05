# $Id$
# Authority: shuff
# Upstream: Father Chrysostomos <sprout$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name constant-lexical

Summary: Perl pragma to declare lexical compile-time constants
Name: perl-%{real_name}
Version: 2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/constant-lexical/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/constant-lexical-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(constant) >= 1.03
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sub::Delete)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(constant) >= 1.03
Requires: perl(Sub::Delete)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module creates compile-time constants in the manner of constant.pm, but
makes them local to the enclosing scope.

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
%dir %{perl_vendorlib}/constant/
%{perl_vendorlib}/constant/*

%changelog
* Wed May 05 2010 Steve Huff <shuff@vecna.org> - 2-1
- Initial package.
