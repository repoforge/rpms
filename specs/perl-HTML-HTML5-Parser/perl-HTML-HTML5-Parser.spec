# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name HTML-HTML5-Parser

Summary: parse HTML reliably
Name: perl-HTML-HTML5-Parser
Version: 0.102
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-HTML5-Parser/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/HTML-HTML5-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Error)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(HTML::Encoding) >= 0.55
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Signature) >= 0.66
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI)
BuildRequires: perl(XML::LibXML) >= 1.60
BuildRequires: perl >= v5.8.1
Requires: perl(Error)
Requires: perl(HTML::Encoding) >= 0.55
Requires: perl(LWP::UserAgent)
Requires: perl(XML::LibXML) >= 1.60
Requires: perl >= v5.8.1

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
%doc %{_mandir}/man3/HTML::HTML5::Parser.3pm*
%doc %{_mandir}/man3/HTML::HTML5::Parser::NamedEntityList.3pm*
%{_bindir}/html2xhtml
%dir %{perl_vendorlib}/
%{perl_vendorlib}/HTML/HTML5/Parser.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/DecodeHandle.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/Info.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/UnicodeChecker.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/UniversalCharDet.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/WebLatin1.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Charset/WebThai.pm
%{perl_vendorlib}/HTML/HTML5/Parser/NamedEntityList.pm
%{perl_vendorlib}/HTML/HTML5/Parser/TagSoupParser.pm
%{perl_vendorlib}/HTML/HTML5/Parser/Tokenizer.pm
%exclude %{perl_vendorarch}/auto/HTML/HTML5/Parser/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.102-1
- initial package
