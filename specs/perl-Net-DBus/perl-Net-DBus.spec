# $Id$
# Authority: dag
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DBus
%define real_version 0.033006

Summary: Perl module with bindings for the DBus message system
Name: perl-Net-DBus
Version: 0.33.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DBus/

Source: http://www.cpan.org/modules/by-module/Net/Net-DBus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: pkgconfig

%description
perl-Net-DBus is a Perl module with bindings for the DBus message system.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc AUTHORS CHANGES LICENSE MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Net::DBus.3pm*
%doc %{_mandir}/man3/Net::DBus::*.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/DBus/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/DBus/
%{perl_vendorarch}/Net/DBus.pm

%changelog
* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.33.6-1
- Updated to release 0.33.6.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.33.5-1
- Updated to release 0.33.5.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.32.2-1
- Initial package. (using DAR)
