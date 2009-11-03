# $Id$
# Authority: dag
# Upstream: Tony Monroe <tmonroe+cpan$nog,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IPv6Addr

Summary: Check validity of IPv6 addresses
Name: perl-Net-IPv6Addr
Version: 0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IPv6Addr/

Source: http://www.cpan.org/modules/by-module/Net/Net-IPv6Addr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Check validity of IPv6 addresses.

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
%doc ChangeLog MANIFEST README rfc1886.txt rfc1924.txt rfc2373.txt
%doc %{_mandir}/man3/Net::IPv6Addr.3pm*
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/IPv6Addr/
%{perl_vendorlib}/Net/IPv6Addr.pm

%changelog
* Sun Mar 16 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
