# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Locker

Summary: Distributed lock handler
Name: perl-IPC-Locker
Version: 1.463
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Locker/

Source: http://search.cpan.org/CPAN/authors/id/W/WS/WSNYDER/IPC-Locker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/lockerd
%{_bindir}/pidstatd
%{_bindir}/pidwatch
%{_bindir}/lockersh
%{perl_vendorlib}/IPC/Locker.pm
%{perl_vendorlib}/IPC/Locker
%{perl_vendorlib}/IPC/PidStat.pm
%{perl_vendorlib}/IPC/PidStat

%changelog
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
