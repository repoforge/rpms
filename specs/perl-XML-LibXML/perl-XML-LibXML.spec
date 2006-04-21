# $Id$
# Authority: dag

# ExcludeDist: el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXML

Summary: XML-LibXML Perl module
Name: perl-XML-LibXML
Version: 1.58
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXML-%{version}.tar.gz
Patch: perl-XML-LibXML-1.58-parsers.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, libxml2-devel >= 2.4.20
BuildRequires: perl(XML::LibXML::Common), perl(XML::NamespaceSupport), perl(XML::SAX)

Requires: perl >= 0:5.8.0

%description
XML-LibXML Perl module.

%prep
%setup -n %{real_name}-%{version}
%patch

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/XML/
%{perl_vendorarch}/auto/XML/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.58-1.2
- Rebuild for Fedora Core 5.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 1.58-1
- Changed to binary package, removed noarch.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.58-0
- Updated to release 1.58.

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 1.56-0
- Updated to release 1.56.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.55-0
- Fixed site -> vendor. (Matthew Mastracci)
- Updated to release 1.55.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.54-0
- Updated to release 1.54.
- Initial package. (using DAR)
