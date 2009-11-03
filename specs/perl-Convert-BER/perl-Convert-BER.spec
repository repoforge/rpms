# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-BER
%define real_version 1.31

Summary: ASN.1 Basic Encoding Rules perl module
Name: perl-Convert-BER
Version: 1.3101
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BER/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-BER-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
ASN.1 Basic Encoding Rules perl module.

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
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man3/Convert::BER.3pm*
%dir %{perl_vendorlib}/Convert/
#%{perl_vendorlib}/Convert/BER/
%{perl_vendorlib}/Convert/BER.pm
%{perl_vendorlib}/Convert/BER.pod

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.3101-1
- Switch to upstream version.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.31.01-1
- Initial package. (using DAR)
