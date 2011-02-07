# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name XML-LibXML-Debugging

Summary: get debugging information from XML::LibXML nodes
Name: perl-XML-LibXML-Debugging
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML-Debugging/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/XML-LibXML-Debugging-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Entities) >= 3.27
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(XML::LibXML)
BuildRequires: perl >= v5.8.0
Requires: perl(HTML::Entities) >= 3.27
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
%doc %{_mandir}/man3/XML::LibXML::Debugging.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/XML/LibXML/Debugging.pm
%exclude %{perl_vendorarch}/auto/XML/LibXML/Debugging/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.04-1
- initial package
