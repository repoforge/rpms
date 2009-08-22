# $Id$
# Authority: dag
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Argv

Summary: ClearCase-specific subclass of Argv
Name: perl-ClearCase-Argv
Version: 1.46
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Argv/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-Argv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Argv) >= 1.22

%description
ClearCase-specific subclass of Argv.

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
%doc Changes MANIFEST README README.html examples/
%doc %{_mandir}/man3/ClearCase::Argv.3pm*
%dir %{perl_vendorlib}/ClearCase/
#%{perl_vendorlib}/ClearCase/Argv/
%{perl_vendorlib}/ClearCase/Argv.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.46-1
- Updated to version 1.46.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.45-1
- Updated to version 1.45.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Initial package. (using DAR)
