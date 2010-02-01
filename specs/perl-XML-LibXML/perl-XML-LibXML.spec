# $Id$
# Authority: dag
# Upstream: Petr Pajas <pajas$matfyz,cz>

### EL4 and EL5 ship with perl-XML-LibXML 1.58
# but we should still provide this as an option for perl-Image-Info

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXML

Summary: Interface to Gnome libxml2 xml parsing and DOM library
Name: perl-XML-LibXML
Version: 1.70
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML/

Source: http://search.cpan.org/CPAN/authors/id/P/PA/PAJAS/XML-LibXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: libxml2-devel >= 2.4.20
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::NamespaceSupport) >= 1.07
BuildRequires: perl(XML::SAX) >= 0.11
Requires: perl(XML::NamespaceSupport) >= 1.07
Requires: perl(XML::SAX) >= 0.11
Requires: perl >= 2:5.8.0
Provides: perl-Image-Info-alternative = 1.30

Obsoletes: perl-XML-LibXML-Common

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-XML-LibXML is a Perl module that implements binding for libxml2.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
	SKIP_SAX_INSTALL=1
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find docs/ example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README docs/ example/
%doc %{_mandir}/man3/XML::LibXML.3pm*
%doc %{_mandir}/man3/XML::LibXML::*.3pm*
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/LibXML/
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/LibXML/
%{perl_vendorarch}/XML/LibXML.pm
%{perl_vendorarch}/XML/LibXML.pod

%changelog
* Mon Feb 01 2010 Steve Huff <shuff@vecna.org> - 
- This version obsoletes the upstream perl-XML-LibXML-Common package.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 1.70-2
- Update perl-Image-Info-alternative provides

* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 1.70-1
- Updated to version 1.70.

* Thu Sep 10 2009 Steve Huff <shuff_@_hmdc.harvard.edu> - 1.69-2
- This provides perl-Image-Info-alternative = 1.29.

* Tue May 26 2008 Christoph Maser <cmr@financial.com> - 1.69-1
- Updated to release 1.69.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.66-1
- Updated to release 1.66.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.65-1
- Updated to release 1.65.

* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 1.63-1
- Updated to release 1.63.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 1.58-1
- Changed to binary package, removed noarch.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.58-0
- Updated to release 1.58.

* Thu Nov 20 2003 Dag Wieers <dag@wieers.com> - 1.56-0
- Updated to release 1.56.

- Fixed site -> vendor. (Matthew Mastracci)
- Updated to release 1.55.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 1.54-0
- Updated to release 1.54.
- Initial package. (using DAR)
