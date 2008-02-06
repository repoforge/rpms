# $Id$
# Authority: dag
# Upstream: Grant McLean <grantm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-SAX

Summary: Perl module that implements a simple API for XML
Name: perl-XML-SAX
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-%{version}.tar.gz
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
perl-XML-SAX is a Perl module that implements a simple API for XML.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >ParserDetails.ini
[XML::SAX::PurePerl]
http://xml.org/sax/features/namespaces = 1

[XML::LibXML::SAX::Parser]
http://xml.org/sax/features/namespaces = 1

[XML::LibXML::SAX]
http://xml.org/sax/features/namespaces = 1
EOF

%build
echo "N" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

#%{__install} -Dp -m0644 ParserDetails.ini %{buildroot}%{perl_vendorlib}/XML/SAX/ParserDetails.ini

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/XML::SAX.3pm*
%doc %{_mandir}/man3/XML::SAX*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.12-3
- Added missing provides. (Ville Skyttä)
- Obsoletes perl-XML-SAX-PurePerl and perl-XML-SAX-Base.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR)
