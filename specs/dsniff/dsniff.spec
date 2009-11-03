# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define _libdir %{_sysconfdir}

Summary: Tools for network auditing and penetration testing
Name: dsniff
Version: 2.4
Release: 0.1.b1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/dsniff/

Source: http://www.monkey.org/~dugsong/dsniff/beta/dsniff-%{version}b1.tar.gz
Patch0: dsniff-2.4-time_h.patch
Patch1: dsniff-2.4-mailsnarf_corrupt.patch
Patch2: dsniff-2.4-pcap_read_dump.patch
Patch3: dsniff-2.4-multiple_intf.patch
Patch4: dsniff-2.4-amd64_fix.patch
Patch5: dsniff-2.4-urlsnarf_zeropad.patch
Patch6: dsniff-2.4-libnet_11.patch
Patch7: dsniff-2.4-checksum.patch
Patch8: dsniff-2.4-openssl_098.patch
Patch9: dsniff-2.4-sshcrypto.patch
Patch10: dsniff-2.4-sysconf_clocks.patch
Patch11: dsniff-2.4-urlsnarf_escape.patch
Patch12: dsniff-2.4-string_header.patch
Patch13: dsniff-2.4-arpa_inet_header.patch
Patch14: dsniff-2.4-pop_with_version.patch
Patch15: dsniff-2.4-obsolete_time.patch
Patch16: dsniff-2.4-checksum_libnids.patch
Patch17: dsniff-2.4-fedora_dirs.patch
Patch18: dsniff-2.4-glib2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: db4-devel
BuildRequires: glib2-devel
BuildRequires: libnet
BuildRequires: libnids >= 1.16
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}
BuildRequires: openssl-devel >= 0.9.5a

%description
dsniff is a collection of tools for network auditing and penetration testing.
Dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf and webspy allow to passively
monitor a network for interesting data (passwords, e-mail, files). Arpspoof,
dnsspoof and macof facilitate the interception of network traffic normally
unavailable to an attacker (e.g, due to layer-2 switching). Sshmitm and
webmitm implement active monkey-in-the-middle attacks against redirected SSH
and HTTPS sessions by exploiting weak bindings in ad-hoc PKI.

%prep
%setup
%patch0 -p1 -b .time_h
%patch1 -p1 -b .mailsnarf
%patch2 -p1 -b .pcap_dump
%patch3 -p1 -b .multiple_intf
%patch4 -p1 -b .amd64_fix
%patch5 -p1 -b .urlsnarf_zeropad
%patch6 -p1 -b .libnet_11
%patch7 -p1 -b .checksum
%patch8 -p1 -b .openssl_098
%patch9 -p1 -b .sshcrypto
%{?el5:%patch10 -p1 -b .sysconf_clocks}
%patch11 -p1 -b .urlsnarf_escape
%patch12 -p1 -b .string_header
%patch13 -p1 -b .arpa_inet_header
%patch14 -p1 -b .pop_with_version
%patch15 -p1 -b .obsolete_time
%patch16 -p1 -b .checksum_libnids
%patch17 -p1 -b .fedora_dirs
%patch18 -p1 -b .glib2

### FIXME: Make it build for RH9 and RHEL3
%{?el3:%{__perl} -pi.orig -e 's|^(INCS	=) |$1 -I/usr/kerberos/include |' Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^(INCS	=) |$1 -I/usr/kerberos/include |' Makefile.in}

%{__perl} -pi.orig -e 's|/usr/local/lib/|%{_sysconfdir}/|' *.8 pathnames.h

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install install_prefix="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO
%doc %{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/dsniff/
%{_sbindir}/*

%changelog
* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> -  2.4-0.1.b1
- Added patches from Fedora.

* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 2.4-0.b1
- Updated to release 2.4b1.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 2.3-0
- Initial package. (using DAR)
