# $Id$
# Authority: dag
# Upstream: <evms-devel$lists,sf,net>

%define _sbindir /sbin
%define _libdir /lib

Summary: Enterprise Volume Management System utilities
Name: evms
Version: 2.3.3
Release: 1
License: GPL
Group: System Environment/Base
URL: http://evms.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/evms/evms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2.0, gtk+-devel >= 1.2.0, ncurses-devel

%description
This package contains the user-space tools needed to manage EVMS (Enterprise
Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel patched
with the most recent EVMS code. Please see the EVMS-HOWTO on the project web
page or in the source package for detailed instructions on patching your kernel
with EVMS and using the tools after installation.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install \
	DESTDIR="%{buildroot}"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog ChangeLog COPYING INSTALL* PLUGIN.IDS README* TERMINOLOGY
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/evms.conf*
%{_sbindir}/*
%{_libdir}/*.so*
%{_libdir}/evms/
%{_includedir}/evms/
%exclude %{_libdir}/*.a

%changelog
* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 2.3.3-1
- Updated to release 2.3.3.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 2.3.2-1
- Updated to release 2.3.2.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 2.2.2-0
- Updated to release 2.2.2.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.

* Tue Jul 01 2003 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Initial package. (using DAR)
