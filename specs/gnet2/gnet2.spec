# $Id$
# Authority: dag
# Upstream: David Helder <dhelder$umich,edu>

Summary: Simple network library
Name: gnet2
Version: 2.0.7
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnetlibrary.org/

Source: http://www.gnetlibrary.org/src/gnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: glib2-devel, pkgconfig >= 0.9, libtool, gcc-c++

%description
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon GLib. It is intended to be small, fast, easy-to-use,
and easy to port.

Features include :
  TCP "client" and "server" sockets,
  UDP and IP Multicast sockets,
  High-level TCP connection and server objects,
  Asynchronous socket IO,
  Internet address abstraction,
  Asynchronous DNS lookup,
  IPv4 and IPv6 support,
  Byte packing and unpacking,
  URI parsing,
  SHA and MD5 hashes,
  Base64 encoding and decoding and
  SOCKS support

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n gnet-%{version}

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--with-html-dir="%{buildroot}%{_docdir}/libgnet2.0-dev/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libgnet-2.0.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%doc %{_docdir}/libgnet2.0-dev/
%{_datadir}/aclocal/gnet-2.0.m4
%{_includedir}/gnet-2.0/
%{_libdir}/gnet-2.0/
%{_libdir}/libgnet-2.0.a
%exclude %{_libdir}/libgnet-2.0.la
%{_libdir}/libgnet-2.0.so
%{_libdir}/pkgconfig/gnet-2.0.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.7-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 2.0.7-1
- Updated to release 2.0.7.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Initial package. (using DAR)
