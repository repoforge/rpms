# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>

Summary: Honeypot daemon
Name: honeyd
Version: 1.0
Release: 2
License: BSD
Group: Applications/Internet
URL: http://www.citi.umich.edu/u/provos/honeyd/

Source: http://www.citi.umich.edu/u/provos/honeyd/honeyd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel, flex, libpcap, libdnet, automake, autoconf
BuildRequires: readline-devel, bison, libdnet-devel

%description
Honeyd is a small daemon that creates virtual hosts on a network.
The hosts can be configured to run arbitrary services, and their
TCP personality can be adapted so that they appear to be running
certain versions of operating systems. Honeyd enables a single
host to claim multiple addresses on a LAN for network simulation.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure
%{__perl} -pi.orig -e 's| (\$\(honeyddatadir\))| \$(DESTDIR)$1|g' Makefile.in

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
%doc LICENSE README TODO config.sample nmap.prints scripts/
%doc %{_mandir}/man1/honeydctl.1*
%doc %{_mandir}/man8/honeyd.8*
%{_bindir}/honeyd
%{_bindir}/honeydctl
%{_datadir}/honeyd/
%{_includedir}/honeyd/
%{_libdir}/honeyd/

%changelog
* Sun Apr 10 2005 Dag Wieers <dag@wieers.com> - 1.0-2
- Added pf.os, use %%{__make} install. (Mario Pascucci)

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Tue Apr 20 2004 Dag Wieers <dag@wieers.com> - 0.8-1.b
- Updated to release 0.8b.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
