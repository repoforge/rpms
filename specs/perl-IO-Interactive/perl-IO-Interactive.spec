# $Id$
# Authority: dag
# Upstream: Damian Conway <DCONWAY$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Interactive
%define real_version 0.000005

Summary: Utilities for interactive I/O
Name: perl-IO-Interactive
Version: 0.0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Interactive/

Source: http://www.cpan.org/modules/by-module/IO/IO-Interactive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Utilities for interactive I/O.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/IO::Interactive.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/Interactive/
%{perl_vendorlib}/IO/Interactive.pm

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Initial package. (using DAR)
