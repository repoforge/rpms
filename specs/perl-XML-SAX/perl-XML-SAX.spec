# $Id$
# Authority: dag

# ExcludeDist: el4

%define real_name XML-SAX

Summary: XML-SAX Perl module
Name: perl-XML-SAX
Version: 0.13
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-SAX/

Source: http://www.cpan.org/modules/by-module/XML/XML-SAX-%{version}.tar.gz
Source1: ParserDetails.ini
Patch0: perl-XML-SAX-parsers.patch
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
%patch

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.12-3
- Added missing provides. (Ville Skyttä)
- Obsoletes perl-XML-SAX-PurePerl and perl-XML-SAX-Base.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR) 
