# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name HTML-HTML5-Sanity

Summary: make HTML5 DOM trees less insane
Name: perl-HTML-HTML5-Sanity
Version: 0.101
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-HTML5-Sanity/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/HTML-HTML5-Sanity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Digest::SHA)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Locale::Country) >= 1.06
BuildRequires: perl(Module::Signature) >= 0.66
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(XML::LibXML) >= 1.60
BuildRequires: perl(XML::LibXML::Debugging)
BuildRequires: perl >= v5.8.0
Requires: perl(Locale::Country) >= 1.06
Requires: perl(XML::LibXML) >= 1.60
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
%doc %{_mandir}/man3/HTML::HTML5::Sanity.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/HTML/HTML5/Sanity.pm
%exclude %{perl_vendorarch}/auto/HTML/HTML5/Sanity/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.101-1
- initial package
