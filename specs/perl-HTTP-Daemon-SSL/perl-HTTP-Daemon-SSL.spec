# $Id$
# Authority: dag
# Upstream: Mark Aufflick <mark$aufflick,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Daemon-SSL

Summary: Simple HTTP server class with SSL support
Name: perl-HTTP-Daemon-SSL
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Daemon-SSL/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Daemon-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple HTTP server class with SSL support

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
%doc BUGS Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Daemon::SSL.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Daemon/
#%{perl_vendorlib}/HTTP/Daemon/SSL/
%{perl_vendorlib}/HTTP/Daemon/SSL.pm

%changelog
* Wed Apr 09 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
