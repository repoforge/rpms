# $Id$
# Authority: dag
# Upstream: Asher Blum <asher$wildspark,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-RBLClient

Summary: Queries multiple Realtime Blackhole Lists in parallel
Name: perl-Net-RBLClient
Version: 0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-RBLClient/

Source: http://www.cpan.org/modules/by-module/Net/Net-RBLClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Queries multiple Realtime Blackhole Lists in parallel.

%prep
%setup -n RBLCLient-%{version}

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
%doc README
%doc %{_mandir}/man1/spamalyze.1*
%doc %{_mandir}/man3/Net::RBLClient.3pm*
%{_bindir}/spamalyze
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/RBLClient/
%{perl_vendorlib}/Net/RBLClient.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
