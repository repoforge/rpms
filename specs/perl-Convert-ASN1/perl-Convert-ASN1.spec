# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-ASN1

Summary: Perl classes implementing conversion from/to ASN.1 data structures using BER/DER rules
Name: perl-Convert-ASN1
Version: 0.18
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-ASN1/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-ASN1-%{version}.tar.gz
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
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README SIGNATURE examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Convert/

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.18-0
- Updated to release 0.18.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
