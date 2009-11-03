# $Id$
# Authority: dag
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Wrapper

Summary: General-purpose wrapper for cleartool
Name: perl-ClearCase-Wrapper
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Wrapper/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-Wrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
General-purpose wrapper for cleartool.

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
%doc Changes MANIFEST README README.GUI examples/
%doc %{_mandir}/man3/ClearCase::Wrapper.3pm*
%{_bindir}/cleartool.plx
%dir %{perl_vendorlib}/auto/ClearCase/
%{perl_vendorlib}/auto/ClearCase/Wrapper/
%dir %{perl_vendorlib}/ClearCase/
%{perl_vendorlib}/ClearCase/Wrapper/
%{perl_vendorlib}/ClearCase/Wrapper.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Initial package. (using DAR)
