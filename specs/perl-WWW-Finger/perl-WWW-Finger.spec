# $Id$
# Authority: shuff
# Upstream: Toby Inkster <tonyink$cpan,org>
# Test

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Finger

Summary: Get useful data from e-mail addresses
Name: perl-%{real_name}
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Finger/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/WWW-Finger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.8.1
BuildRequires: perl(Carp) >= 1.00
BuildRequires: perl(Digest::MD5) >= 2.00
BuildRequires: perl(Digest::SHA1) >= 2.00
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HTTP::Link::Parser) >= 0.03
BuildRequires: perl(JSON) >= 2.00
BuildRequires: perl(LWP::Simple) >= 5.00
BuildRequires: perl(LWP::UserAgent) >= 5.00
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(RDF::Query) >= 2.200
BuildRequires: perl(RDF::Query::Client) >= 0.02
BuildRequires: perl(RDF::Trine) >= 0.112
BuildRequires: perl(URI) >= 1.30
BuildRequires: perl(XML::LibXML) >= 1.60
BuildRequires: perl(XRD::Parser) >= 0.04
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Carp) >= 1.00
Requires: perl(Digest::MD5) >= 2.00
Requires: perl(Digest::SHA1) >= 2.00
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Getopt::Long)
Requires: perl(HTTP::Link::Parser) >= 0.03
Requires: perl(JSON) >= 2.00
Requires: perl(LWP::Simple) >= 5.00
Requires: perl(LWP::UserAgent) >= 5.00
Requires: perl(Pod::Usage)
Requires: perl(RDF::Query) >= 2.200
Requires: perl(RDF::Query::Client) >= 0.02
Requires: perl(RDF::Trine) >= 0.112
Requires: perl(URI) >= 1.30
Requires: perl(XML::LibXML) >= 1.60
Requires: perl(XRD::Parser) >= 0.04


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is not an implementation of the finger protocol (RFC 1288). Use
Net::Finger for that. Instead it is a set of implementations of other methods
for getting information from an e-mail address, or e-mail-like identifier. This
package includes four such implementations, and it's pretty easy to create your
own additional implementations:

    * WebFinger
    * Fingerpoint
    * cpan.org scraper (for user@cpan.org)
    * Unnamed finger protocol described on bitworking.org

Only the first two implementations are enabled by default. See
"IMPLEMENTATIONS" on how to enable others, and for more details.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/*
%{_bindir}/*

%changelog
* Fri Feb 12 2010 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
