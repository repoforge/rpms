# $Id: $
# Authority: dries
# Upstream: Daniel Stodle <daniels$stud,cs,uit,no>

Summary: Reliably tunnel TCP connections over ICMP packets
Name: ptunnel
Version: 0.52
Release: 1
License: BSD
Group: Applications/Internet
URL: http://www.cs.uit.no/~daniels/PingTunnel/index.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cs.uit.no/~daniels/PingTunnel/PingTunnel.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap

%description
Ping Tunnel is a tool for reliably tunneling TCP connections over ICMP echo
request and reply packets (commonly known as ping requests and replies). It
is useful for evading firewalls that, for whatever reason, prevent outgoing
TCP connections, but allow in- and outgoing ICMP packets. The tunnel works
by having a proxy run on a machine ping-able from the inside of the
firewall, with the client running on the local machine from which TCP access
is required.

%prep
%setup -n PingTunnel

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README web
%{_bindir}/ptunnel

%changelog
* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52 (Makefile patch applied by author).

* Sun Jan 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Initial package.
