# $Id$
# Authority: shuff
# Upstream: Niels Provos <provos$citi,umich,edu>

### EL5.4 ships with libevent 1.1a-3.2.1
### EL5.5 ships with libevent 1.4.13-1
# ExclusiveDist: el5

%define real_name libevent
%define real_version 1.1a

Summary: Abstract asynchronous event notification library - backwards compatibility
Name: compat-libevent11a
Version: 3.2.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://monkey.org/~provos/libevent/

Source: http://www.monkey.org/~provos/libevent-1.1a.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

# if you have the real libevent-1.1a, you don't need this
Conflicts: libevent = %{real_version}

%description
The libevent API provides a mechanism to execute a callback function when a
specific event occurs on a file descriptor or after a timeout has been reached.
libevent is meant to replace the asynchronous event loop found in event driven
network servers. An application just needs to call event_dispatch() and can
then add or remove events dynamically without having to change the event loop.

This package provides backwards compatibility for applications linked against
libevent-1.1a-3.2.1.

%prep
%setup -n %{real_name}-%{real_version}

%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/libevent-%{real_version}.so.*
%exclude %{_mandir}/man?/*
%exclude %{_includedir}/*
%exclude %{_libdir}/libevent.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Thu Apr 08 2010 Steve Huff <shuff@vecna.org> - 3.2.1-1
- Initial package.
