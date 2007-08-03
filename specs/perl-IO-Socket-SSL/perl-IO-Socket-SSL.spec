# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Socket-SSL

Summary: IO-Socket-SSL module for perl
Name: perl-IO-Socket-SSL
Version: 1.07
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Socket-SSL/

Source: http://www.cpan.org/modules/by-module/IO/IO-Socket-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.8.0

%description
IO-Socket-SSL module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
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
%doc BUGS Changes MANIFEST README docs/* example/
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/IO/
%dir %{perl_vendorlib}/IO/Socket/
%{perl_vendorlib}/IO/Socket/SSL.pm

%changelog
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
