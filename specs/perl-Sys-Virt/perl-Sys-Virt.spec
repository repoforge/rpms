# $Id$
# Authority: dag
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Virt
%define real_version 0.001001

Summary: Perl module to represent and manage a libvirt hypervisor connection
Name: perl-Sys-Virt
Version: 0.1.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Virt/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-Virt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, xen-libs-devel

%description
perl-Sys-Virt is a Perl module to represent and manage
a libvirt hypervisor connection.

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
%doc AUTHORS CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Sys::Virt.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/Virt.pm
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/Virt/

%changelog
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.1.1-1
- Initial package. (using DAR)
