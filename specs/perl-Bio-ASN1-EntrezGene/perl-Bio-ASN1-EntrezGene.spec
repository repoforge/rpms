# $Id$
# Authority: dag
# Upstream: Mingyi Liu <mingyiliu$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bio-ASN1-EntrezGene
%define real_version 1.09

Summary: Perl module that implements a Parser for NCBI Entrez Gene
Name: perl-Bio-ASN1-EntrezGene
Version: 1.091
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bio-ASN1-EntrezGene/

Source: http://www.cpan.org/modules/by-module/Bio/Bio-ASN1-EntrezGene-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Bio-ASN1-EntrezGene is a Perl module that implements regular
expression-based Perl Parser for NCBI Entrez Gene. 

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes MANIFEST README README.1st examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Bio/
%dir %{perl_vendorlib}/Bio/ASN1/
%{perl_vendorlib}/Bio/ASN1/EntrezGene/
%{perl_vendorlib}/Bio/ASN1/EntrezGene.pm
%{perl_vendorlib}/Bio/ASN1/Sequence/
%{perl_vendorlib}/Bio/ASN1/Sequence.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.091-1
- Updated to release 1.091.

* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Initial package. (using DAR)
