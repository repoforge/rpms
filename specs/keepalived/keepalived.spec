# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

Summary: HA monitor built upon LVS, VRRP and services poller
Name: keepalived
Version: 1.1.6
Release: 0
License: GPL
Group: Applications/System
URL: http://keepalived.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://keepalived.sf.net/software/keepalived-%{version}.tar.gz
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

%build
%{?rh9:export CPPFLAGS="-I/usr/kerberos/include"}
%configure \
%{?rh9:--includedir="/usr/kerberos/include"}
%{__make} %{?_smp_flags}

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
#%config %{_initrddir}/*
%config(noreplace) %{_sysconfdir}/keepalived/
%config %{_sysconfdir}/init.d/*
%{_bindir}/*
%{_sbindir}/*

%changelog
* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 1.1.6-0
- Updated to release 1.1.6.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 1.1.5-0
- Updated to release 1.1.5.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Updated to release 1.1.4.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
