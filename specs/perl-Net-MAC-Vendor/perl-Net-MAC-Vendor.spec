# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-MAC-Vendor

Summary: Lookup the vendor for a MAC address
Name: perl-Net-MAC-Vendor
Version: 1.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-MAC-Vendor/

Source: http://www.cpan.org/modules/by-module/Net/Net-MAC-Vendor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lookup the vendor for a MAC address.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::MAC::Vendor.3*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/MAC/
#%{perl_vendorlib}/Net/MAC/Vendor/
%{perl_vendorlib}/Net/MAC/Vendor.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.17-1
- Updated to latest upstream version { old source not available }

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
