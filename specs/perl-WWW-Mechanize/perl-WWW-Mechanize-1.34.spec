# $Id$
# Authority: dries
# Upstream: Andy Lester <andy$petdance,com>
# ExclusiveDist: el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize

Summary: Handy web browsing in a Perl object
Name: perl-WWW-Mechanize
Version: 1.34
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize/

Source: http://backpan.perl.org/authors/id/P/PE/PETDANCE/WWW-Mechanize-1.34.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Carp)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HTML::Form) >= 1.038
BuildRequires: perl(HTML::HeadParser)
BuildRequires: perl(HTML::Parser) >= 3.33
BuildRequires: perl(HTML::TokeParser) >= 2.28
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(HTTP::Request) >= 1.3
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(LWP) >= 5.802
BuildRequires: perl(LWP::UserAgent) >= 2.024
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More) >= 0.34
BuildRequires: perl(URI) >= 1.25
BuildRequires: perl(URI::URL)
BuildRequires: perl(URI::file)
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(File::Temp)
Requires: perl(FindBin)
Requires: perl(Getopt::Long)
Requires: perl(HTML::Form) >= 1.038
Requires: perl(HTML::HeadParser)
Requires: perl(HTML::Parser) >= 3.33
Requires: perl(HTML::TokeParser) >= 2.28
Requires: perl(HTTP::Daemon)
Requires: perl(HTTP::Request) >= 1.3
Requires: perl(HTTP::Status)
Requires: perl(LWP) >= 5.802
Requires: perl(LWP::UserAgent) >= 2.024
Requires: perl(Pod::Usage)
Requires: perl(Test::More) >= 0.34
Requires: perl(Test::Warn) >= 0.11
Requires: perl(URI) >= 1.25
Requires: perl(URI::URL)
Requires: perl(URI::file)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
WWW::Mechanize, or Mech for short, is a Perl module for stateful programmatic
web browsing, used for automating interaction with websites.

Features include:

* All HTTP methods
* High-level hyperlink and HTML form support, without having to parse HTML
  yourself
* SSL support
* Automatic cookies
* Custom HTTP headers
* Automatic handling of redirections
* Proxies
* HTTP authentication

Mech supports performing a sequence of page fetches including following links
and submitting forms. Each fetched page is parsed and its links and forms are
extracted. A link or a form can be selected, form fields can be filled and the
next page can be fetched. Mech also stores a history of the URLs you've
visited, which can be queried and revisited.

%prep
%setup -n %{real_name}-%{version}

%build
echo "y" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --nolive
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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/*

%changelog
* Wed Jun 02 2010 Steve Huff <shuff@vecna.org> - 1.34-2
- This is the last version that can work on el5.
- Captured all deps from META.yml, prettied up.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.34-1
- Updated to release 1.34.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.32-1
- Updated to release 1.32.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Updated to release 1.30.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.

