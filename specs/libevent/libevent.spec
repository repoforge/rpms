# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>

Summary: Abstract asynchronous event notification library
Name: libevent
Version: 1.1a
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://monkey.org/~provos/libevent/

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
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/libevent-%{version}.so.*

%files devel
%defattr(-, root, root, 0755)
%doc sample/
%{_includedir}/event.h
%{_libdir}/libevent.a
%{_libdir}/libevent.so
%exclude %{_libdir}/libevent.la
%{_mandir}/man3/event.3*


%changelog
* Wed Jan 11 2006 Matthias Saou <http://freshrpms.net/> 1.1a-1
- Update to 1.1a.
- Clean up spec file, as make install now works properly, and PIC too.

* Fri May 06 2005 Dag Wieers <dag@wieers.com> - 1.0e-1
- Updated to release 1.0e.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 1.0b-1
- Updated to release 1.0b.

* Thu Jan 20 2005 Dag Wieers <dag@wieers.com> - 1.0-2
- Added deprecated interface.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.7-0.a
- Initial package. (using DAR)

