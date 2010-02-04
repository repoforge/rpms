# $Id$
# Authority: dries
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-MediaWiki

Summary: Converts HTML to MediaWiki markup
Name: perl-HTML-WikiConverter-MediaWiki
Version: 0.59
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-MediaWiki/

Source: http://search.cpan.org/CPAN/authors/id/D/DI/DIBERRI/HTML-WikiConverter-MediaWiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::WikiConverter) >= 0.63
BuildRequires: perl(Test::More)
BuildRequires: perl(URI) >= 1.35
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(HTML::WikiConverter) >= 0.63
Requires: perl(URI) >= 1.35

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::WikiConverter::MediaWiki adds the MediaWiki dialect to
HTML::WikiConverter allowing the conversion of HTML to MediaWiki
markup.

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
%dir %{perl_vendorlib}/HTML/WikiConverter/
%{perl_vendorlib}/HTML/WikiConverter/*

%changelog
* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 0.59-2
- Added missing dependencies.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.59-1
- Updated to version 0.59.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Initial package.
