# $Id$
# Authority: dag
# Upstream: GomoR <perl$gomor,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Packet-Target

Summary: an object for all network related stuff
Name: perl-Net-Packet-Target
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Packet-Target/

Source: http://www.cpan.org/modules/by-module/Net/Net-Packet-Target-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
an object for all network related stuff.

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
%doc Changes LICENSE LICENSE.Artistic MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::Packet::Target.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Packet/
#%{perl_vendorlib}/Net/Packet/Target/
%{perl_vendorlib}/Net/Packet/Target.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
