# $Id$
# Authority: dag
# Upstream: Alberto Reggiori <areggiori$webweaving,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RDFStore

Summary: Perl module to store and query RDF graphs
Name: perl-RDFStore
Version: 0.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDFStore/

Source: http://www.cpan.org/authors/id/A/AR/AREGGIORI/RDFStore-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-RDFStore is a Perl module to store and query RDF graphs.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES INSTALL LICENSE README TODO VERSION sfl-license.txt doc/ samples/
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/rdf.pl
%{_bindir}/rdfdump.pl
%{_bindir}/rdfquery.pl
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/RDFStore.pm
%{perl_vendorarch}/DBMS.pm
%{perl_vendorarch}/RDFStore/
%{perl_vendorarch}/RDFStore.pm
%dir %{perl_vendorarch}/RDQL/
%{perl_vendorarch}/RDQL/Parser.pm
%dir %{perl_vendorarch}/Util/
%{perl_vendorarch}/Util/BLOB.pm
%{perl_vendorarch}/auto/DBMS/
%{perl_vendorarch}/auto/RDFStore/

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.51-1
- Initial package. (using DAR)
