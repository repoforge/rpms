# $Id$
# Authority: dag

### EL6 ships with xdelta-1.1.4-8.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Binary file delta generator and an RCS replacement library
Name: xdelta
Version: 1.1.4
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://sourceforge.net/projects/xdelta/

Source: http://xdelta.googlecode.com/files/xdelta-%{version}.tar.gz
Patch1: xdelta-1.1.3-aclocal.patch
Patch3: xdelta-1.1.3-edsio.patch
Patch4: xdelta-1.1.4-glib2.patch
Patch6: xdelta-1.1.3-pkgconfig.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.10.0
BuildRequires: zlib-devel
BuildRequires: pkgconfig

%description
Xdelta (X for XCF: the eXperimental Computing Facility at Berkeley) is
a binary delta generator (like a diff program for binaries) and an RCS
version control replacement library. The Xdelta library performs its
work independently of the actual format used to encode the file and is
intended to be used by various higher-level programs such as XCF's
Project Revision Control System (PRCS).  PRCS is a front end for a
version control toolset.  Xdelta uses a binary file delta algorithm to
replace the standard diff program used by RCS.

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
%patch1 -p1 -b .aclocal
%patch3 -p1 -b .edsio
%patch4 -p1 -b .glib2
%patch6 -p1 -b .pkgconfig

%build
autoreconf -fiv
%configure
%{__make} %{?_smp_mflags} \
    CFLAGS="-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE %{optflags} $(pkg-config --cflags glib-2.0)" \
    LDFLAGS="$(pkg-config --libs glib-2.0)"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS README xdelta.magic
%doc %{_mandir}/man1/xdelta.1*
%{_bindir}/xdelta
%{_libdir}/libedsio.so.*
%{_libdir}/libxdelta.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/xdelta-config
%{_datadir}/aclocal/xdelta.m4
%{_includedir}/edsio*.h
%{_includedir}/xd*.h
%{_libdir}/libedsio.so
%{_libdir}/libxdelta.so
%{_libdir}/pkgconfig/xdelta.pc
%exclude %{_libdir}/libedsio.a
%exclude %{_libdir}/libxdelta.a
%exclude %{_libdir}/libedsio.la
%exclude %{_libdir}/libxdelta.la

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Initial package. (using DAR)
