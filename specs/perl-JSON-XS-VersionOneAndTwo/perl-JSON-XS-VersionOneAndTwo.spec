# $Id$
# Authority: shuff
# Upstream: Leon Brocard <acme$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS-VersionOneAndTwo

Summary: Support versions 1 and 2 of JSON::XS
Name: perl-%{real_name}
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-XS-VersionOneAndTwo/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/JSON-XS-VersionOneAndTwo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(JSON::XS)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
JSON::XS is by far the best JSON module on the CPAN. However, it changed its
API at version 2.01. If you have to maintain code which may be run on systems
with either version one or two then this is a bit of a pain. This module takes
the pain away without sacrificing performance.

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/JSON/XS/
%{perl_vendorlib}/JSON/XS/*

%changelog
* Thu Feb 25 2010 Steve Huff <shuff@vecna.org> - 0.31-1
- Initial package.
