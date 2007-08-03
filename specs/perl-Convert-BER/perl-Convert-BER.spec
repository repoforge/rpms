# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-BER
%define real_version 1.3101

Summary: ASN.1 Basic Encoding Rules perl module
Name: perl-Convert-BER
Version: 1.31.01
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BER/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-BER-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
ASN.1 Basic Encoding Rules perl module.

%prep
%setup -n %{real_name}-%{real_version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Convert/BER.p*

%changelog
* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 1.32.01-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.32.01-1
- Initial package. (using DAR)
