# $Id$
# Authority: shuff
# Upstream: Marc Mims <marc$questright,com>
# ExcludeDist: el3 el4
# Rationale: versions > 3.05002 require perl(URI) >= 1.40, RHEL5 bundles 1.35

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Twitter

Summary: A perl interface to the Twitter API
Name: perl-%{real_name}
Version: 3.05002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Twitter/

Source: http://search.cpan.org/CPAN/authors/id/M/MM/MMIMS/Net-Twitter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.8.1
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Visitor::Callback)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(JSON::Any) >= 1.21
BuildRequires: perl(LWP::UserAgent) >= 2.032
BuildRequires: perl(Moose) >= 0.85
BuildRequires: perl(Moose::Exporter)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(MooseX::MultiInitArg)
BuildRequires: perl(Net::Netrc)
BuildRequires: perl(Net::OAuth) >= 0.16
BuildRequires: perl(Scalar::Util) >= 0.16
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(namespace::autoclean)
Requires: perl >= 5.8.1
Requires: perl(Data::Visitor::Callback)
Requires: perl(DateTime)
Requires: perl(DateTime::Format::Strptime)
Requires: perl(Digest::SHA)
Requires: perl(HTML::Entities)
Requires: perl(HTTP::Request::Common)
Requires: perl(JSON::Any) >= 1.21
Requires: perl(LWP::UserAgent) >= 2.032
Requires: perl(Moose) >= 0.85
Requires: perl(Moose::Exporter)
Requires: perl(Moose::Role)
Requires: perl(MooseX::AttributeHelpers)
Requires: perl(MooseX::MultiInitArg)
Requires: perl(Net::Netrc)
Requires: perl(Net::OAuth) >= 0.16
Requires: perl(Scalar::Util) >= 0.16
Requires: perl(URI)
Requires: perl(URI::Escape)
Requires: perl(namespace::autoclean)

# manage perl dependencies manually
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a perl interface to the Twitter APIs. See
http://apiwiki.twitter.com/Twitter-API-Documentation for a full description of
the Twitter APIs.

OMG! THE MOOSE!

Net::Twitter is Moose based. Moose provides some advantages, including the
ability for the maintainer of this module to respond quickly to Twitter API
changes.

See Net::Twitter::Lite if you need an alternative without Moose and its
dependencies.

Net::Twitter::Lite's API method definitions and documentation are generated
from Net::Twitter. It is a related module, but does not depend on Net::Twitter
or Moose for installation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/Identica.pm
%{perl_vendorlib}/Net/Twitter
%{perl_vendorlib}/Net/Twitter.pm
%{perl_vendorlib}/Net/Twitter.pod

%changelog
* Wed Dec 23 2009 Steve Huff <shuff@vecna.org> - 3.05002-1
- Initial package.
