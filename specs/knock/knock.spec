# $Id$
# Authority: dag
# Upstream: Judd Vinet <jvinet$zeroflux,org>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?el6:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Port-knocking server
Name: knock
Version: 0.5
Release: 3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.zeroflux.org/knock/

Source: http://www.zeroflux.org/knock/files/knock-%{version}.tar.gz
%{?el6:Patch0: knock-el6-compilation-error.patch}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
knockd is a port-knock server. It listens to all traffic on an ethernet
interface, looking for special "knock" sequences of port-hits. A client
makes these port-hits by sending a TCP (or UDP) packet to a port on the
server. This port need not be open -- since knockd listens at the link-
layer level, it sees all traffic even if it's destined for a closed port.

When the server detects a specific sequence of port-hits, it runs a
command defined in its configuration file. This can be used to open up
holes in a firewall for quick access.

%prep
%setup
%{?el6:%patch0 -p1}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING  README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/knockd.conf
%{_bindir}/knock
%{_sbindir}/knockd

%changelog
* Thu Jan 03 2013 Jan Horacek <jahor@jhr.cz> - 0.5-3
- patch for building on EL6

* Fri Dec 16 2011 Jan Horacek <jahor@jhr.cz> - 0.5-2
- EL6 has libpcap-devel

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
