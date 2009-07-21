# $Id$
# Authority: dag
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Daemon-Generic

Summary: Framework to provide start/stop/reload for a daemon
Name: perl-Daemon-Generic
Version: 0.61
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Daemon-Generic/

Source: http://www.cpan.org/modules/by-module/Daemon/Daemon-Generic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Framework to provide start/stop/reload for a daemon.

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
%doc CHANGELOG MANIFEST META.yml README
%doc %{_mandir}/man3/Daemon::Generic.3pm*
%doc %{_mandir}/man3/Daemon::Generic::*.3pm*
%dir %{perl_vendorlib}/Daemon/
%{perl_vendorlib}/Daemon/Generic/
%{perl_vendorlib}/Daemon/Generic.pm
%{perl_vendorlib}/Daemon/Generic.pod

%changelog
* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 0.61-1
- Initial package. (using DAR)
