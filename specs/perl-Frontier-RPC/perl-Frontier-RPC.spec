# $Id$
# Authority: dag
# Upstream: Ken MacLeod <ken$bitsko,slc,ut,us>

### EL6 ships with perl-Frontier-RPC-0.07b4p1-9.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Frontier-RPC

Summary: Encode/decode RPC2 format XML
Name: perl-Frontier-RPC
Version: 0.07b4
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Frontier-RPC/

Source: http://www.cpan.org/modules/by-module/Frontier/Frontier-RPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Encode/decode RPC2 format XML.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog Changes MANIFEST README docs/ examples/
%doc %{_mandir}/man3/Apache::XMLRPC.3pm*
%doc %{_mandir}/man3/Frontier::*.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/XMLRPC.pm
%{perl_vendorlib}/Frontier/

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.07b4-1
- Initial package. (using DAR)
