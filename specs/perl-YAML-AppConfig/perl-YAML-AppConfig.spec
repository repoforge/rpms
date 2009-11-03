# $Id$
# Authority: dag
# Upstream: Matthew O'Connor <moconnor$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-AppConfig

Summary: Perl module to manage configuration files with YAML and variable reference
Name: perl-YAML-AppConfig
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-AppConfig/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-AppConfig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(YAML)

%description
perl-YAML-AppConfig is a Perl module to manage configuration files with YAML
and variable reference.

This package contains the following Perl module:

    YAML::AppConfig

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/YAML::AppConfig.3pm*
%dir %{perl_vendorlib}/YAML/
%{perl_vendorlib}/YAML/AppConfig.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.16-1
- Initial package. (using DAR)
