# $Id$
# Authority: dries
# Upstream: Roderick Schertler <roderick$argon,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find

Summary: Perl module to find URIs in arbitrary text
Name: perl-URI-Find
Version: 20100505
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/URI-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Module::Build) >= 0.30
#BuildRequires: perl(Test::More) >= 0.82
BuildRequires: perl(Test::More)
BuildRequires: perl(URI) >= 1.00
BuildRequires: perl(URI::URL) >= 5.00
BuildRequires: perl >= v5.6.0
Requires: perl(URI) >= 1.00
Requires: perl(URI::URL) >= 5.00
Requires: perl >= v5.6.0

%filter_from_requires /^perl*/d
%filter_setup


%description
This module does one thing: Finds URIs and URLs in plain text. It finds them
quickly and it finds them all (or what URI::URL considers a URI to be.) It
only finds URIs which include a scheme (http:// or the like).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/URI::Find*
%doc %{_mandir}/man1/urifind.1*
%{_bindir}/urifind
%dir %{perl_vendorlib}/URI
%{perl_vendorlib}/URI/Find.pm
%{perl_vendorlib}/URI/Find/

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 20100505-1
- Updated to version 20100505.

* Mon Mar  8 2010 Christoph Maser <cmr@financial.com> - 20100211-1
- Updated to version 20100211.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 20090319-1
- Updated to version 20090319.

* Sat Sep 09 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.16-1
- initial packaging.
