# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr$cpan,org>

# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-ASN1

Summary: Convert between perl data structures and ASN.1 encoded packets
Name: perl-Convert-ASN1
Version: 0.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-ASN1/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-ASN1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.005

Obsoletes: perl-convert-asn1

%description
Convert-ASN1 is a set of Perl classes implementing conversion routines for
encoding and decoding ASN.1 data structures using BER/DER rules.

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
%doc ChangeLog MANIFEST META.yml README SIGNATURE examples/
%doc %{_mandir}/man3/Convert::ASN1.3pm*
%doc %{perl_vendorlib}/Convert/ASN1/
%{perl_vendorlib}/Convert/ASN1/
%{perl_vendorlib}/Convert/ASN1.pm
%{perl_vendorlib}/Convert/ASN1.pod

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.21-2
- Disabled auto-requires for examples/.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.18-0
- Updated to release 0.18.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
