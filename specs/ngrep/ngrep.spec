# $Id$
# Authority: dag
# Upstream: Jordan Ritter <jpr5$darkridge,com>

%define _default_patch_fuzz 2

%define _include_pcap %{_includedir}/pcap

%{!?dtag:%define _with_libpcapdevel 1}
%{?el6:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?el5:%define _include_pcap %{_includedir}}
%{?el4:%define _include_pcap %{_includedir}}
%{?el3:%define _include_pcap %{_includedir}}
%{?el2:%define _include_pcap %{_includedir}}

Summary: Realtime network grep tool
Name: ngrep
Version: 1.45
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ngrep.sourceforge.net/

Source: http://dl.sf.net/ngrep/ngrep-%{version}.tar.bz2
Patch0: ngrep-1.45-system-pcre.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
BuildRequires: pcre-devel
%{?_with_libpcapdevel:BuildRequires: libpcap-devel}

%description
ngrep is grep command that works on realtime network data.

ngrep strives to provide most of GNU grep's common features, applying
them to the network layer. ngrep is a pcap-aware tool that will allow
you to specify extended regular or hexadecimal expressions to match
against data payloads of packets. It currently recognizes TCP, UDP
and ICMP across Ethernet, PPP, SLIP, FDDI, Token Ring and null
interfaces, and understands bpf filter logic in the same fashion as
more common packet sniffing tools, such as tcpdump and snoop.

%prep
%setup
%patch0 -p1

%build
export EXTRA_INCLUDES="$(pcre-config --cflags)"
export EXTRA_LIBS="$(pcre-config --libs)"
%configure \
    --enable-ipv6 \
    --enable-pcre \
    --with-pcap-includes="%{_include_pcap}"
%{__make} %{?_smp_mflags} STRIPFLAG=

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" BINDIR_INSTALL="%{_sbindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt doc/*.txt scripts/
%doc %{_mandir}/man8/ngrep.8*
%{_sbindir}/ngrep

%changelog
* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.45-2
- Included patch from Fedora.
- Fix build on RHEL6 (include_pcap).

* Thu Nov 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.45-1
- Updated to release 1.45.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 1.44-1
- Updated to release 1.44.

* Wed Feb 23 2005 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Mon Aug 11 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Updated to release 1.41.

* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 1.40.1-0
- Initial package. (using DAR)
