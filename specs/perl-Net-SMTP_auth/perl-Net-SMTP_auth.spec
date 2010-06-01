# $Id$
# Authority: shuff
# Upstream: Alex Pleiner <alex$zeitform,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SMTP_auth

Summary: SMTP_AUTH wrapper for Net::SMTP
Name: perl-%{real_name}
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMTP_auth/

Source: http://search.cpan.org/CPAN/authors/id/A/AP/APLEINER/Net-SMTP_auth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Authen::SASL) >= 2.03
BuildRequires: perl(Digest::HMAC_MD5) >= 1.00
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::Base64) >= 2.00
BuildRequires: perl(Net::SMTP) >= 2.26
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Authen::SASL) >= 2.03
Requires: perl(Digest::HMAC_MD5) >= 1.00
Requires: perl(MIME::Base64) >= 2.00
Requires: perl(Net::SMTP) >= 2.26


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module implements a client interface to the SMTP and ESMTP protocol AUTH
service extension, enabling a perl5 application to talk to and authenticate
against SMTP servers. This documentation assumes that you are familiar with the
concepts of the SMTP protocol described in RFC821 and with the AUTH service
extension described in RFC2554.

A new Net::SMTP_auth object must be created with the new method. Once this has
been done, all SMTP commands are accessed through this object.

The Net::SMTP_auth class is a subclass of Net::SMTP, which itself is a subclass
of Net::Cmd and IO::Socket::INET.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/*

%changelog
* Tue Jun 01 2010 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
