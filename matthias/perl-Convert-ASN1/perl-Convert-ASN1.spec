# Authority: dag

%define rname Convert-ASN1

Summary: A set of Perl classes implementing conversion from/to ASN.1 data structures using BER/DER rules.
Name: perl-Convert-ASN1
Version: 0.17
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-ASN1/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/G/GB/GBARR/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

Obsoletes: perl-convert-asn1

%description
Convert-ASN1 is a set of Perl classes implementing conversion routines for
encoding and decoding ASN.1 data structures using BER/DER rules.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README examples/
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
