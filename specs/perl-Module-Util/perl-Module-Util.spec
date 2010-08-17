# $Id$
# Authority: shuff
# Upstream: Matt Lawrence <mattlaw$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Util

Summary: Module name tools and transformations
Name: perl-Module-Util
Version: 1.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Util/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MATTLAW/Module-Util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.5.3
BuildRequires: perl(Module::Build::Compat) >= 0.02
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.5.3

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a few useful functions for manipulating module names. Its
main aim is to centralise some of the functions commonly used by modules that
manipulate other modules in some way, like converting module names to relative
paths.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/Module/Util.pm
#%{perl_vendorlib}/Module/Util/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Aug 17 2010 Steve Huff <shuff@vecna.org> - 1.07-1
- Initial package.
