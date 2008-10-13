# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Linux-LVM

Summary: Perl module for accessing Logical Volume Manager(LVM) data structures
Name: perl-Linux-LVM
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Linux-LVM/

Source: http://www.cpan.org/modules/by-module/Linux/Linux-LVM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Linux-LVM is a Perl module for accessing Logical Volume Manager(LVM)
data structures on Linux.

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Linux::LVM.3pm*
%dir %{perl_vendorlib}/Linux/
%{perl_vendorlib}/Linux/LVM.pm
%dir %{perl_vendorlib}/auto/Linux/
%{perl_vendorlib}/auto/Linux/LVM/

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
