# $Id$
# Authority: dag

Summary: Low-level event loop management library
Name: liboop
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://liboop.org/

Source: http://download.ofb.net/liboop/liboop-1.0.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Liboop is a low-level event loop management library for POSIX-based operating
systems. It supports the development of modular, multiplexed applications
which may respond to events from several sources. It replaces the "select()
loop" and allows the registration of event handlers for file and network I/O,
timers and signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost any
application.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL
%{_libdir}/liboop.so.*
%{_libdir}/liboop-*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/oop.h
%{_includedir}/oop-*.h
%{_libdir}/liboop.so
%{_libdir}/liboop-*.so
%{_libdir}/pkgconfig/liboop.pc
%{_libdir}/pkgconfig/liboop-glib2.pc
%exclude %{_libdir}/liboop.a
%exclude %{_libdir}/liboop.la
%exclude %{_libdir}/liboop-*.a
%exclude %{_libdir}/liboop-*.la

%changelog
* Fri Aug 17 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
