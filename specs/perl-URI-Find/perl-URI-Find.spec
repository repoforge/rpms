# $Id$
# Authority: dries
# Upstream: Roderick Schertler <roderick$argon,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find

Summary: Perl module to find URIs in arbitrary text
Name: perl-URI-Find
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/URI-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(URI), perl(URI::URL), perl(ExtUtils::MakeMaker)

%description
This module does one thing: Finds URIs and URLs in plain text. It finds them
quickly and it finds them all (or what URI::URL considers a URI to be.) It
only finds URIs which include a scheme (http:// or the like).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

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
* Sat Sep 09 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.16-1
- initial packaging.
