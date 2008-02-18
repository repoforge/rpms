# $Id$
# Authority: dries

Summary: HAM radio equipment control libraries
Name: hamlib
Version: 1.2.7
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://hamlib.org

Source: http://dl.sf.net/hamlib/hamlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libxml2-devel

%description
The HAM radio equipment control libraries allow you to write amateur radio 
equipment control programs for transceivers and antenna rotators which use 
CAT or similar computer interfaces for control.

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
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man1/rigctl.1*
%doc %{_mandir}/man1/rigmem.1*
%doc %{_mandir}/man1/rigsmtr.1*
%doc %{_mandir}/man1/rigswr.1*
%doc %{_mandir}/man1/rotctl.1*
%doc %{_mandir}/man8/rigctld.8*
%doc %{_mandir}/man8/rpc.rigd.8*
%doc %{_mandir}/man8/rpc.rotd.8*
%{_bindir}/rigctl
%{_bindir}/rigctld
%{_bindir}/rigmem
%{_bindir}/rigsmtr
%{_bindir}/rigswr
%{_bindir}/rotctl
%{_sbindir}/rpc.rigd
%{_sbindir}/rpc.rotd
%{_libdir}/libhamlib++.so.*
%{_libdir}/libhamlib.so.*
%{_libdir}/pkgconfig/hamlib.pc
%{_datadir}/aclocal/hamlib.m4

%files devel
%{_includedir}/hamlib/
%{_libdir}/hamlib-*.so
%{_libdir}/libhamlib++.so
%{_libdir}/libhamlib.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Sun Feb 17 2008 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Initial package.
