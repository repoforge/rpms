# $Id$
# Authority: shuff
# Upstream: John Beppu <beppu$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

### perl-AnyEvent-HTTP is rfx on EL5
%{?el5:# Tag: rfx}

%define real_name AnyEvent-CouchDB

Summary: a non-blocking CouchDB client based on jquery.couch.js
Name: perl-AnyEvent-CouchDB
Version: 1.25
Release: 1%{?dist}
License: MIT
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyEvent-CouchDB/

Source: http://search.cpan.org/CPAN/authors/id/B/BE/BEPPU/AnyEvent-CouchDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(AnyEvent::HTTP) >= 1.11
BuildRequires: perl(CouchDB::View)
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::All)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Scope::Guard)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(AnyEvent::HTTP) >= 1.11
Requires: perl(CouchDB::View)
Requires: perl(Data::Dump::Streamer)
Requires: perl(Exception::Class)
Requires: perl(IO::All)
Requires: perl(JSON::XS)
Requires: perl(Scope::Guard)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
AnyEvent::CouchDB is a non-blocking CouchDB client implemented on top of the
AnyEvent  framework. Using this library will give you the ability to run many
CouchDB requests asynchronously, and it was intended to be used within a
Coro+AnyEvent environment. However, it can also be used synchronously if you
want.

Its API is based on jquery.couch.js, but we've adapted the API slightly so that
it makes sense in an asynchronous Perl environment.

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
%doc Changes META.json README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/AnyEvent/CouchDB.pm
%{perl_vendorlib}/AnyEvent/CouchDB/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Aug 01 2011 Steve Huff <shuff@vecna.org> - 1.25-1
- Updated to version 1.25.
- RFX on el5 due to dependency on perl-AnyEvent-HTTP.

* Fri Sep 24 2010 Steve Huff <shuff@vecna.org> - 1.21-1
- Initial package.
