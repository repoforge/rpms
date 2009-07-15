# $Id$
# Authority: dag

Summary: Configuration file abstraction library
Name: libmcs
Version: 0.7.1
Release: 1
License: BSD
Group: Applications/System
URL: http://www.atheme.org/projects/mcs.shtml

Source: http://distfiles.atheme.org/libmcs-%{version}.tbz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: GConf2-devel
BuildRequires: libmowgli-devel

Obsoletes: mcs <= %{version}-%{release}
Provides: mcs = %{version}-%{release}
Obsoletes: mcs-libs <= %{version}-%{release}
Provides: mcs-libs = %{version}-%{release}

%description
mcs is a library and set of userland tools which abstract the storage of
configuration settings away from userland applications.

It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.

There have been other projects like this before (such as GConf), but unlike
those projects, mcs strictly handles abstraction. It does not impose any
specific data storage requirement, nor is it tied to any desktop environment or
software suite.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Obsoletes: mcs-devel <= %{version}-%{release}
Provides: mcs-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
echo -n "gconf" >mcs-backend

%build
source "/etc/profile.d/qt.sh"
%configure \
    --disable-dependency-tracking \
    --enable-gconf
%{__make} %{?_smp_mflags} PLUGIN_CPPFLAGS="-I$QTDIR/include -I%{_includedir}/kde/"

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 mcs-backend %{buildroot}%{_sysconfdir}/mcs-backend

#%{__rm} %{buildroot}%{_includedir}/libmcs/mcs_config.h
#%{__perl} -pi -e 's|^#include <libmcs/mcs_config.h||' %{buildroot}%{_includedir}/libmcs/mcs.h

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING Mercurial-Access README TODO
%config(noreplace) %{_sysconfdir}/mcs-backend
%{_bindir}/mcs-getconfval
%{_bindir}/mcs-info
%{_bindir}/mcs-query-backends
%{_bindir}/mcs-setconfval
%{_bindir}/mcs-walk-config
%{_libdir}/libmcs.so.*
%{_libdir}/mcs/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmcs/
%{_libdir}/libmcs.so
%{_libdir}/pkgconfig/libmcs.pc

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Wed Oct 17 2007 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Initial package. (using DAR)
