# $Id$
# Authority: shuff
# Upstream: Jeff Kim <dohyun$hollow,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Amazon-EC2

Summary: Perl interface to the Amazon Elastic Compute Cloud (EC2) environment.
Name: perl-Net-Amazon-EC2
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Amazon-EC2/

Source: http://search.cpan.org/CPAN/authors/id/J/JK/JKIM/Net-Amazon-EC2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Digest::HMAC_SHA1) >= 1.01
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Moose) >= 0.38
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(XML::Simple) >= 2.18
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Digest::HMAC_SHA1) >= 1.01
Requires: perl(HTTP::Date)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Moose) >= 0.38
Requires: perl(Params::Validate)
Requires: perl(URI)
Requires: perl(XML::Simple) >= 2.18

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is a Perl interface to Amazon's Elastic Compute Cloud. It uses the
Query API to communicate with Amazon's Web Services framework.  This module is
coded against the Query API version of the '2009-11-30' version of the EC2 API
last updated December 8th, 2009.

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
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/Amazon/EC2.pm
%{perl_vendorlib}/Net/Amazon/EC2/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist
%exclude %{perl_vendorlib}/Net/Amazon/._EC2.pm

%changelog
* Wed Jan 26 2011 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
