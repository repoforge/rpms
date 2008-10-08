# $Id$
# Authority: dag
# Upstream: Pythian Remote DBA <pause$pythian,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Oracle

Summary: Oracle database driver for the DBI module
Name: perl-DBD-Oracle
Version: 1.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Oracle/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Oracle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(DBI)

%description
Oracle database driver for the DBI module.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.64bit.txt
%doc README.aix.txt README.clients.txt README.explain.txt README.help.txt
%doc README.hpux.txt README.java.txt README.linux.txt README.login.txt
%doc README.longs.txt README.macosx.txt README.sec.txt README.vms.txt
%doc README.win32.txt %doc README.wingcc.txt Todo
%doc %{_mandir}/man3/DBD::Oracle.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Oracle/
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Oracle.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Initial package. (using DAR)
