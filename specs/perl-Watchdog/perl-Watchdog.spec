# $Id$
# Authority: dag
# Upstream: Clemens Gesell <clemens,gesell$vegatron,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Watchdog

Summary: Perl module named Watchdog
Name: perl-Watchdog
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Watchdog/

Source: http://www.cpan.org/modules/by-module/Watchdog/Watchdog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Watchdog is a Perl module.

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
%doc MANIFEST README upgrade-0.09-0.10.diff
%doc %{_mandir}/man3/Watchdog::*.3pm*
%{perl_vendorlib}/Watchdog/

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
