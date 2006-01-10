# $Id$
# Authority: dries
# Upstream: Andrea Marchesini <bakunin$autistici,org>

Summary: Library for parsing, writing and creating XML
Name: libnxml
Version: 0.3
Release: 1
License: GPL
Group: Development/Libraries
URL: http://autistici.org/bakunin/codes.php

Source: http://autistici.org/bakunin/libnxml/libnxml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, curl-devel

%description
nXML is a C library for parsing, writing, and creating XML 1.0 and 1.1 
files or streams. It supports UTF-8, UTF-16be and UTF-16le, UCS-4 (1234, 
4321, 2143, 2312).

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libnxml.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nxml.h
%{_libdir}/libnxml.a
%{_libdir}/libnxml.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/nxml.pc

%changelog
* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
