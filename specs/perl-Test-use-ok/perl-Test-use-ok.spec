# $Id$
# Authority: dag
# Upstream: , 2006 by Audrey Tang <cpan@audreyt.org>.

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-use-ok

Summary: Alternative to Test::More::use_ok
Name: perl-Test-use-ok
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-use-ok/

Source: http://www.cpan.org/modules/by-module/Test/Test-use-ok-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
Requires: perl >= 0:5.005

%description
Alternative to Test::More::use_ok.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/ok.3pm*
%doc %{_mandir}/man3/Test::use::ok.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/use/
%{perl_vendorlib}/ok.pm
%{perl_vendorlib}/Test/use/ok.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
