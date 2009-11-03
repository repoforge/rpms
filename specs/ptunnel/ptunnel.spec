# $Id: $
# Authority: dries
# Upstream: Daniel Stodle <daniels$stud,cs,uit,no>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define real_name PingTunnel

Summary: Reliably tunnel TCP connections over ICMP packets
Name: ptunnel
Version: 0.70
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.cs.uit.no/~daniels/PingTunnel/index.html

Source: http://www.cs.uit.no/~daniels/PingTunnel/PingTunnel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Ping Tunnel is a tool for reliably tunneling TCP connections over ICMP echo
request and reply packets (commonly known as ping requests and replies). It
is useful for evading firewalls that, for whatever reason, prevent outgoing
TCP connections, but allow in- and outgoing ICMP packets. The tunnel works
by having a proxy run on a machine ping-able from the inside of the
firewall, with the client running on the local machine from which TCP access
is required.

%prep
%setup -n %{real_name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall mandir="%{buildroot}%{_mandir}/man8"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README web/
%doc %{_mandir}/man8/ptunnel.8*
%{_bindir}/ptunnel

%changelog
* Wed Jan 21 2009 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.54-1
- Updated to release 0.54.

* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52 (Makefile patch applied by author).

* Sun Jan 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Initial package.
