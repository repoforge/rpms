# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>

Summary: Abstract asynchronous event notification library
Name: libevent
Version: 0.8
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://monkey.org/~provos/libevent/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://monkey.org/~provos/libevent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.


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
	--enable-shared
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -fPIC"

### FIXME: configure should have the ability to specify for static or shared libraries
${CC:-%{__cc}} -Wl,-soname,libevent.so.0 -shared %{optflags} -fPIC -o libevent.so.0.0.7 *.o

%install
%{__rm} -rf %{buildroot}
%makeinstall

### FIXME: This should be part of the normal 'make install' procedure !
%{__install} -m0755 libevent.so.0.0.7 %{buildroot}%{_libdir}
%{__ln_s} -f libevent.so.0.0.7 %{buildroot}%{_libdir}/libevent.so
%{__ln_s} -f libevent.so.0.0.7 %{buildroot}%{_libdir}/libevent.so.0

%{__install} -m0755 event.h %{buildroot}%{_includedir}/libevent.h
%{__ln_s} -f libevent.h %{buildroot}%{_includedir}/event.h

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.7-0.a
- Initial package. (using DAR)

