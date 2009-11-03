# $Id$
# Authority: dag
# Upstream: Sebastian Riedel, <sri@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Engine-Apache

Summary: Catalyst Apache Engines
Name: perl-Catalyst-Engine-Apache
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Engine-Apache/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Engine-Apache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime) >= 5.7

%description
Catalyst Apache Engines.

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
%doc %{_mandir}/man3/Catalyst::Engine::Apache.3pm*
%doc %{_mandir}/man3/Catalyst::Engine::Apache::*.3pm*
%doc %{_mandir}/man3/Catalyst::Engine::Apache2.3pm*
%doc %{_mandir}/man3/Catalyst::Engine::Apache2::*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Engine/
%{perl_vendorlib}/Catalyst/Engine/Apache/
%{perl_vendorlib}/Catalyst/Engine/Apache.pm
%{perl_vendorlib}/Catalyst/Engine/Apache2/
%{perl_vendorlib}/Catalyst/Engine/Apache2.pm

%changelog
* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Initial package. (using DAR)
