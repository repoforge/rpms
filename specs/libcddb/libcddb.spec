# $Id$
# Authority: dag

Summary: Library (C API) for accessing CDDB servers
Name: libcddb
Version: 1.3.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://libcddb.sourceforge.net/

Source: http://dl.sf.net/sourceforge/libcddb/libcddb-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libcdio-devel >= 0.67

%description
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (e.g http://freedb.org/).

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
### Don't use rpath!
%{__perl} -pi -e '
		s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
		s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g;
	' libtool
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
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/cddb_query
%{_libdir}/libcddb.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cddb/
%{_libdir}/libcddb.a
%exclude %{_libdir}/libcddb.la
%{_libdir}/libcddb.so
%{_libdir}/pkgconfig/libcddb.pc

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
