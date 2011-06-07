# $Id$
# Authority: shuff
# Upstream: Marcel Gruenauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Constructor

Summary: Constructor generator
Name: perl-Class-Accessor-Constructor
Version: 1.100880
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Constructor/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Class-Accessor-Constructor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Accessor::Complex)
BuildRequires: perl(Class::Accessor::Installer)
BuildRequires: perl(Data::Inherited)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Tie::Hash)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(parent)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.0
Requires: perl(Carp)
Requires: perl(Class::Accessor)
Requires: perl(Class::Accessor::Complex)
Requires: perl(Class::Accessor::Installer)
Requires: perl(Data::Inherited)
Requires: perl(English)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(Tie::Hash)
Requires: perl(Scalar::Util)
Requires: perl(Test::More)
Requires: perl(constant)
Requires: perl(parent)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module generates accessors for your class in the same spirit as
Class::Accessor does. While the latter deals with accessors for scalar values,
this module provides accessor makers for rather flexible constructors.

The accessor generators also generate documentation ready to be used with
Sub::Documentation.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
# %{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\\.31.*/ && s/6\\.3\\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Class/Accessor/Constructor.pm
%{perl_vendorlib}/Class/Accessor/Constructor/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Jun 07 2011 Steve Huff <shuff@vecna.org> - 1.100880-1
- Initial package.
