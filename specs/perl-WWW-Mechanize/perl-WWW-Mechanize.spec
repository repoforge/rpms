# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize

Summary: Handy web browsing in a Perl object
Name: perl-WWW-Mechanize
Version: 1.68
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Manifest)
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
BuildRequires: perl(HTTP::Server::Simple) >= 0.35
BuildRequires: perl(HTTP::Server::Simple::CGI)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::Socket::SSL)
#BuildRequires: perl(LWP) >= 5.829
BuildRequires: perl(LWP)
#BuildRequires: perl(LWP::UserAgent) >= 5.829
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More) >= 0.34
BuildRequires: perl(Test::Warn) >= 0.11
#BuildRequires: perl(URI) >= 1.36
BuildRequires: perl(URI)
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
Requires: perl(HTTP::Server::Simple) >= 0.35
Requires: perl(HTTP::Server::Simple::CGI)
Requires: perl(HTTP::Status)
Requires: perl(IO::Socket::SSL)
#Requires: perl(LWP) >= 5.829
Requires: perl(LWP)
#Requires: perl(LWP::UserAgent) >= 5.829
Requires: perl(LWP::UserAgent)
Requires: perl(Pod::Usage)
Requires: perl(Test::More) >= 0.34
Requires: perl(Test::Warn) >= 0.11
#Requires: perl(URI) >= 1.36
Requires: perl(URI)
Requires: perl(URI::URL)
Requires: perl(URI::file)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
Handy web browsing in a Perl object.

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
%doc %{_mandir}/man1/mech-dump.1*
%doc %{_mandir}/man3/WWW::Mechanize.3pm*
%doc %{_mandir}/man3/WWW::Mechanize::*.3pm*
%{_bindir}/mech-dump
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Mechanize/
%{perl_vendorlib}/WWW/Mechanize.pm

%changelog
* Mon Jun 11 2012 Olivier Bilodeau <obilodeau@inverse.ca> - 1.68-1
- Updated to version 1.68.

* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 1.66-1
- Updated to version 1.66.

* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 1.62-1
- Updated to version 1.62.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.60-1
- Updated to version 1.60.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.58-1
- Updated to version 1.58.
- Switch to manual dependencies

* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 1.56-1
- Updated to version 1.56.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.54-1
- Updated to version 1.54.

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

