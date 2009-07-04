# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Locker

Summary: Distributed lock handler
Name: perl-IPC-Locker
Version: 1.484
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Locker/

Source: http://search.cpan.org/CPAN/authors/id/W/WS/WSNYDER/IPC-Locker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package provides a server for locks and a package for clients
to access that server.  The result is that clients can access named
locks on a Internet wide bases, solving critical section problems
without the mess of NFS or other file locking techniques.

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
%doc COPYING Changes MANIFEST MANIFEST.SKIP META.yml README readme.texi
%doc %{_mandir}/man1/lockerd.1*
%doc %{_mandir}/man1/lockersh.1*
%doc %{_mandir}/man1/pidstat.1*
%doc %{_mandir}/man1/pidstatd.1*
%doc %{_mandir}/man1/pidwatch.1*
%doc %{_mandir}/man1/uriexec.1*
%doc %{_mandir}/man3/IPC::Locker.3pm*
%doc %{_mandir}/man3/IPC::Locker::*.3pm*
%doc %{_mandir}/man3/IPC::PidStat.3pm*
%doc %{_mandir}/man3/IPC::PidStat::*.3pm*
%{_bindir}/lockerd
%{_bindir}/lockersh
%{_bindir}/pidstat
%{_bindir}/pidstatd
%{_bindir}/pidwatch
%{_bindir}/uriexec
%dir %{perl_vendorlib}/IPC/
%{perl_vendorlib}/IPC/Locker/
%{perl_vendorlib}/IPC/Locker.pm
%{perl_vendorlib}/IPC/PidStat/
%{perl_vendorlib}/IPC/PidStat.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.484-1
- Updated to version 1.484.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 1.483-1
- Updated to release 1.483.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.481-1
- Updated to release 1.481.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.472-1
- Updated to release 1.472.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.470-1
- Updated to release 1.470.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.463-1
- Updated to release 1.463.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.452-1
- Updated to release 1.452.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.451-1
- Updated to release 1.451.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.440-1
- Updated to release 1.440.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.434-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.434-1
- Updated to release 1.434.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.424-1
- Updated to release 1.424.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.433-1
- Initial package.
