# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-DNS

Summary: Event driven wrapper for Net::DNS::Resolver
Name: perl-POE-Component-Client-DNS
Version: 1.051
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-DNS/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-DNS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::DNS) >= 0.59
BuildRequires: perl(POE) >= 1.28
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings) >= 0.084
Requires: perl(Net::DNS) >= 0.59
Requires: perl(POE) >= 1.28
Requires: perl(Test::More)
Requires: perl(Test::NoWarnings) >= 0.084

%filter_from_requires /^perl*/d
%filter_setup

%description
POE::Component::Client::DNS is an event driven wrapper for
Net::DNS::Resolver.  It accepts events containing Net::DNS::Resolver
questions, and it emits events carrying Net::DNS::Packet responses.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Component::Client::DNS.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
#%{perl_vendorlib}/POE/Component/Client/DNS/
%{perl_vendorlib}/POE/Component/Client/DNS.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.051-1
- Updated to version 1.051.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 1.050-1
- Updated to version 1.050.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.9803-1
- Initial package.
