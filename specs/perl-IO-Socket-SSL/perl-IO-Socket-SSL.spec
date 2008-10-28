# $Id$
# Authority: dag
# Upstream: Steffen Ullrich <Steffen_Ullrich$genua,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Socket-SSL

Summary: Nearly transparent SSL encapsulation for IO::Socket::INET
Name: perl-IO-Socket-SSL
Version: 1.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Socket-SSL/

Source: http://www.cpan.org/modules/by-module/IO/IO-Socket-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
Nearly transparent SSL encapsulation for IO::Socket::INET.

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
find docs/ example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changes MANIFEST META.yml README* docs/ example/
%doc %{_mandir}/man3/IO::Socket::SSL.3pm*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%{perl_vendorlib}/IO/Socket/SSL.pm

%changelog
* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.07-2
- Disabled auto-requires for docs/ and example/.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 0.999-1
- Updated to release 0.999.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.97-1
- Updated to release 0.97.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.96-0
- Update to release 0.96.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.
- Initial package. (using DAR)
