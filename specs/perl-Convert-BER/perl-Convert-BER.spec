# $Id: perl-Archive-Tar.spec 120 2004-03-15 17:26:20Z dag $

# Authority: dag

%define rname Convert-BER
%define rversion 1.3101

Summary: ASN.1 Basic Encoding Rules perl module.
Name: perl-Convert-BER
Version: 1.31.01
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-BER/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Convert-BER-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
ASN.1 Basic Encoding Rules perl module.

%prep
%setup -n %{rname}-%{rversion} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

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
