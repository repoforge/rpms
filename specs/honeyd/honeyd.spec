# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

%define real_version 0.8b

Summary: Honeypot daemon
Name: honeyd
Version: 0.8
Release: 1.b
License: BSD
Group: Applications/Internet
URL: http://www.citi.umich.edu/u/provos/honeyd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.citi.umich.edu/u/provos/honeyd/honeyd-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel, flex, libpcap

%description
Honeyd is a small daemon that creates virtual hosts on a network.
The hosts can be configured to run arbitrary services, and their
TCP personality can be adapted so that they appear to be running
certain versions of operating systems. Honeyd enables a single
host to claim multiple addresses on a LAN for network simulation.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 honeyd %{buildroot}%{_sbindir}/honeyd
%{__install} -D -m0644 honeyd.8 %{buildroot}%{_mandir}/man8/honeyd.8

%{__install} -d -m0755 %{buildroot}%{_datadir}/honeyd/
%{__install} -m0644 xprobe2.conf nmap.assoc nmap.prints config.sample %{buildroot}%{_datadir}/honeyd/

%{__install} -d -m0755 %{buildroot}%{_libdir}/honeyd/
%{__install} -m0755 libhoneyd.so honeyd_overload.lo atomicio.lo fdpass.lo %{buildroot}%{_libdir}/honeyd/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO config.sample nmap.prints scripts/
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/honeyd/
%{_datadir}/honeyd/

%changelog
* Tue Apr 20 2004 Dag Wieers <dag@wieers.com> - 0.8-1.b
- Updated to release 0.8b.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
