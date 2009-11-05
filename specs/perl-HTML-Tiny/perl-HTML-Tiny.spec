# $Id$
# Authority: shuff
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tiny

Summary: Lightweight, dependency free HTML/XML generation
Name: perl-%{real_name}
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tiny/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDYA/HTML-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(ExtUtils::MakeMaker::Coverage) # not yet packaged
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::Tiny is a simple, dependency free module for generating HTML (and XML).
It concentrates on generating syntactically correct XHTML using a simple Perl
notation.

In addition to the HTML generation functions utility functions are provided to

    * encode and decode URL encoded strings
    * entity encode HTML
    * build query strings
    * JSON encode data structures


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
%doc Changes MANIFEST META.yml README SIGNATURE examples/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/*

%changelog
* Thu Nov 05 2009 Steve Huff <shuff@vecna.org> - 0.92-1
- Initial package.
