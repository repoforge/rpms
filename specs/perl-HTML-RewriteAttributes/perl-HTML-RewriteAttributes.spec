# $Id$
# Authority: shuff
# Upstream: Shawn M Moore <sartak$bestpractical,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-RewriteAttributes

Summary: concise attribute rewriting
Name: perl-HTML-RewriteAttributes
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-RewriteAttributes/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/HTML-RewriteAttributes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTML::Tagset)
BuildRequires: perl(URI)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(HTML::Entities)
Requires: perl(HTML::Parser)
Requires: perl(HTML::Tagset)
Requires: perl(URI)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

You simply specify a callback to run for each attribute and we do the rest for
you.

This module is designed to be subclassable to make handling special cases
easier. See the source for methods you can override.

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
%doc Changes META.yml SIGNATURE
%doc %{_mandir}/man?/*
%{perl_vendorlib}/HTML/RewriteAttributes.pm
%{perl_vendorlib}/HTML/RewriteAttributes/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jul 28 2010 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
