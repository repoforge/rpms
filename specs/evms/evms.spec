# $Id$
# Authority: dag
# Upstream: <evms-devel$lists,sf,net>

%define _sbindir /sbin
%define _libdir /lib

Summary: Enterprise Volume Management System utilities
Name: evms
Version: 2.5.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://evms.sourceforge.net/

Source: http://dl.sf.net/evms/evms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2.0, gtk+-devel >= 1.2.0, ncurses-devel
BuildRequires: gettext

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
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog ChangeLog COPYING INSTALL* PLUGIN.IDS README* TERMINOLOGY
%doc %{_mandir}/man8/evms*.8*
%config(noreplace) %{_sysconfdir}/evms.conf*
%{_sbindir}/evms*
%{_libdir}/libevms*.so*
%{_libdir}/evms/
%{_includedir}/evms/
%exclude %{_libdir}/libevms.a

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.3-1
- Updated to release 2.5.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.2-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 17 2005 Dag Wieers <dag@wieers.com> - 2.5.2-1
- Updated to release 2.5.2.

* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Updated to release 2.4.1.

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
