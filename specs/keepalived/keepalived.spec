# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}
%{!?kernel:%define kernel %(rpm --quiet -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

Summary: HA monitor built upon LVS, VRRP and services poller
Name: keepalived
Version: 1.1.7
Release: 2
License: GPL
Group: Applications/System
URL: http://keepalived.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.keepalived.org/software/keepalived-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
The main goal of the keepalived project is to add a strong & robust
keepalive facility to the Linux Virtual Server project. This project
is written in C with multilayer TCP/IP stack checks.

Keepalived implements a framework based on three family checks: Layer3,
Layer4 & Layer5. This framework gives the daemon the ability of checking
a LVS server pool states. When one of the server of the LVS server pool
is down, keepalived informs the linux kernel via a setsockopt call to
remove this server entrie from the LVS topology.

In addition keepalived implements a VRRPv2 stack to handle director
failover. So in short keepalived is a userspace daemon for LVS cluster
nodes healthchecks and LVS directors failover.

%prep
%setup

%{__perl} -pi.orig -e 's|\$\(prefix\)/man|\$(mandir)|' Makefile.in */Makefile.in

%build
%{?el3:export CPPFLAGS="-I/usr/kerberos/include"}
%{?rh9:export CPPFLAGS="-I/usr/kerberos/include"}
%configure \
%{?el3:--includedir="/usr/kerberos/include"} \
%{?rh9:--includedir="/usr/kerberos/include"} \
	--with-kernel-dir="/lib/modules/%{kernel}/build"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/chkconfig --add keepalived

%preun
if [ $1 -eq 0 ]; then
	/sbin/service keepalived stop &>/dev/null || :
	/sbin/chkconfig --del keepalived
fi

%postun
/sbin/service keepalived condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR ChangeLog CONTRIBUTORS COPYING README TODO doc/
%doc %{_mandir}/man?/*
#%config %{_initrddir}/*
%config(noreplace) %{_sysconfdir}/keepalived/
%config %{_sysconfdir}/init.d/keepalived
%{_bindir}/genhash
%{_sbindir}/keepalived

%changelog
* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.1.7-2
- Fixes to build with kernel IPVS support. (Tim Verhoeven)

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.1.7-1
- Updated to release 1.1.7. (Mathieu Lubrano)

* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 1.1.6-0
- Updated to release 1.1.6.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 1.1.5-0
- Updated to release 1.1.5.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Updated to release 1.1.4.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
