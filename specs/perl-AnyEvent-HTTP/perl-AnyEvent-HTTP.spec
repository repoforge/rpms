# $Id$
# Authority: shuff
# Upstream: Marc Lehmann <schmorp@schmorp.de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

### perl-AnyEvent is rfx on EL5
%{?el5:# Tag: rfx}

%define real_name AnyEvent-HTTP

Summary: Simple but non-blocking HTTP/HTTPS client
Name: perl-%{real_name}
Version: 2.13
Release: 2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyEvent-HTTP/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(AnyEvent) >= 5
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(AnyEvent) >= 5
Requires: perl(common::sense)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module implements a simple, stateless and non-blocking HTTP client. It
supports GET, POST and other request methods, cookies and more, all on a very
low level. It can follow redirects, supports proxies, and automatically limits
the number of connections to the values specified in the RFC.

It should generally be a "good client" that is enough for most HTTP tasks.
Simple tasks should be simple, but complex tasks should still be possible as
the user retains control over request and response headers.

The caller is responsible for authentication management, cookies (if the
simplistic implementation in this module doesn't suffice), referer and other
high-level protocol details for which this module offers only limited support.

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
%doc COPYING Changes MANIFEST META.json README 
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AnyEvent/HTTP.pm

%changelog
* Mon Aug 01 2011 Steve Huff <shuff@vecna.org> - 2.13-2
- RFX on el5, since it needs AnyEvent.

* Sat Jul 30 2011 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Thu Apr 21 2011 Steve Huff <shuff@vecna.org> - 2.04-1
- Updated to release 2.04.
- Fleshed out description and dependencies a bit.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 1.44-1
- Updated to version 1.44.

* Thu Sep 17 2009 Steve Huff <shuff@vecna.org> - 1.43-1
- Initial package.
