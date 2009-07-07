# $Id$
# Authority: dag
# Upstream: Chris Winters <chris$cwinters,com>
# Upstream: Stevan Little <stevan$iinteractive,com>
# Upstream: Rob Kinyon <rob,kinyon$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Mock

Summary: Mock database driver for testing
Name: perl-DBD-Mock
Version: 1.39
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Mock/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Mock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.6.0

%description
Mock database driver for testing.

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
%doc %{_mandir}/man3/DBD::Mock.3pm*
%dir %{perl_vendorlib}/DBD/
#%{perl_vendorlib}/DBD/Mock/
%{perl_vendorlib}/DBD/Mock.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.39-1
- Updated to version 1.39.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.37-1
- Updated to release 1.37.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.35-1
- Initial package. (using DAR)
