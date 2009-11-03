# $Id$
# Authority: dag
# Upstream: Scott Penrose <scottp$dd,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Device-ParallelPort

Summary: Parallel Port Driver for Perl
Name: perl-Device-ParallelPort
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Device-ParallelPort/

Source: http://www.cpan.org/modules/by-module/Device/Device-ParallelPort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parallel Port Driver for Perl.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Device::ParallelPort.3pm*
%doc %{_mandir}/man3/Device::ParallelPort::*.3pm*
%dir %{perl_vendorlib}/Device/
%{perl_vendorlib}/Device/ParallelPort/
%{perl_vendorlib}/Device/ParallelPort.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
