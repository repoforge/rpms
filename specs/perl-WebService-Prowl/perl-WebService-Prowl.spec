# $Id$
# Authority: shuff
# Upstream: Masayoshi Sekimura <sekimura$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Prowl

Summary: a interface to Prowl Public API
Name: perl-%{real_name}
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Prowl/

Source: http://search.cpan.org/CPAN/authors/id/S/SE/SEKIMURA/WebService-Prowl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Simple)
BuildRequires: perl >= 5.8.1
Requires: perl(Carp)
Requires: perl(Crypt::SSLeay)
Requires: perl(LWP::UserAgent)
Requires: perl(URI::Escape)
Requires: perl(XML::Simple)
Requires: perl >= 5.8.1

### AnyEvent::HTTP is optional, not required
%filter_from_requires /^perl(AnyEvent.*/d
%filter_setup

%description
This module aims to be a implementation of a interface to the Prowl Public API
(as available on http://forums.cocoaforge.com/viewtopic.php?f=45&t=20339)

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
%doc %{_mandir}/man3/WebService::Prowl.3pm*
%doc %{_mandir}/man3/WebService::Prowl::*.3pm*
%dir %{perl_vendorlib}/WebService/
%dir %{perl_vendorlib}/WebService/Prowl/
%{perl_vendorlib}/WebService/Prowl.pm
%{perl_vendorlib}/WebService/Prowl/*.pm

%changelog
* Tue Nov 24 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Sat Oct 03 2009 Steve Huff <shuff@vecna.org> - 0.05-1
- Updated to version 0.05.

* Thu Oct 01 2009 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial package.
