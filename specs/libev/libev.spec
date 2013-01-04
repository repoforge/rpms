# $Id$
# Authority: shuff
# Upstream: Marc Lehmann <schmorpforge$schmorp,de>
# ExcludeDist: el2 rh7 rh9 el3 el4

Summary: High-performance event loop library
Name: libev
Version: 4.11
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://software.schmorp.de/pkg/libev/

Source: http://dist.schmorp.de/libev/libev-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Features include child/pid watchers, periodic timers based on wallclock
(absolute) time (in addition to timers using relative timeouts), as well as
epoll/kqueue/event ports/inotify/eventfd/signalfd support, fast timer
management, time jump detection and correction, and ease-of-use.

It can be used as a libevent replacement using its emulation API or directly
embedded into your programs without the need for complex configuration support.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Conflicts: libevent-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static --disable-dependency-tracking
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
%doc Changes LICENSE README
%{_libdir}/libev.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.gz
%{_includedir}/*.h
%{_libdir}/libev.so
%exclude %{_libdir}/libev.la

%changelog
* Fri Jan 04 2012 Steve Huff <shuff@vecna.org> - 4.11-1
- Initial package.
