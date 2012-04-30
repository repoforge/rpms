# $Id$
# Authority: dag
# Upstream: Tim Bunce <Tim,Bunce$pobox,com>
# Upstream: Tim Bunce <dbi-users$perl,org>

### EL6 ships with perl-DBI-1.609-4.el6
### EL5 ships with perl-DBI-1.52-2.el5
### EL4 ships with perl-DBI-1.40-9
### EL3 ships with perl-DBI-1.32-9
### EL2 ships with perl-DBI-1.18-3
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBI

Summary: Database independent interface for Perl
Name: perl-DBI
Version: 1.620
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBI/

Source: http://search.cpan.org/CPAN/authors/id/T/TI/TIMB/DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 1
#BuildRequires: perl(Test::Simple) >= 0.84
BuildRequires: perl(Test::Simple) 
Requires: perl(File::Spec)
Requires: perl(Scalar::Util)
Requires: perl(Storable) >= 1
#Requires: perl(Test::Simple) >= 0.84
Requires: perl(Test::Simple)

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-DBI is a Perl module that implements a database independent interface.

%prep
%setup -q -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
#%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO_2005.txt
%doc %{_mandir}/man1/dbilogstrip.1*
%doc %{_mandir}/man1/dbiprof.1*
%doc %{_mandir}/man1/dbiproxy.1*
%doc %{_mandir}/man3/Bundle::DBI.3pm*
%doc %{_mandir}/man3/DBD::*.3pm*
%doc %{_mandir}/man3/DBI.3pm*
%doc %{_mandir}/man3/DBI::*.3pm*
#%doc %{_mandir}/man3/Roadmap.3pm*
#%doc %{_mandir}/man3/TASKS.3pm*
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
#%{perl_vendorarch}/Roadmap.pod
#%{perl_vendorarch}/TASKS.pod
%dir %{perl_vendorarch}/Win32/
%{perl_vendorarch}/Win32/DBIODBC.pm
%{perl_vendorarch}/dbixs_rev.pl
#%{perl_vendorarch}/goferperf.pl

### Remove this file because it generates an rpm dependency for Win32::ODBC
%exclude %{perl_vendorarch}/DBI/W32ODBC.pm

%changelog
* Mon Apr 30 2012 David Hrbáč <david@hrbac.cz> - 1.620-1
- new upstream release

* Wed Apr 25 2012 David Hrbáč <david@hrbac.cz> - 1.619-1
- new upstream release

* Tue Feb 28 2012 David Hrbáč <david@hrbac.cz> - 1.618-1
- new upstream release

* Thu Feb 16 2012 David Hrbáč <david@hrbac.cz> - 1.617-1
- new upstream release

* Sun Jan 30 2011 David Hrbáč <david@hrbac.cz> - 1.616-1
- new upstream release

* Wed Sep 22 2010 David Hrbáč <david@hrbac.cz> - 1.615-1
- new upstream release

* Fri Sep 10 2010 David Hrbáč <david@hrbac.cz> - 1.613-1
- new upstream release

* Wed May 26 2010 Christoph Maser <cmaser@gmx.de> - 1.611-1
- Updated to version 1.611.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.609-1
- Updated to version 1.609.

* Thu May 28 2009 Christoph Maser <cmr@financial.com> - 1.608-1
- Updated to release 1.608.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.607-1
- Updated to release 1.607.

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
