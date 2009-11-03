# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Address-IPv4-Local

Summary: A class for discovering the local system's IP address
Name: perl-Net-Address-IPv4-Local
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Address-IPv4-Local/

Source: http://www.cpan.org/modules/by-module/Net/Net-Address-IPv4-Local-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
Requires: perl(Error)

%description
A class for discovering the local system's IP address.

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
%doc CHANGES MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Net::Address::IPv4::Local.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Address/
%dir %{perl_vendorlib}/Net/Address/IPv4/
%{perl_vendorlib}/Net/Address/IPv4/Local.pm

%changelog
* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
