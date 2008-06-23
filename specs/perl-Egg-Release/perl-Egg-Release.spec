# $Id$
# Authority: dag
# Upstream: Masatoshi Mizuno <lushe$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Egg-Release

Summary: Version of Egg WEB Application Framework
Name: perl-Egg-Release
Version: 3.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Egg-Release/

Source: http://www.cpan.org/modules/by-module/Egg/Egg-Release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
Requires: perl >= 2:5.8.1

%description
Version of Egg WEB Application Framework.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README licenses eg/
%doc %{_mandir}/man3/Egg.3pm*
%doc %{_mandir}/man3/Egg::*.3pm*
%{perl_vendorlib}/Egg/
%{perl_vendorlib}/Egg.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 3.14-1
- Updated to release 3.14.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 3.09-1
- Updated to release 3.09.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 3.07-1
- Updated to release 3.07.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.26-1
- Initial package. (using DAR)
