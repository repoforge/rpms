# $Id$
# Authority: dag

%define real_name Convert-BER
%define real_version 1.3101

Summary: ASN.1 Basic Encoding Rules perl module
Name: perl-Convert-BER
Version: 1.31.01
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BER/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-BER-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.32.01-1
- Initial package. (using DAR)
