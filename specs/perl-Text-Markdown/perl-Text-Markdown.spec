# $Id$
# Authority: shuff
# Upstream: Thomas Doran <bobtfish$bobtfish,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Markdown

Summary: Convert Markdown syntax to (X)HTML
Name: perl-%{real_name}
Version: 1.000031
Release: 1%{?dist}
License: BSD
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Markdown/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Text-Markdown-%{version}.tar.gz
Patch0: %{name}_Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(FindBin)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Text::Balanced)
BuildRequires: perl >= v5.8.0
Requires: perl(Digest::MD5)
Requires: perl(Encode)
Requires: perl(Text::Balanced)
Requires: perl >= v5.8.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

# we are a Markdown compiler
Provides: Markdown
Provides: %{_bindir}/Markdown.pl

Conflicts: perl(Text::MultiMarkdown) < 1.0.26

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format is most
similar to that of plain text email, and supports features such as headers,
*emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use span-level HTML
tags anywhere in a Markdown document, and you can use block level HTML tags
(like <div> and <table> as well).

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 script/Markdown.pl %{buildroot}%{_bindir}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes License.text MANIFEST README Readme.text Todo
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/*
%{_bindir}/*

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.000031-1
- Updated to version 1.000031.

* Wed Mar 10 2010 Steve Huff <shuff@vecna.org> - 1.000030-1
- Initial package.
