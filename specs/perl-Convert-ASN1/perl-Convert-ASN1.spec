# $Id$

# Authority: dag

%define real_name Convert-ASN1

Summary: set of Perl classes implementing conversion from/to ASN.1 data structures using BER/DER rules
Name: perl-Convert-ASN1
Version: 0.18
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-ASN1/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/G/GB/GBARR/Convert-ASN1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

Obsoletes: perl-convert-asn1

%description
Convert-ASN1 is a set of Perl classes implementing conversion routines for
encoding and decoding ASN.1 data structures using BER/DER rules.

%prep
%setup -n %{real_name}-%{version} 

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
%doc ChangeLog MANIFEST README SIGNATURE examples/
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.18-0
- Updated to release 0.18.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
