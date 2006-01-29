# $Id$
# Authority: dries
# Upstream: Andrea Marchesini <bakunin$autistici,org>

Summary: Library for parsing, writing and creating RSS files or streams
Name: libmrss
Version: 0.7
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www2.autistici.org/bakunin/libmrss/

Source: http://www2.autistici.org/bakunin/libmrss/libmrss-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel

%description
mRss is a C library for parsing, writing and creating RSS files or streams. 

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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libmrss.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mrss.h
%{_libdir}/libmrss.a
%{_libdir}/libmrss.so
%{_libdir}/pkgconfig/mrss.pc
%exclude %{_libdir}/*.la

%changelog
* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
