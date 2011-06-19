# $Id$
# Authority: shuff
# Upstream: Marcel Gruenauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Documentation

Summary: Collect documentation for subroutines
Name: perl-Sub-Documentation
Version: 1.100880
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Documentation/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Sub-Documentation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(Attribute::Handlers)
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.0
Requires: perl(Attribute::Handlers)
Requires: perl(Carp)
Requires: perl(English)
Requires: perl(Exporter)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(Scalar::Util)
Requires: perl(Test::Differences)
Requires: perl(Test::More)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides support for generating documentation for your subroutines.
It does not itself generate the documentation, but relies on tools such as
Pod::Weaver::Transformer::AddMethodAutoDoc - which is a plugin to Pod::Weaver
that is most likely used in conjunction with Dist::Zilla - to put the collected
information to use.

Also see Sub::Documentation::Attributes.

Modules that generate methods - such as Class::Accessor::Installer - might want
to use this module. Class::Accessor::Complex, Class::Accessor::Constructor and
Class::Accessor::FactoryTyped use Class::Accessor::Installer and so support
this kind of auto-generated documentation.

This functions are exported on request.

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
%{perl_vendorlib}/Sub/Documentation.pm
%{perl_vendorlib}/Sub/Documentation/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Jun 07 2011 Steve Huff <shuff@vecna.org> - 1.100880-1
- Initial package.
