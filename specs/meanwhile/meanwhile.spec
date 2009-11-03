# $Id$
# Authority: dag
# Christopher O'Brien <siege@preoccupied.net>

Summary: Lotus Sametime Community Client library
Name: meanwhile
Version: 1.0.2
Release: 1%{?dist}
License: LGPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Source: http://dl.sf.net/meanwhile/meanwhile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.2, gcc-c++, gmp-devel, doxygen

%description
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

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
%{__mv} %{buildroot}%{_datadir}/doc/meanwhile-doc-%{version} rpmdoc

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README rpmdoc/* TODO
%{_libdir}/libmeanwhile.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/meanwhile/
%{_libdir}/libmeanwhile.a
%exclude %{_libdir}/libmeanwhile.la
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc

%changelog
* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Fri Jun 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Fri May 06 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
