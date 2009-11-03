# $Id$
# Authority: dries

Summary: Network transport library
Name: skstream
Version: 0.3.6
Release: 1%{?dist}
License: GPL/LGPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/skstream

Source: http://dl.sf.net/worldforge/skstream-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
skstream is a network transport library written in C++ using the iostream
interface. It provides classes for handling TCP socket connections. It is
derived from the FreeSockets library by Rafael Guterres Jeffman. Its
primary use to the WorldForge project, who maintain this version, is as a
transport for Atlas-C++, the standard Atlas protocol implementation.

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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libskstream-0.3.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/skstream-0.3/
%exclude %{_libdir}/libskstream-0.3.la
%{_libdir}/libskstream-0.3.so
%{_libdir}/pkgconfig/skstream-0.3.pc
%{_libdir}/pkgconfig/skstream-unix-0.3.pc
%{_libdir}/skstream-0.3/

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.6-1
- Updated to release 0.3.6.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.5-1
- Initial package.
