# $Id$
# Authority: shuff
# Upstream: Cal Henderson <cal$iamcal,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Parser-Lite-Tree-XPath

Summary: XPath access to XML::Parser::Lite::Tree structures
Name: perl-XML-Parser-Lite-Tree-XPath
Version: 0.24
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Parser-Lite-Tree-XPath/

Source: http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/XML-Parser-Lite-Tree-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Parser::Lite::Tree) >= 0.11
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.6
Requires: perl(XML::Parser::Lite::Tree) >= 0.11

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This pure-Perl implementation of XPath is a complement to
XML::Parser::Lite::Tree, a pure-Perl XML tree parser and builder. It aims to
implement 100% of the W3C XPath specification.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/Parser/Lite/Tree/XPath.pm
%{perl_vendorlib}/XML/Parser/Lite/Tree/XPath/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/*/*/.packlist

%changelog
* Mon Jun 20 2011 Steve Huff <shuff@vecna.org> - 0.24-1
- Initial package.
