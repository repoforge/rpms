# $Id$
# Authority: shuff
# Upstream: Franck Cuny <franck$lumberjaph,net>
# ExcludeDist: el4 el5
# Rationale: needs Perl 5.10

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-HTTP-API

Summary: Easily create clients for web APIs
Name: perl-Net-HTTP-API
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-HTTP-API/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRANCKC/Net-HTTP-API-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.10.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(JSON)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Exporter)
BuildRequires: perl(Moose::Meta::Method)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::MetaRole)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(MooseX::Types::URI)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(overload)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.10.0
Requires: perl(HTTP::Request)
Requires: perl(JSON)
Requires: perl(LWP::UserAgent)
Requires: perl(Moose)
Requires: perl(Moose::Exporter)
Requires: perl(Moose::Meta::Method)
Requires: perl(Moose::Role)
Requires: perl(Moose::Util::MetaRole)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::Types::Moose)
Requires: perl(MooseX::Types::URI)
Requires: perl(Try::Tiny)
Requires: perl(XML::Simple)
Requires: perl(YAML::Syck)
Requires: perl(overload)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Net::HTTP::API is a module to help to easily create a client for a web API.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/HTTP/API.pm
%{perl_vendorlib}/Net/HTTP/API/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Feb 25 2011 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
