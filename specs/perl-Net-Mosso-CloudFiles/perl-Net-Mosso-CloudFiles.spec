# $Id$
# Authority: shuff
# Upstream: Leon Brocard <acme$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Mosso-CloudFiles

Summary: Interface to Mosso CloudFiles service
Name: perl-%{real_name}
Version: 0.43
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Mosso-CloudFiles/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/Net-Mosso-CloudFiles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(Data::Stream::Bulk)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::MD5::File)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(JSON::XS::VersionOneAndTwo)
BuildRequires: perl(LWP)
BuildRequires: perl(LWP::ConnCache::MaxKeepAliveRequests)
BuildRequires: perl(LWP::UserAgent::Determined)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::StrictConstructor)
BuildRequires: perl(Test::Exception)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Crypt::SSLeay)
Requires: perl(Data::Stream::Bulk)
Requires: perl(Digest::MD5)
Requires: perl(Digest::MD5::File)
Requires: perl(File::Slurp)
Requires: perl(JSON::XS::VersionOneAndTwo)
Requires: perl(LWP)
Requires: perl(LWP::ConnCache::MaxKeepAliveRequests)
Requires: perl(LWP::UserAgent::Determined)
Requires: perl(Moose)
Requires: perl(MooseX::StrictConstructor)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides a simple interface to the Mosso Cloud Files service.
"Cloud Files is reliable, scalable and affordable web-based storage for backing
up and archiving all your static content". Find out more at

    http://www.mosso.com/cloudfiles.jsp.

To use this module you will need to sign up to Mosso Cloud Files and provide a
"user" and "key". If you use this module, you will incurr costs as specified by
Mosso. Please check the costs. If you use this module with your user and key
you will be responsible for these costs.

I highly recommend reading all about Cloud Files, but in a nutshell data is
stored in objects. Objects are referenced by names and objects are stored in
containers.

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/Mosso/
%{perl_vendorlib}/Net/Mosso/*

%changelog
* Thu Feb 25 2010 Steve Huff <shuff@vecna.org> - 0.43-1
- Initial package.
