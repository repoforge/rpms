# $Id$
# Authority: shuff
# Upstream: Leon Brocard <acme$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name LWP-ConnCache-MaxKeepAliveRequests

Summary: A connection cache that enforces a max keep alive limit
Name: perl-%{real_name}
Version: 0.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LWP-ConnCache-MaxKeepAliveRequests/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/LWP-ConnCache-MaxKeepAliveRequests-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(Moose)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(LWP)
Requires: perl(Moose)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
LWP::UserAgent is the default module for issuing HTTP requests from Perl. It
has a keep_alive setting which by default allows unlimited requests to the same
server. Some servers will disconnect you after a limited number of requests (in
Apache 2 this is achieved with the MaxKeepAliveRequests directive). This module
allows you to limit the maximum number of keep alive requests to a server.

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
%dir %{perl_vendorlib}/LWP/ConnCache/
%{perl_vendorlib}/LWP/ConnCache/*

%changelog
* Thu Feb 25 2010 Steve Huff <shuff@vecna.org> - 0.32-1
- Initial package.
