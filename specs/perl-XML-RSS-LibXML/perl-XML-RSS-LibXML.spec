# $Id$
# Authority: dag
# Upstream: -2007 Daisuke Maki <dmaki@cpan.org>, Tatsuhiko Miyagawa <miyagawa@bulknews.net>. All rights reserved.

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSS-LibXML

Summary: XML::RSS with XML::LibXML
Name: perl-XML-RSS-LibXML
Version: 0.3100
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-LibXML/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/XML-RSS-LibXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(XML::LibXML) >= 1.66
BuildRequires: perl(XML::LibXML::XPathContext)
Requires: perl(Class::Accessor::Fast)
Requires: perl(DateTime::Format::Mail)
Requires: perl(DateTime::Format::W3CDTF)
Requires: perl(Encode)
Requires: perl(UNIVERSAL::require)
Requires: perl(XML::LibXML) >= 1.66
Requires: perl(XML::LibXML::XPathContext)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
XML::RSS with XML::LibXML.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/XML::RSS::LibXML*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/RSS/
%{perl_vendorlib}/XML/RSS/LibXML/
%{perl_vendorlib}/XML/RSS/LibXML.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.3100-1
- Updated to version 0.3100.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.3004-1
- Updated to version 0.3004.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.3002-1
- Initial package. (using DAR)
