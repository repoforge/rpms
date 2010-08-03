# $Id$
# Authority: shuff
# Upstream: Ian Langworth <ian$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-KwikiFormatish

Summary: convert Kwikitext into XML-compliant HTML
Name: perl-Text-KwikiFormatish
Version: 1.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-KwikiFormatish/

Source: http://search.cpan.org/CPAN/authors/id/I/IA/IAN/Text-KwikiFormatish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(CGI::Util)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(CGI::Util)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
CGI::Kwiki includes a formatter (CGI::Kwiki::Formatter) for converting
Kwikitext (a nice form of wikitext) to HTML. Unfortunately, it isn't easy to
use the formatter outside the CGI::Kwiki environment. Additionally, the HTML
produced by the formatter isn't XHTML-1 compliant. This module aims to fix both
of these issues and provide an interface similar to Text::WikiFormat.

Essentially, this module is the code from Brian Ingerson's
CGI::Kwiki::Formatter with a format subroutine, code relating to slides
removed, tweaked subroutinesa, and more.

Since the wikitext spec for input wikitext for this module differs a little
from the default Kwiki formatter, I thought it best to call it "Formatish"
instead of *the* Kwiki Format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README SIGNATURE
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Text/KwikiFormatish.pm
#%{perl_vendorlib}/Text/KwikiFormatish/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Aug 03 2010 Steve Huff <shuff@vecna.org> - 1.11-1
- Initial package.
