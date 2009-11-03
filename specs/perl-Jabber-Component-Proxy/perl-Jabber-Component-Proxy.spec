# $Id$
# Authority: dag
# Upstream: DJ Adams <dj,adams$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-Component-Proxy

Summary: Perl module that implements a simple proxy for Jabber Components
Name: perl-Jabber-Component-Proxy
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-Component-Proxy/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-Component-Proxy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jabber-Component-Proxy is a Perl module that implements a simple proxy
for Jabber Components.

This package contains the following Perl module:

    Jabber::Component::Proxy

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
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/Jabber::Component::Proxy.3pm*
%dir %{perl_vendorlib}/Jabber/
%dir %{perl_vendorlib}/Jabber/Component/
#%{perl_vendorlib}/Jabber/Component/Proxy/
%{perl_vendorlib}/Jabber/Component/Proxy.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
