# $Id$
# Authority: dag
# Upstream: DJ Adams <dj,adams$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-RPC-HTTPgate

Summary: Perl module that implements an HTTP gateway for Jabber-RPC
Name: perl-Jabber-RPC-HTTPgate
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-RPC-HTTPgate/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-RPC-HTTPgate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jabber-RPC-HTTPgate is a Perl module that implements an HTTP gateway
for Jabber-RPC.

This package contains the following Perl module:

    Jabber::RPC::HTTPgate

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
%doc %{_mandir}/man3/Jabber::RPC::HTTPgate.3pm*
%dir %{perl_vendorlib}/Jabber/
%dir %{perl_vendorlib}/Jabber/RPC/
#%{perl_vendorlib}/Jabber/RPC/HTTPgate/
%{perl_vendorlib}/Jabber/RPC/HTTPgate.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
