# $Id$
# Authority: shuff
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-Markdown

Summary: Converts HTML to Markdown markup
Name: perl-HTML-WikiConverter-Markdown
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-Markdown/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-WikiConverter-Markdown-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Tagset)
BuildRequires: perl(HTML::WikiConverter) >= 0.67
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
Requires: perl(HTML::WikiConverter) >= 0.67

%description
HTML::WikiConverter::Markdown adds the Markdown dialect to
HTML::WikiConverter allowing the conversion of HTML to Markdown
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
* Thu Feb 04 2010 Steve Huff <shuff@vecna.org> - 0.05-1
- Initial package.
