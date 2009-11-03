# $Id$
# Authority: dag
# Upstream: Rafal Wojtczuk <nergal$icm,edu,pl>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Implementation of an E-component of Network Intrusion Detection System
Name: libnids
Version: 1.21
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libnids.sourceforge.net/

Source: http://dl.sf.net/libnids/libnids-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet, libpcap, pkgconfig, glib2-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.0.x. Libnids
offers IP defragmentation, TCP stream assembly and TCP port scan
detection.

Using libnids, one has got a convenient access to data carried by a
TCP stream, no matter how artfully obscured by an attacker.

%prep
%setup

%build
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING MISC README doc/ samples/
%doc %{_mandir}/man3/libnids.3*
%{_libdir}/libnids.a
%{_includedir}/nids.h

%changelog
* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Mon Aug 09 2004 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.18-0
- Updated to release 1.18.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 1.16-0
- Initial package. (using DAR)
