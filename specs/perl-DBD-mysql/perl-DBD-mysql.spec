# $Id$
# Authority: dag
# Upstream: Patrick Galbraith <patg$patg,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-mysql

Summary: Perl module that implements a MySQL driver for DBI
Name: perl-DBD-mysql
Version: 4.008
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-mysql/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-mysql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, mysql-devel

# rhel/centos contains the perl module DBD-mysql in a package named perl-DBD-MySQL
Obsoletes: perl-DBD-MySQL <= %{version}-%{release}
Provides: perl-DBD-MySQL = %{version}-%{release}

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/mysql/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/mysql/
%{perl_vendorarch}/DBD/mysql.pm
%dir %{perl_vendorarch}/Bundle/
%dir %{perl_vendorarch}/Bundle/DBD/
%{perl_vendorarch}/Bundle/DBD/mysql.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 4.008-1
- Updated to release 4.008.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 4.007-1
- Updated to release 4.007.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 4.006-1
- Updated to release 4.006.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 4.005-1
- Initial package. (using DAR)
