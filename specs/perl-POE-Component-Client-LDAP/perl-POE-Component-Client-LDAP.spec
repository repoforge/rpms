# $Id$
# Authority: dag
# Upstream: Jonathan Steinert

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-LDAP

Summary: subclass of Net::LDAP which uses POE to speak via sockets in async mode.
Name: perl-POE-Component-Client-LDAP
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-LDAP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-LDAP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Net::LDAP) >= 0.31
BuildRequires: perl(Net::LDAP::ASN)
BuildRequires: perl(Convert::ASN1)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Filter::Stream)
BuildRequires: perl(POE::Session)
BuildRequires: perl(POE::Kernel)
BuildRequires: perl(POE::Wheel::Null)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(POE::Driver::SysRW)
Requires: perl >= 0:5.6.0

%description
subclass of Net::LDAP which uses POE to speak via sockets in async mode..

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
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/POE::Component::Client::LDAP.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/LDAP.pm
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/ASN1.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
