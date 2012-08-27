# $Id$
# Authority: shuff
# Upstream: Dominique Dumont <domi.dumont$free,fr>

# ExcludeDist el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%{?el5:%global _with_gcc44 1}

%define real_name Config-Augeas

Summary: Edit configuration files through Augeas C library
Name: perl-Config-Augeas
Version: 0.903
Release: 1%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Augeas/

Source: http://search.cpan.org/CPAN/authors/id/R/RA/RAPHINK/Config-Augeas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: augeas-devel
BuildRequires: %{?_with_gcc44:gcc44}%{!?_with_gcc44:gcc >= 4.4}
BuildRequires: perl
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: pkgconfig
BuildRequires: rpm-macros-rpmforge
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Augeas is a library and command line tool that focuses on the most basic
problem in handling Linux configurations programmatically: editing actual
configuration files in a controlled manner.

To that end, Augeas exposes a tree of all configuration settings (well, all the
ones it knows about) and a simple local API for manipulating the tree. Augeas
then modifies underlying configuration files according to the changes that have
been made to the tree; it does as little modeling of configurations as
possible, and focuses exclusively on transforming the tree-oriented syntax of
its public API to the myriad syntaxes of individual configuration files.

This module provides an object oriented Perl interface for Augeas configuration
edition library with a more "perlish" API than Augeas C counterpart.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL \
    --installdirs="vendor" \
    --prefix="%{buildroot}%{_prefix}" \
    --config cc=%{?_with_gcc44:gcc44}%{!?_with_gcc44:gcc}

%install
%{__rm} -rf %{buildroot}
./Build pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog META.json README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Config/Augeas.pm
%{perl_vendorarch}/auto/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Aug 03 2012 Steve Huff <shuff@vecna.org> - 0.903-1
- Updated to version 0.903.

* Tue Feb 01 2011 Steve Huff <shuff@vecna.org> - 0.701-1
- Initial package.
