# $Id$
# Authority: shuff
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter

Summary: Converts HTML to wiki markup
Name: perl-HTML-WikiConverter
Version: 0.68
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-WikiConverter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Data::Inheritable) >= 0.02
BuildRequires: perl(CSS) >= 1.07
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Element)
BuildRequires: perl(HTML::Entities) >= 1.27
BuildRequires: perl(HTML::Tagset) >= 3.04
BuildRequires: perl(HTML::Tree) >= 3.18
BuildRequires: perl(Params::Validate) >= 0.77
BuildRequires: perl(Pod::Usage) >= 1.16
BuildRequires: perl(Test::More)
BuildRequires: perl(URI) >= 1.35
BuildRequires: perl(URI::Escape)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Class::Data::Inheritable) >= 0.02
Requires: perl(CSS) >= 1.07
Requires: perl(Exporter)
Requires: perl(HTML::Element)
Requires: perl(HTML::Entities) >= 1.27
Requires: perl(HTML::Tagset) >= 3.04
Requires: perl(HTML::Tree) >= 3.18
Requires: perl(Params::Validate) >= 0.77
Requires: perl(Pod::Usage) >= 1.16
Requires: perl(URI) >= 1.35
Requires: perl(URI::Escape)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::WikiConverter is an HTML to wiki converter. It can convert HTML source
into a variety of wiki markups, called wiki "dialects". The following dialects
are supported:

  DokuWiki
  Kwiki
  MediaWiki
  MoinMoin
  Oddmuse
  PbWiki
  PhpWiki
  PmWiki
  SlipSlap
  TikiWiki
  UseMod
  WakkaWiki
  WikkaWiki

Note that while dialects usually produce satisfactory wiki markup, not all
features of all dialects are supported. Consult individual dialects'
documentation for details of supported features. Suggestions for improvements,
especially in the form of patches, are very much appreciated.

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
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/HTML/WikiConverter/
%{perl_vendorlib}/HTML/WikiConverter/*
%{perl_vendorlib}/HTML/WikiConverter.pm
%{_bindir}/*

%changelog
* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 0.68-1
- Initial package.
