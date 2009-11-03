# $Id$

# Authority: dag
# Upstream: Blake Matheny <bmatheny$purdue,edu>

Summary: Change Password Utility
Name: cpu
Version: 1.4.3
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://cpu.sourceforge.net/

Source: http://dl.sf.net/cpu/cpu-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: openldap-devel

%description
CPU is an LDAP user management tool written in C and loosely based on
FreeBSD's pw(8). The goal of CPU is to be a suitable replacement of
the useradd/usermod/userdel utilities for administrators using an LDAP
backend and wishing to have a suite of command line tools for doing
the administration.

%prep
%setup

### FIXME: Change datadir to datadir/doc. (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(datadir\)|\$(docdir)|g' doc/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	docdir="../rpm-doc"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.a \
		%{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README rpm-doc/* TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_sbindir}/*
%{_libdir}/*.so*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.3-0.2
- Rebuild for Fedora Core 5.

* Mon Jan 12 2004 Dag Wieers <dag@wieers.com> - 1.4.3-0
- Updated to release 1.4.3.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0.a
- Updated to release 1.4.0a.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.3.100-0
- Updated to release 1.3.100.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.3.99-0.a
- Initial package. (using DAR)
