# $Id$
# Authority: dag
# Upstream: Oliver Gorwits <oliver,gorwits$oucs,ox,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Appliance-Session

Summary: Run command-line sessions to network appliances
Name: perl-Net-Appliance-Session
Version: 1.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Appliance-Session/

Source: http://www.cpan.org/modules/by-module/Net/Net-Appliance-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Run command-line sessions to network appliances

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
%doc Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::Appliance::Session.3pm*
%doc %{_mandir}/man3/Net::Appliance::Session::*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Appliance/
%{perl_vendorlib}/Net/Appliance/Session/
%{perl_vendorlib}/Net/Appliance/Session.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.36-1
- Updated to version 1.36.

* Tue Sep 16 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Initial package. (using DAR)
