# $Id$
# Authority: dag
# Upstream: Chris Cobb <no,spam$ccobb,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Tools

Summary: OO interface to Rational's cleartool/multitool command interpreters
Name: perl-ClearCase-Tools
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Tools/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-Tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
OO interface to Rational's cleartool/multitool command interpreters.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/ClearCase::*.3pm*
%doc %{_mandir}/man3/MultiSite::*.3pm*
%{perl_vendorlib}/ClearCase/
%{perl_vendorlib}/MultiSite/

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
