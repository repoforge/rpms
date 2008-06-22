# $Id$
# Authority: dag
# Upstream: Tim Bunce <Tim,Bunce$pobox,com>
# Upstream: Tim Bunce <dbi-users$perl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBI

Summary: Database independent interface for Perl
Name: perl-DBI
Version: 1.605
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBI/

Source: http://www.cpan.org/modules/by-module/DBI/DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-DBI is a Perl module that implements a database independent interface.

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
%doc Changes MANIFEST META.yml README Roadmap.pod TODO_2005.txt
%doc %{_mandir}/man1/dbilogstrip.1*
%doc %{_mandir}/man1/dbiprof.1*
%doc %{_mandir}/man1/dbiproxy.1*
%doc %{_mandir}/man3/Bundle::DBI.3pm*
%doc %{_mandir}/man3/DBD::*.3pm*
%doc %{_mandir}/man3/DBI.3pm*
%doc %{_mandir}/man3/DBI::*.3pm*
%doc %{_mandir}/man3/Roadmap.3pm*
%doc %{_mandir}/man3/TASKS.3pm*
%doc %{_mandir}/man3/Win32::DBIODBC.3pm*
%{_bindir}/dbilogstrip
%{_bindir}/dbiprof
%{_bindir}/dbiproxy
%{perl_vendorarch}/auto/DBI/
%dir %{perl_vendorarch}/Bundle/
%{perl_vendorarch}/Bundle/DBI.pm
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBI/
%{perl_vendorarch}/DBI.pm
%{perl_vendorarch}/Roadmap.pod
%{perl_vendorarch}/TASKS.pod
%dir %{perl_vendorarch}/Win32/
%{perl_vendorarch}/Win32/DBIODBC.pm
%{perl_vendorarch}/dbixs_rev.pl
#%{perl_vendorarch}/goferperf.pl

### Remove this file because it generates an rpm dependency for Win32::ODBC
%exclude %{perl_vendorarch}/DBI/W32ODBC.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.605-1
- Updated to release 1.605.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.604-1
- Updated to release 1.604.

* Mon Feb 18 2008 Dag Wieers <dag@wieers.com> - 1.602-1
- Updated to release 1.602.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.601-1
- Updated to release 1.601.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.58-2
- Remove dependency on perl(Win32::ODBC). (Mark D. Nagel)

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.58-1
- Initial package. (using DAR)
