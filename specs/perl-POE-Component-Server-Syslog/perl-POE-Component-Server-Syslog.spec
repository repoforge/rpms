# $Id$
# Authority: dries
# Upstream: Matt Cashner <sungo$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-Syslog

Summary: Syslog services for POE
Name: perl-POE-Component-Server-Syslog
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-Syslog/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides syslog services for POE.

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
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE VERSION examples/
%doc %{_mandir}/man3/POE::Component::Server::Syslog.3pm*
%doc %{_mandir}/man3/POE::Component::Server::Syslog::*.3pm*
%doc %{_mandir}/man3/POE::Filter::Syslog.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/Syslog/
%{perl_vendorlib}/POE/Component/Server/Syslog.pm
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/Syslog.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
