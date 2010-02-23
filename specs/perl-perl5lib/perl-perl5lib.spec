# $Id$
# Authority: shuff
# Upstream: Brian McCauley <nobull67$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name perl5lib

Summary: Honour PERL5LIB even in taint mode
Name: perl-%{real_name}
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/perl5lib/

Source: http://search.cpan.org/CPAN/authors/id/N/NO/NOBULL/perl5lib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl's taint mode was originally intended for setuid scripts. In that situation
it would be unsafe for Perl to populate @INC from $ENV{PERL5LIB}. The explicit
-T flag is now often used in CGI scripts and suchlike. In such situations it
often makes sense to consider $ENV{PERL5LIB} as untainted.

This module uses the lib module to simulate the effect of non-taint mode Perl's
default handling of $ENV{PERL5LIB}.

As a side effect any directories in $ENV{PERL5LIB} are brought to the front of
@INC. Occasionally this may be useful if one needs an explict use lib for a
project but one still wants development versions in one's personal module
directory to override.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Tue Feb 23 2010 Steve Huff <shuff@vecna.org> - 1.02-1
- Initial package.
