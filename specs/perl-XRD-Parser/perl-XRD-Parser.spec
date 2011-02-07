# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name XRD-Parser

Summary: parse XRD and host-meta files into RDF::Trine models
Name: perl-XRD-Parser
Version: 0.101
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XRD-Parser/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/XRD-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(HTTP::Link::Parser) >= 0.03
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(RDF::Trine)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl >= v5.8.0
Requires: perl(HTTP::Link::Parser) >= 0.03
Requires: perl(LWP::UserAgent)
Requires: perl(RDF::Trine)
Requires: perl(Scalar::Util)
Requires: perl(URI)
Requires: perl(URI::Escape)
Requires: perl(XML::LibXML)
Requires: perl >= v5.8.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/XRD::Parser.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/XRD/Parser.pm
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.101-1
- initial package
