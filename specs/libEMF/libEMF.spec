# $Id$
# Authority: dag

Summary: Library for generating Enhanced Metafiles
Name: libEMF
Version: 1.0.3
Release: 1%{?dist}
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://libemf.sourceforge.net/

Source: http://dl.sf.net/pstoedit/libEMF-%{version}.tar.gz
Patch: libEMF-1.0.3-amd64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libstdc++-devel

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

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
%patch -p1 -b .amd64
%{__chmod} 0644 libemf/libemf.h

%build
%configure \
    --disable-static \
    --enable-editing
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" CPPROG="%{__cp} -avp"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_bindir}/printemf
%{_libdir}/libEMF.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/
%{_includedir}/libEMF/
%{_libdir}/libEMF.so
%exclude %{_libdir}/libEMF.la

%changelog
* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (using DAR)
