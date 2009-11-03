# $Id$
# Authority: dag
# Upstream: Jerzy Wachowiak <jerzy,wachowiak$wp,pl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-FastForward

Summary: Perl module that implements spreadsheet web services  
Name: perl-Apache-FastForward
Version: 1.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-FastForward/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-FastForward-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.4
Requires: perl >= 2:5.8.4

%description
perl-Apache-FastForward is a Perl module that implements
spreadsheet web services.

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
%doc %{_mandir}/man3/Apache::FastForward.3pm*
%doc %{_mandir}/man3/Apache::FastForward::Spreadsheet.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/FastForward/
%{perl_vendorlib}/Apache/FastForward.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
