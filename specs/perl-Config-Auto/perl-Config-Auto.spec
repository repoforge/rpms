# $Id$
# Authority: cmr
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Auto

Summary: Magical config file parser
Name: perl-Config-Auto
Version: 0.20
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Auto/

Source: http://www.cpan.org/modules/by-module/Config/Config-Auto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Config::IniFiles)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Config::IniFiles)
Requires: perl(File::Spec::Functions)
Requires: perl(YAML)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module was written after having to write Yet Another Config File Parser
for some variety of colon-separated config. I decided "never again".

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
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/Auto/
%{perl_vendorlib}/Config/Auto.pm

%changelog
* Tue Apr 06 2010 Steve Huff <shuff@vecna.org> - 0.20-2
- Captured missing dependencies.

* Mon Jun 29 2009 Unknown - 0.20-1
- Initial package. (using DAR)
