# $Id$

# Authority: dag
# Upstream: Jordan Ritter <jpr5@darkridge.com>

Summary: Realtime network grep tool
Name: ngrep
Version: 1.42
Release: 1
License: GPL
Group: Applications/Internet
URL: http://ngrep.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ngrep/ngrep-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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

### FIXME: Let Makefile use standard autotools directories. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|^(BINDIR).+$|$1=\$(bindir)|g;
		s|^(MANDIR).+$|$1=\$(mandir)/man8|g;
	' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES CREDITS INSTALL LICENSE README* TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Mon Aug 11 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Updated to release 1.41.

* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 1.40.1-0
- Initial package. (using DAR)
