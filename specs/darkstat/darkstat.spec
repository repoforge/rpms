# $Id$
# Authority: dag
# Upstream: Emil Mikulic <www-28ab$dmr,ath,cx>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Network traffic analyzer
Name: darkstat
Version: 3.0.711
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://dmr.ath.cx/net/darkstat/

Source: http://dmr.ath.cx/net/darkstat/darkstat-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%setup

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
%doc AUTHORS COPYING* INSTALL LICENSE NEWS README THANKS
%doc %{_mandir}/man1/darkstat.1*
%{_sbindir}/darkstat

%changelog
* Sun Aug 10 2008 Dag Wieers <dag@wieers.com> - 3.0.711-1 
- Updated to release 3.0.711.

* Mon Jun 09 2008 Dag Wieers <dag@wieers.com> - 3.0.708-1
- Updated to release 3.0.708.

* Tue Oct 02 2007 Dag Wieers <dag@wieers.com> - 3.0.707-1
- Updated to release 3.0.707.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 3.0.619-1
- Updated to release 3.0.619.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 3.0.540-1
- Updated to release 3.0.540.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 3.0.471-1
- Updated to release 3.0.471.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.6-1
- Initial package. (using DAR)
