# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Run3

Summary: Run a subprocess with input/ouput redirection
Name: perl-IPC-Run3
Version: 0.043
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Run3/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Run3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
Requires: perl >= 0:5.6.0

%description
Run a subprocess in batch mode.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/IPC::Run3.3pm*
%doc %{_mandir}/man3/IPC::Run3::*.3pm*
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Run3/
%{perl_vendorlib}/IPC/Run3.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.043-1
- Updated to version 0.043.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.042-1
- Updated to release 0.042.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.040-1
- Updated to release 0.040.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.039-1
- Updated to release 0.039.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.037-1
- Updated to release 0.037.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.036-1
- Updated to release 0.036.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.035-1
- Updated to release 0.035.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.034-1
- Updated to release 0.034.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.032-1
- Updated to release 0.032.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
