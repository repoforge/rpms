# $Id$

# Authority: dag

%define real_name XML-LibXML

Summary: XML-LibXML Perl module
Name: perl-XML-LibXML
Version: 1.58
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/P/PH/PHISH/%{real_name}-%{version}.tar.gz
Patch: perl-XML-LibXML-parsers.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
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
