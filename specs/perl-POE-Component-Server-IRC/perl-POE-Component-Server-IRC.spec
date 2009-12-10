# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-IRC

Summary: Event-driven networkable IRC server daemon
Name: perl-POE-Component-Server-IRC
Version: 1.40
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-IRC/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Algorithm::Diff) >= 1.19
BuildRequires: perl(Carp)
BuildRequires: perl(Crypt::PasswdMD5) >= 1.3
BuildRequires: perl(Date::Format)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::Netmask) >= 1.9012
BuildRequires: perl(POE) >= 0.9999
BuildRequires: perl(POE::Component::Client::DNS) >= 1
BuildRequires: perl(POE::Component::Client::Ident) >= 1
BuildRequires: perl(POE::Component::IRC) >= 5.7
BuildRequires: perl(POE::Component::Pluggable) >= 1.14
BuildRequires: perl(POE::Filter::IRCD) >= 2.2
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Filter::Stackable)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl >= 5.6.0
Requires: perl(Algorithm::Diff) >= 1.19
Requires: perl(Carp)
Requires: perl(Crypt::PasswdMD5) >= 1.3
Requires: perl(Date::Format)
Requires: perl(Net::Netmask) >= 1.9012
Requires: perl(POE) >= 0.9999
Requires: perl(POE::Component::Client::DNS) >= 1
Requires: perl(POE::Component::Client::Ident) >= 1
Requires: perl(POE::Component::IRC) >= 5.7
Requires: perl(POE::Component::Pluggable) >= 1.14
Requires: perl(POE::Filter::IRCD) >= 2.2
Requires: perl(POE::Filter::Line)
Requires: perl(POE::Filter::Stackable)
Requires: perl(POE::Wheel::ReadWrite)
Requires: perl(POE::Wheel::SocketFactory)
Requires: perl(Socket)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup


%description
A fully event-driven networkable IRC server daemon module.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man1/pmkpasswd.1*
%doc %{_mandir}/man3/POE::Component::Server::IRC.3pm*
%doc %{_mandir}/man3/POE::Component::Server::IRC::*.3pm*
%{_bindir}/pmkpasswd
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/IRC/
%{perl_vendorlib}/POE/Component/Server/IRC.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.38-1
- Updated to version 1.38.

* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 1.32-1
- Updated to release 1.32.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Fri Jan 05 2007 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
