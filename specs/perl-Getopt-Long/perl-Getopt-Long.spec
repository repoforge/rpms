# $Id$
# Authority: dag
# Upstream: Johan Vromans <jv$cpan,org>

### EL6 ships with Getopt::Long in perl-5.10.1-119.el6_1.1
### EL5 ships with Getopt::Long in perl-5.8.8-32.el5_6.3
### EL4 ships with Getopt::Long in perl-5.8.5-53.el4
### EL3 ships with Getopt::Long in perl-5.8.0-101.EL3
### EL2 ships with Getopt::Long in perl-5.6.1-37.1.99ent
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Long

Summary: Extended processing of command line options
Name: perl-Getopt-Long
Version: 2.38
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Long/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Long-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Extended processing of command line options 

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Announce CHANGES INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Getopt::Long.3pm*
%dir %{perl_vendorlib}/Getopt/
#%{perl_vendorlib}/Getopt/Long/
%{perl_vendorlib}/Getopt/Long.pm
%{perl_vendorlib}/newgetopt.pl

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2.38-1
- Updated to version 2.38.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.37-1
- Updated to release 2.37.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.35-1
- Initial package. (using DAR)
