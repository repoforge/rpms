# $Id: perl-DBD-mysql.spec 8763 2010-04-16 15:05:31Z cmr $
# Authority: dag
# Upstream: Patrick Galbraith <patg$patg,net>

### EL6 ships with perl-DBD-MySQL-4.013-3.el6
### EL5 ships with perl-DBD-MySQL-3.0007-2.el5
### EL4 ships with perl-DBD-MySQL-2.9004-3.1
### EL3 ships with perl-DBD-MySQL-2.1021-4.EL3
### EL2 ships with perl-DBD-MySQL-1.2216-4
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-mysql

Summary: Perl module that implements a MySQL driver for DBI
Name: perl-DBD-MySQL
Version: 4.014
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-mysql/

Source: http://search.cpan.org/CPAN/authors/id/C/CA/CAPTTOFU/DBD-mysql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
BuildRequires: perl(DBI) >= 1.08
BuildRequires: perl(Data::Dumper)
Requires: mysql
Requires: perl(DBI) >= 1.08
Requires: perl(Data::Dumper)

### We used to provide RPMS with the upstreal distribution name perl-DBD-mysql
Obsoletes: perl-DBD-mysql <= %{version}-%{release}
Provides: perl-DBD-mysql = %{version}-%{release}

%description
perl-DBD-mysql is a Perl module that implements a MySQL driver for DBI.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL.html MANIFEST MANIFEST.SKIP META.yml README TODO eg/
%doc %{_mandir}/man3/Bundle::DBD::mysql.3pm*
%doc %{_mandir}/man3/DBD::mysql.3pm*
%doc %{_mandir}/man3/DBD::mysql::INSTALL.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/mysql/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/mysql/
%{perl_vendorarch}/DBD/mysql.pm
%dir %{perl_vendorarch}/Bundle/
%dir %{perl_vendorarch}/Bundle/DBD/
%{perl_vendorarch}/Bundle/DBD/mysql.pm

%changelog
* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 4.014-1
- Updated to version 4.014.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 4.013-1
- Updated to version 4.013.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 4.012-1
- Updated to version 4.012.

* Thu May 27 2009 Christoph Maser <cmr@financial.com> - 4.011-1
- Updated to release 4.011.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 4.010-1
- Updated to release 4.010.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 4.008-1
- Updated to release 4.008.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 4.007-1
- Updated to release 4.007.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 4.006-1
- Updated to release 4.006.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 4.005-1
- Initial package. (using DAR)
