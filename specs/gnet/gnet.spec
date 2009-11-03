# $Id$
# Authority: rudolf
# Upstream: David Helder <dhelder$umich,edu>

Summary: Gnet, a network library
Name: gnet
Version: 1.1.9
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnetlibrary.org/

Source: http://www.gnetlibrary.org/src/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: glib >= 1.2.10, glib-devel

%description
Gnet is a simple network library. It is writen in C, object-oriented,
and built upon GLib. It is intended to be small, fast, easy-to-use,
and easy to port.

Features:
  * TCP "client" and "server" sockets
  * UDP and IP Multicast
  * Internet address abstraction
  * Asynchronous socket IO
  * Asynchronous DNS lookup
  * Byte packing and unpacking
  * URLs (Experimental)
  * Server and Conn objects (Experimental)

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--with-html-dir="%{buildroot}%{_docdir}/libgnet1.1-dev/"
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
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_libdir}/libgnet.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%doc %{_mandir}/man1/gnet-config.1*
%doc %{_docdir}/libgnet1.1-dev/
%{_bindir}/gnet-config
%{_datadir}/aclocal/gnet.m4
%{_includedir}/gnet/
%{_libdir}/gnet/
%{_libdir}/libgnet.a
%exclude %{_libdir}/libgnet.la
%{_libdir}/libgnet.so
%{_libdir}/pkgconfig/gnet.pc

%changelog
* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 1.1.9-0
- Updated to release 1.1.9.

* Sun Jun 22 2003 Dag Wieers <dag@wieers.com> - 1.1.8-2
- Minor cleanup.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 1.1.8-1
- Fixed the --program-prefix problem.

* Mon Jan 06 2003 Dag Wieers <dag@wieers.com> - 1.1.8-0
- Updated to release 1.1.8. (using DAR)

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 1.1.7-0
- Updated to release 1.1.7.
- Cleaned up SPEC file.

* Thu Oct 26 2000 Benjamin Kahn <xkahn@helixcode.com>
- Added missing file in lib/gnet

* Mon Feb 28 2000 David Helder <dhelder@umich.edu>
- Updated for version 1.0

* Sat Jan 15 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- Moved lib*.so and lib*a to the devel package
- Creation of a gnet.spec.in for autoconf process

* Wed Jan 14 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- HTML documentation has been move to /usr/doc/gnet-{version}/html

* Thu Jan 13 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- First try at an RPM
