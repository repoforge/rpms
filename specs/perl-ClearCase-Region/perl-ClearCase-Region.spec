# $Id$
# Authority: dag
# Upstream: Leslie D. Paul <Leslie,D,Paul$bankofamerica,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Region

Summary: Perl module named ClearCase-Region
Name: perl-ClearCase-Region
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Region/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-Region-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-ClearCase-Region is a Perl module.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE MANIFEST README docs/ examples/
%config %{perl_vendorlib}/*.conf
%dir %{perl_vendorlib}/ClearCase/
#%{perl_vendorlib}/ClearCase/Region/
%{perl_vendorlib}/ClearCase/Region.pm
%{perl_vendorlib}/ClearCase/Region_Cfg_Parser.pm
#%{perl_vendorlib}/ClearCase/Vob/
%{perl_vendorlib}/ClearCase/Vob.pm
%{perl_vendorlib}/ClearCase/Vob_Cfg_Parser.pm

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
