# $Id$
# Authority: dag
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-PidUtil

Summary: PID file management utilities
Name: perl-Proc-PidUtil
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-PidUtil/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-PidUtil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
PID file management utilities.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Proc::PidUtil.3pm*
%dir %{perl_vendorlib}/Proc/
#%{perl_vendorlib}/Proc/PidUtil/
%{perl_vendorlib}/Proc/PidUtil.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
