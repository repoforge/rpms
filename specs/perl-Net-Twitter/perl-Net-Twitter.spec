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
Version: 3.10003
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Twitter/

Source: http://search.cpan.org/CPAN/authors/id/M/MM/MMIMS/Net-Twitter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Data::Visitor::Callback)
BuildRequires: perl(DateTime) >= 0.51
BuildRequires: perl(DateTime::Format::Strptime) >= 1.09
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Encode)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(JSON::Any) >= 1.21
BuildRequires: perl(JSON::XS)
BuildRequires: perl(LWP::UserAgent) >= 2.032
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose) >= 0.85
BuildRequires: perl(Moose::Exporter)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(MooseX::MultiInitArg)
BuildRequires: perl(Net::Netrc)
BuildRequires: perl(Net::OAuth) >= 0.2
BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(URI) >= 1.4
BuildRequires: perl(URI::Escape)
BuildRequires: perl(namespace::autoclean) >= 0.09
BuildRequires: perl >= 5.8.1
Requires: perl(Carp)
Requires: perl(Data::Visitor::Callback)
Requires: perl(DateTime) >= 0.51
Requires: perl(DateTime::Format::Strptime) >= 1.09
Requires: perl(Digest::SHA)
Requires: perl(Encode)
Requires: perl(HTML::Entities)
Requires: perl(HTTP::Request::Common)
Requires: perl(JSON::Any) >= 1.21
Requires: perl(JSON::XS)
Requires: perl(LWP::UserAgent) >= 2.032
Requires: perl(List::Util)
Requires: perl(Moose) >= 0.85
Requires: perl(Moose::Exporter)
Requires: perl(Moose::Role)
Requires: perl(MooseX::AttributeHelpers)
Requires: perl(MooseX::MultiInitArg)
Requires: perl(Net::Netrc)
Requires: perl(Net::OAuth) >= 0.2
Requires: perl(Scalar::Util)
Requires: perl(Try::Tiny)
Requires: perl(URI) >= 1.4
Requires: perl(URI::Escape)
Requires: perl(namespace::autoclean) >= 0.09
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 3.10003-1
- Updated to version 3.10003.

* Wed Dec 23 2009 Steve Huff <shuff@vecna.org> - 3.05002-1
- Initial package.
