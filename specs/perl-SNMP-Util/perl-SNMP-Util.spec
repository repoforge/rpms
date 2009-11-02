# $Id$
# Authority: shuff
# Upstream: Wayne Marquette <wayne.marquette$ascend,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SNMP-Util

Summary: Perform SNMP set,get,walk,next,walk_hash,...
Name: perl-%{real_name}
Version: 1.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SNMP-Util/

Source: http://search.cpan.org/CPAN/authors/id/W/WM/WMARQ/SNMP-Util-%{version}.tar.gz
Patch0: %{name}_noninteractive.patch
Patch1: %{name}_examples-hashbang.patch
Patch2: %{name}_mibdir.patch
Patch3: %{name}_snmpversion.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FileHandle)
BuildRequires: perl(SNMP) >= 1.8
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(FileHandle)
Requires: perl(SNMP) >= 1.8


### filter all autoreq perl module
%filter_from_requires /^perl.*/d
%filter_from_requires /^\/usr\/bin\/perl.*/d
%filter_setup

%description
This Perl library is a set of utilities for configuring and monitoring SNMP
based devices. This library requires the UCD port of SNMP and the SNMP.pm
module writted by Joe Marzot.


%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%doc MANIFEST README examples/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/SNMP/
%{perl_vendorlib}/SNMP/*

%changelog
* Mon Nov 02 2009 Steve Huff <shuff@vecna.org> - 1.8-1
- Initial package.
