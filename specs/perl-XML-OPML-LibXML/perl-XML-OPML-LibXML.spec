# $Id$
# Authority: shuff
# Upstream: Tatsuhiko Miyagawa <miyakawa$bulknews,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-OPML-LibXML

Summary: Parse OPML documents with LibXML
Name: perl-XML-OPML-LibXML
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-OPML-LibXML/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/XML-OPML-LibXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::LibXML) >= 1.60
BuildRequires: rpm-macros-rpmforge

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
XML::OPML::LibXML is an OPML parser written using XML::LibXML. This module is
part of spin-off CPANization of Plagger plugins.

For now, all this module does is just parsing an OPML document. The API is very
simple and limited to low-level access, yet.

NOTE: This module is not designed to be a drop-in replacement of XML::OPML.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

# fix benchmark.pl
%{__perl} -pi -e 's|/t||;' eg/benchmark.pl

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
%doc Changes META.yml README eg/ t/samples
%doc %{_mandir}/man?/*
%{perl_vendorlib}/XML/OPML/LibXML.pm
%{perl_vendorlib}/XML/OPML/LibXML/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Mon Aug 29 2011 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial package.
