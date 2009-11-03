# $Id$
# Authority: dag
# Upstream: Jack Shirazi <jack$JavaPerformanceTuning,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Usage

Summary: Perl module that allows autochecking on arguments
Name: perl-Usage
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Usage/

Source: http://www.cpan.org/modules/by-module/Usage/Usage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Usage is a Perl module that allows autochecking on arguments.

This package contains the following Perl module:

    Usage

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
%doc MANIFEST
#%doc %{_mandir}/man3/Usage.3pm*
%{perl_vendorlib}/Usage.pm
%{perl_vendorlib}/auto/Usage/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
