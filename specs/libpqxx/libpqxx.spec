# $Id$
# Authority: dries

Summary: C++ client API for PostgreSQL
Name: libpqxx
Version: 2.6.9
Release: 2
License: BSD
Group: System Environment/Libraries
URL: http://pqxx.org/

Source: http://pqxx.org/download/software/libpqxx/libpqxx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, postgresql-devel, postgresql-libs, gcc-c++, pkgconfig
Requires: postgresql-libs

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL. Supersedes
older libpq++ interface. Requires an up-to-date C++ compiler, like gcc 2.95
or better.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: postgresql-devel, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%{__perl} -pi -e "s|.Werror||g;" configure*

%build
%configure \
	--enable-shared
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
%{_libdir}/libpqxx-%{version}.so

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc doc/html/*
%{_includedir}/pqxx/*
%{_libdir}/libpqxx.a
%exclude %{_libdir}/*.la
%{_libdir}/libpqxx.so
%{_bindir}/pqxx-config
%{_libdir}/pkgconfig/libpqxx.pc

%changelog
* Sun Jun 22 2008 David Rennalls <drennalls@gmail.com> - 2.6.9-2
- Various fixes.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 2.6.9-1
- Updated to release 2.6.9.

* Mon Nov 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.7-2
- Added openssl-devel and pkgconfig requires, thanks to Rex Dieter.

* Mon Nov 13 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.7-1
- Updated to release 2.6.7.

* Sun May 28 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.6-1
- Updated to release 2.6.6.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Initial package.
