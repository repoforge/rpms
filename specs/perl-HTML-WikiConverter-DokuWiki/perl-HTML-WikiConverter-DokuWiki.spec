# $Id$
# Authority: shuff
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-DokuWiki

Summary: Converts HTML to DokuWiki markup
Name: perl-HTML-WikiConverter-DokuWiki
Version: 0.53
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-DokuWiki/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-WikiConverter-DokuWiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::WikiConverter) >= 0.53
Requires: perl(HTML::WikiConverter) >= 0.53

%description
HTML::WikiConverter::DokuWiki adds the DokuWiki dialect to
HTML::WikiConverter allowing the conversion of HTML to DokuWiki
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
* Fri Feb 05 2010 Steve Huff <shuff@vecna.org> - 0.53-1
- Initial package.
