# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>


%{!?dtag:%define _with_libpcapdevel 1}
%{?fc7:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Honeypot daemon
Name: honeyd
Version: 1.5c
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.honeyd.org/

Source: http://www.citi.umich.edu/u/provos/honeyd/honeyd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, flex, bison, libdnet-devel, automake, autoconf
BuildRequires: libpcap, libdnet-devel, libdnsres-devel, libevent-devel
BuildRequires: python-devel >= 2.4
BuildRequires: pcre-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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
%{__install} -d %{buildroot}%{_datadir}/honeyd
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README config.sample nmap.prints scripts/
%doc %{_mandir}/man1/honeydctl.1*
%doc %{_mandir}/man8/honeyd.8*
%{_bindir}/honeydstats
%{_bindir}/honeyd
%{_bindir}/honeydctl
%{_datadir}/honeyd/
%{_includedir}/honeyd/
%{_libdir}/honeyd/

%changelog
* Tue May 29 2007 Dag Wieers <dag@wieers.com> - 1.5c-1
- Updated to release 1.5c.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.5b-5
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 1.5b-4
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 1.5b-3
- Rebuild against libevent-1.3b.

* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 1.5b-2
- Rebuild against libevent-1.1b.

* Sat Aug 19 2006 Dag Wieers <dag@wieers.com> - 1.5b-1
- Updated to release 1.5b.

* Tue Feb 21 2006 Dag Wieers <dag@wieers.com> - 1.5a-1
- Updated to release 1.5a.

* Sun Apr 10 2005 Dag Wieers <dag@wieers.com> - 1.0-2
- Added pf.os, use %%{__make} install. (Mario Pascucci)

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Tue Apr 20 2004 Dag Wieers <dag@wieers.com> - 0.8-1.b
- Updated to release 0.8b.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
