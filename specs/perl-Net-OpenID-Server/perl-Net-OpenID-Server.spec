# $Id$
# Authority: shuff
# Upstream: Martin Atkins <mart$degeneration,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenID-Server

Summary: library for building your own OpenID server
Name: perl-Net-OpenID-Server
Version: 1.02
Release: 1%{?dist}
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OpenID-Server/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MART/Net-OpenID-Server-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Crypt::DH) >= 0.05
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(URI)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Crypt::DH) >= 0.05
Requires: perl(Digest::SHA1)
Requires: perl(MIME::Base64)
Requires: perl(URI)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is the Perl API for (the server half of) OpenID, a distributed identity
system based on proving you own a URL, which is then your identity. More
information is available at:

  http://openid.net/

As of version 1.01 this module has support for both OpenID 1.1 and 2.0. Prior
to this, only 1.1 was supported.

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
%doc ChangeLog META.yml doc/*
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/OpenID/
%{perl_vendorlib}/Net/OpenID/Server.pm
#%{perl_vendorlib}/Net/OpenID/Server/*
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Aug 17 2010 Steve Huff <shuff@vecna.org> - 1.02-1
- Initial package.
