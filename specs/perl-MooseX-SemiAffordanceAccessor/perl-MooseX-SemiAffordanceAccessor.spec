# $Id$
# Authority: shuff
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-SemiAffordanceAccessor

Summary: Name your accessors foo() and set_foo()
Name: perl-%{real_name}
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-SemiAffordanceAccessor/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/MooseX-SemiAffordanceAccessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Module::Build::Compat) >= 0.02
BuildRequires: perl(Moose) >= 0.84
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose) >= 0.84


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module does not provide any methods. Simply loading it changes the default
naming policy for the loading class so that accessors are separated into get
and set methods. The get methods have the same name as the accessor, while set
methods are prefixed with "set_".

If you define an attribute with a leading underscore, then the set method will
start with "_set_".

If you explicitly set a "reader" or "writer" name when creating an attribute,
then that attribute's naming scheme is left unchanged.

The name "semi-affordance" comes from David Wheeler's Class::Meta module.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/*

%changelog
* Fri Dec 18 2009 Steve Huff <shuff@vecna.org> - 0.05-1
- Initial package.
