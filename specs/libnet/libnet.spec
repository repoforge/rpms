# $Id$
# Authority: dag
# Upstream: Mike D. Schiffman <mike_schiffman$hotmail,com>

Summary: Routines to help with network packet contruction and handling
Name: libnet
Version: 1.1.2.1
Release: 2.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.packetfactory.net/projects/libnet/

Source: http://www.packetfactory.net/libnet/dist/libnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libnet is a high-level API (toolkit) allowing the application programmer to
construct and inject network packets. It provides a portable and simplified
interface for low-level network packet shaping, handling and injection.

Libnet hides much of the tedium of packet creation from the application
programmer such as multiplexing, buffer management, arcane packet header
information, byte-ordering, OS-dependent issues, and much more. Libnet
features portable packet creation interfaces at the IP layer and link layer,
as well as a host of supplementary and complementary functionality.

Using libnet, quick and simple packet assembly applications can be whipped up
with little effort. With a bit more time, more complex programs can be written
(Traceroute and ping were easily rewritten using libnet and libpcap).

%prep
%setup -n %{name}

%build
%{expand: %%define optflags %{optflags} -fPIC}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 libnet-config %{buildroot}%{_bindir}/libnet-config

%{__install} -d -m0755 %{buildroot}%{_mandir}/man3/
%{__install} -Dp -m0644 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/BUGS doc/CHANGELOG doc/CONTRIB doc/COPYING doc/DESIGN_NOTES
%doc doc/MIGRATION doc/PACKET* doc/PORTED doc/RAWSOCKET* doc/TODO doc/html/
%doc %{_mandir}/man3/*.3*
%{_bindir}/libnet-config
%{_includedir}/libnet/
%{_includedir}/libnet.h
%{_libdir}/libnet.a

%changelog
* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 1.1.2.1-2
- Added -fPIC to %%optflags.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 1.1.2.1-1
- Updated to 1.1.2.1.

* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Patch to build with gcc-3.3.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2. (using DAR)

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to 1.0.2a (1.1.0 does not work with some apps)

* Thu Aug 02 2001 Dag Wieers <dag@wieers.com> - 1.0.1
- Initial package.
