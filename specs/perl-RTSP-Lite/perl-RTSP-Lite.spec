# $Id$
# Authority: dag
# Upstream: Masaaki NABESHIMA <nabe$kosho,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RTSP-Lite

Summary: Lightweight RTSP implementation
Name: perl-RTSP-Lite
Version: 0.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RTSP-Lite/

Source: http://www.cpan.org/modules/by-module/RTSP/RTSP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lightweight RTSP implementation.

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
%doc README
%doc %{_mandir}/man3/RTSP::Lite.3pm*
%dir %{perl_vendorlib}/RTSP/
%{perl_vendorlib}/RTSP/Lite.pm
%{perl_vendorlib}/RTSP/describe.pl
%{perl_vendorlib}/RTSP/play.pl

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
