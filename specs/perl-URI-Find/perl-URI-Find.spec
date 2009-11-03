# $Id$
# Authority: dries
# Upstream: Roderick Schertler <roderick$argon,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find

Summary: Perl module to find URIs in arbitrary text
Name: perl-URI-Find
Version: 20090319
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find/

Source: http://www.cpan.org/modules/by-module/URI/URI-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(URI)
BuildRequires: perl(URI::URL)

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
%dir %{perl_vendorlib}/URI
%{perl_vendorlib}/URI/Find.pm
%{perl_vendorlib}/URI/Find/

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 20090319-1
- Updated to version 20090319.

* Sat Sep 09 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.16-1
- initial packaging.
