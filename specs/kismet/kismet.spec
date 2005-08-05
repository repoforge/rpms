# $Id$
# Authority: dag
# Upstream: <wireless$kismetwireless,net>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_gpsmap 1}
%{?el2:%define _without_gpsmap 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define real_version 2005-07-R1

Summary: 802.11 (wireless) network sniffer and network dissector
Name: kismet
Version: 3.0.1
Release: 3.200507r1
License: GPL
Group: Applications/Internet
URL: http://www.kismetwireless.net/

Source: http://www.kismetwireless.net/code/kismet-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ImageMagick-devel, ncurses-devel, autoconf, flex, gcc-c++
BuildRequires: zlib-devel, expat-devel, byacc, gmp-devel, wget
BuildRequires: libtiff-devel, libjpeg-devel, bzip2-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Kismet is an 802.11 (wireless) network sniffer and network dissector.
It is capable of sniffing using most wireless cards, automatic network
IP block detection via UDP, ARP, and DHCP packets, Cisco equipment lists
via Cisco Discovery Protocol, weak cryptographic packet logging, and
Ethereal and tcpdump compatible packet dump files.

%package -n gpsmap
Summary: Tool to plot networks based on kismet files
Group: Applications/Internet

%description -n gpsmap
gpsmap allows to plot networks and estimated network ranges detected by
kismet on downloaded maps or user supplied image files.

%prep
%setup -n %{name}-%{real_version}

#### FIXME: Get rid of the ownership changes (RH9)
%{__perl} -pi.orig -e '
		s|-o \$\(INSTUSR\) -g \$\(INSTGRP\) ||g;
		s|-o \$\(INSTUSR\) -g \$\(MANGRP\) ||g;
	' Makefile.in

%build
%configure
#	--enable-syspcap
%{__make} %{?_smp_mflags} dep all

%install
%{__rm} -rf %{buildroot}
%makeinstall rpm \
	ETC="%{buildroot}%{_sysconfdir}" \
	BIN="%{buildroot}%{_bindir}" \
	SHARE="%{buildroot}%{_datadir}/kismet/" \
	MAN="%{buildroot}%{_mandir}" \
	WAV="%{buildroot}%{_datadir}/kismet/wav/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG GPL README TODO docs/DEVEL.* docs/README*
%doc %{_mandir}/man1/kismet*.1*
%doc %{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/kismet*
%{_datadir}/kismet/

%if %{!?_without_gpsmap:1}0
%files -n gpsmap
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/gpsmap.1*
%{_bindir}/gpsmap*
%endif

%changelog
* Mon Jul 25 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200507r1
- Updated to release 2005-07-R1.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200506r1
- Updated to release 2005-06-R1.

* Sun Apr 03 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200504r1
- Updated to release 2005-04-R1.

* Thu Feb 24 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200501r1
- Revert config directory to /etc.
- Updated to release 2005-01-R1.

* Thu Dec 23 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1.200410r1
- Updated to release 2004-10-R1.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1.200404r1
- Updated to release 2004-04-R1.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1-feb.04.01.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0
- Updated to release 3.0.0.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 2.8.1-0
- Initial package. (using DAR)
