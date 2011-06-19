# $Id$
# Authority: shuff
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Server-Simple-PSGI

Summary: PSGI handler for HTTP::Server::Simple
Name: perl-HTTP-Server-Simple-PSGI
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Server-Simple-PSGI/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/HTTP-Server-Simple-PSGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Server::Simple) >= 0.42
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(HTTP::Server::Simple) >= 0.42

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTTP::Server::Simple::PSGI is a HTTP::Server::Simple based HTTP server that can run PSGI applications. This module only depends on HTTP::Server::Simple, which itself doesn't depend on any non-core modules so it's best to be used as an embedded web server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/HTTP/Server/Simple/PSGI.pm
#%{perl_vendorlib}/HTTP/Server/Simple/PSGI/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/*/.packlist

%changelog
* Thu May 05 2011 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
