# $Id$
# Authority: dag
# Upstream: <tcpreplay-users$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Replay captured network traffic
Name: tcpreplay
Version: 3.3.0
Release: 1
License: BSD
Group: Applications/Internet
URL: http://tcpreplay.synfin.net/trac/

Source: http://dl.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: libnet >= 1.1.1
BuildRequires: libpcap >= 0.5, tcpdump
%{?_with_libpcapdevel:BuildRequires:libpcap-devel >= 0.5}

%description
Tcpreplay is a suite of tools to edit and replay captured network traffic.
The tcpreplay suite includes tcpprep to pre-process pcap files, tcprewrite a
pcap editor and tcpreplay to send packets.  Also included is tcpbridge which
is a user-space bridge and flowreplay, a client-side agent using pcap files
as the basis of connections.

%prep
%setup

%build
%configure \
    --enable-tcpreplay-edit
#   --enable-flowreplay
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"

#%{__install} -Dp -m0755 src/flowreplay %{buildroot}%{_bindir}/flowreplay
%{__install} -Dp -m0755 src/tcpbridge %{buildroot}%{_bindir}/tcpbridge
%{__install} -Dp -m0755 src/tcpprep %{buildroot}%{_bindir}/tcpprep
%{__install} -Dp -m0755 src/tcpreplay %{buildroot}%{_bindir}/tcpreplay
%{__install} -Dp -m0755 src/tcprewrite %{buildroot}%{_bindir}/tcprewrite

#%{__install} -Dp -m0644 src/flowreplay.1 %{buildroot}%{_mandir}/man1/flowreplay.1
%{__install} -Dp -m0644 src/tcpbridge.1 %{buildroot}%{_mandir}/man1/tcpbridge.1
%{__install} -Dp -m0644 src/tcpprep.1 %{buildroot}%{_mandir}/man1/tcpprep.1
%{__install} -Dp -m0644 src/tcpreplay.1 %{buildroot}%{_mandir}/man1/tcpreplay.1
%{__install} -Dp -m0644 src/tcprewrite.1 %{buildroot}%{_mandir}/man1/tcprewrite.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/CHANGELOG docs/CREDIT docs/HACKING docs/INSTALL docs/LICENSE
%doc docs/TODO README
#%doc %{_mandir}/man1/flowreplay.1*
%doc %{_mandir}/man1/tcpbridge.1*
%doc %{_mandir}/man1/tcpprep.1*
%doc %{_mandir}/man1/tcpreplay.1*
%doc %{_mandir}/man1/tcprewrite.1*
#%{_bindir}/flowreplay
%{_bindir}/tcpbridge
%{_bindir}/tcpprep
%{_bindir}/tcpreplay
%{_bindir}/tcprewrite

%changelog
* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 3.3.0-1
- Updated to release 3.3.0.

* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 3.2.5-1
- Updated to release 3.2.5.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 3.2.4-1
- Updated to release 3.2.4.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 3.2.3-1
- Updated to release 3.2.3.

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 3.2.2-1
- Updated to release 3.2.2.

* Fri Oct 26 2007 Dag Wieers <dag@wieers.com> - 3.2.1-1
- Updated to release 3.2.1.

* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Sat Jul 21 2007 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1.

* Fri Apr 20 2007 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Updated to release 3.0.0.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.3.5-1
- Updated to release 2.3.5.

* Sun Jun 05 2005 Dag Wieers <dag@wieers.com> - 2.3.4-1
- Updated to release 2.3.4.

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 2.3.3-1
- Updated to release 2.3.3.

* Mon Nov 08 2004 Dag Wieers <dag@wieers.com> - 2.3.2-1
- Updated to release 2.3.2.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Updated to release 2.3.1.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Updated to release 2.1.0.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 2.0.3-2
- Rebuild against libnet 1.1.2.1.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 1.4.5-0
- Updated to release 1.4.5.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 1.4.1-0
- Updated to release 1.4.1.

* Thu May 08 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0
- Updated to release 1.4.0.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Initial package. (using DAR)
