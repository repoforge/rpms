# $Id$
# Authority: dag
# Upstream: Karthik Krishnamurthy <karthik,k$extremix,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Conf-Bind8

Summary: Front end for a suite of classes for manipulating a Bind8 conf and associated zone record files
Name: perl-Unix-Conf-Bind8
Version: 0.3
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Conf-Bind8/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Conf-Bind8-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

### Provides required by package itself
Provides: perl(Unix::Conf/Bind8/DB/Parser)

%description
Front end for a suite of classes for manipulating a Bind8 conf
and associated zone record files.

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
%doc %{_mandir}/man3/Unix::Conf::Bind8.3pm*
%doc %{_mandir}/man3/Unix::Conf::Bind8::*.3pm*
%dir %{perl_vendorlib}/Unix/
%dir %{perl_vendorlib}/Unix/Conf/
%dir %{perl_vendorlib}/Unix/Conf/Bind8/
%{perl_vendorlib}/Unix/Conf/Bind8/
%{perl_vendorlib}/Unix/Conf/Bind8.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.3-2
- Added selfcontained provides.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
