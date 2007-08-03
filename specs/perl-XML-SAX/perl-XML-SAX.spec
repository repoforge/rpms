# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX

Summary: XML-SAX Perl module
Name: perl-XML-SAX
Version: 0.15
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-%{version}.tar.gz
Source1: ParserDetails.ini
#Patch0: perl-XML-SAX-parsers.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl(XML::NamespaceSupport)
Obsoletes: perl-XML-SAX-PurePerl <= 0.80, perl-XML-SAX-Base <= 1.04

Provides: perl(XML::SAX::PurePerl::DocType), perl(XML::SAX::PurePerl::DTDDecls)
Provides: perl(XML::SAX::PurePerl::EncodingDetect), perl(XML::SAX::PurePerl::NoUnicodeExt)
Provides: perl(XML::SAX::PurePerl::UnicodeExt), perl(XML::SAX::PurePerl::XMLDecl)

%description
XML-SAX Perl module.

%prep
%setup -n %{real_name}-%{version}
#patch

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/SAX.pm
%{perl_vendorlib}/XML/SAX/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.12-3
- Added missing provides. (Ville Skyttä)
- Obsoletes perl-XML-SAX-PurePerl and perl-XML-SAX-Base.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR)
