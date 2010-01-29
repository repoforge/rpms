# $Id$
# Authority: shuff
# Upstream: Sampo Kellomaki <sampo$symlabs,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SMPP

Summary: Pure Perl implementation of SMPP 3.4 over TCP
Name: perl-%{real_name}
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMPP/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAMPO/Net-SMPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_from_requires /^\/apps.*/d
%filter_setup

%description
Implements Short Message Peer to Peer protocol, which is frequently used to
pass short messages between mobile operators implementing short message service
(SMS). This is applicable to both European GSM and American CDMA/TDMA systems.

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/*

%changelog
* Fri Jan 29 2010 Steve Huff <shuff@vecna.org> - 1.12-1
- Initial package.
