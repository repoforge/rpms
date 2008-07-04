# $Id$
# Authority: dag
# Upstream: Nagios Plugin Development Team <nagiosplug-devel$lists,sourceforge,net>
# Upstream: Ton Voon <ton,voon$altinity,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Nagios-Plugin

Summary: Family of perl modules to streamline writing Nagios
Name: perl-Nagios-Plugin
Version: 0.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Nagios-Plugin/

Source: http://www.cpan.org/authors/id/T/TO/TONVOON/Nagios-Plugin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Math::Calc::Units)
Requires: perl(Config::Tiny)

%description
A family of perl modules to streamline writing Nagios.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Nagios::Plugin.3pm*
%doc %{_mandir}/man3/Nagios::Plugin::*.3pm*
%dir %{perl_vendorlib}/Nagios/
%{perl_vendorlib}/Nagios/Plugin/
%{perl_vendorlib}/Nagios/Plugin.pm

%changelog
* Tue Jul 01 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sat Mar 15 2008 Dag Wieers <dag@wieers.com> - 0.24-2
- Added perl(Config::Tiny) as a dependency.

* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
