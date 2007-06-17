# $Id$
# Authority: dries
# Upstream: Stefan Zasada <sjz$zasada,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-CanonicalizeXML

Summary: Wrapper to canonicalization functions
Name: perl-XML-CanonicalizeXML
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-CanonicalizeXML/

Source: http://search.cpan.org/CPAN/authors/id/S/SJ/SJZASADA/XML-CanonicalizeXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), libxml2-devel

%description
This module provides a wrapper to the XML Canonicalization functions
provided by libxml2 (http://www.xmlsoft.org/) to give Perl support to
the the W3C defined algorithms c14n canonicalization
(http://www.w3.org/TR/2001/REC-xml-c14n-20010315) and c14n exclusive
canonicalization (http://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/)

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/XML/CanonicalizeXML.pm
%{perl_vendorarch}/auto/XML/CanonicalizeXML/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
