# $Id$
# Authority: shuff
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-PmWiki

Summary: Converts HTML to PmWiki markup
Name: perl-HTML-WikiConverter-PmWiki
Version: 0.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-PmWiki/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-WikiConverter-PmWiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::WikiConverter)
Requires: perl(HTML::WikiConverter)

%description
HTML::WikiConverter::PmWiki adds the PmWiki dialect to
HTML::WikiConverter allowing the conversion of HTML to PmWiki
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
* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 0.51-1
- Initial package.
