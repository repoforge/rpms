# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Whois

Summary: One shot non-blocking RFC 812 WHOIS query
Name: perl-POE-Component-Client-Whois
Version: 1.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Whois/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-Whois-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::Netmask) >= 1.9012
BuildRequires: perl(POE) >= 1.004
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl >= 5.6.0
Requires: perl(Carp)
Requires: perl(Net::Netmask) >= 1.9012
Requires: perl(POE) >= 1.004
Requires: perl(POE::Filter::Line)
Requires: perl(POE::Wheel::ReadWrite)
Requires: perl(POE::Wheel::SocketFactory)
Requires: perl(Socket)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
This module implements a non-blocking RFC812 whois query.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Client::Whois.3pm*
%doc %{_mandir}/man3/POE::Component::Client::Whois::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/Whois/
%{perl_vendorlib}/POE/Component/Client/Whois.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.28-1
- Updated to version 1.28.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.

