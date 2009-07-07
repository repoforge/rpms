# $Id$
# Authority: dag
# Upstream: Greg Sabino Mullane <greg$turnstep,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Pg

Summary: DBI PostgreSQL interface
Name: perl-DBD-Pg
Version: 2.13.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Pg/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(DBI) >= 1.52
BuildRequires: perl(Module::Signature) >= 0.5
BuildRequires: perl(Test::Harness) >= 2.03
#BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Simple) >= 0.47
BuildRequires: perl(version)
BuildRequires: postgresql-devel
Requires: perl >= 1:5.6.1
Requires: perl(DBI) >= 1.52
Requires: postgresql

%description
DBI PostgreSQL interface.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.dev README.win32 SIGNATURE TODO
%doc %{_mandir}/man3/DBD::Pg.3pm*
%doc %{_mandir}/man3/Bundle::DBD::Pg.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Pg/
%dir %{perl_vendorarch}/Bundle/
%dir %{perl_vendorarch}/Bundle/DBD/
%{perl_vendorarch}/Bundle/DBD/Pg.pm
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Pg.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 2.13.1-1
- Updated to version 2.13.1.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 2.11.5-1
- Updated to release 2.11.5.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 2.11.1-1
- Updated to release 2.11.1.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.10.7
- Updated to release 2.10.7.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Updated to release 2.8.1.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.7.1-1
- Updated to release 2.7.1.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.6.4-1
- Updated to release 2.6.4.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.6.1-1
- Updated to release 2.6.1.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.49-1
- Initial package. (using DAR)
