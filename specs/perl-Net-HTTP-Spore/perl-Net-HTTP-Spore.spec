# $Id$
# Authority: shuff
# Upstream: Franck Cuny <franck$lumberjaph,net>
# Tag: test

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-HTTP-Spore

Summary: SPORE client for Perl
Name: perl-Net-HTTP-Spore
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-HTTP-Spore/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRANCKC/Net-HTTP-Spore-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(IO::All)
BuildRequires: perl(JSON)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Exporter)
BuildRequires: perl(Moose::Meta::Method)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::MetaRole)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(MooseX::Types::URI)
BuildRequires: perl(Net::OAuth)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(YAML)
BuildRequires: perl(overload)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(HTTP::Headers)
Requires: perl(HTTP::Request)
Requires: perl(IO::All)
Requires: perl(JSON)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Moose)
Requires: perl(Moose::Exporter)
Requires: perl(Moose::Meta::Method)
Requires: perl(Moose::Role)
Requires: perl(Moose::Util::MetaRole)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::Types::Moose)
Requires: perl(MooseX::Types::URI)
Requires: perl(Net::OAuth)
Requires: perl(Scalar::Util)
Requires: perl(Time::HiRes)
Requires: perl(Try::Tiny)
Requires: perl(URI)
Requires: perl(URI::Escape)
Requires: perl(XML::Simple)
Requires: perl(YAML)
Requires: perl(overload)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is an implementation of the SPORE specification. To use this
client, you need to use or to write a SPORE specification of an API. Some
specifications are available at http://github.com/SPORE/api-description.

%prep
%setup -n %{real_name}-%{version}

%build
# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.yml META.json README eg/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/HTTP/Spore.pm
%{perl_vendorlib}/Net/HTTP/Spore/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Feb 24 2011 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
