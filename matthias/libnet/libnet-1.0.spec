# Authority: dag

%define rname libnet
%define rversion 1.0.2a

Summary: Routines to help with network packet construction and handling.
#Name: libnet10
Name: libnet
Version: 1.0.2
Release: 2
License: GPL
Group: Development/Libraries
URL: http://www.packetfactory.net/projects/libnet/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.packetfactory.net/libnet/dist/%{rname}-%{rversion}.tar.gz
Patch: libnet-1.0.2a-gcc33.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%setup -n Libnet-%{rversion}
%patch0 -b .gcc33

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BIN_PREFIX="%{buildroot}%{_bindir}" \
	INC_PREFIX="%{buildroot}%{_includedir}/" \
	LIB_PREFIX="%{buildroot}%{_libdir}" \
	MAN_PREFIX="%{buildroot}%{_mandir}/man3"
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 libnet-config %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/libnet.h
%{_includedir}/libnet/
#%{_libdir}/libpwrite

%changelog
* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Patch to build with gcc-3.3.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2. (using DAR)

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to 1.0.2a (1.1.0 does not work with some apps)

* Thu Aug 02 2001 Dag Wieers <dag@wieers.com> - 1.0.1
- Initial package.
