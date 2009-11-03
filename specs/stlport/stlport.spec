# $Id$

# Authority: dries
# Upstream:

%define real_version 5.0-0125

Summary: C++ STL library compatible with the latest ANSI/ISO C++ specification
Name: stlport
Version: 5.0.0125
Release: 1.2%{?dist}
License: Freeware
Group: System Environment/Libraries
URL: http://www.stlport.org

Source: http://www.stlport.org/beta/STLport-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, compat-gcc-c++

%description
The ANSI/ISO C++ specifcation includes a standard C++ library, also known as
the STL. GCC by default comes with an implementation that does not comply
with this standard, but instead partly implements an older version. STLport
is freely available version, based on the SGI STL implementation. It is
fully-compliant, supported, and very fast. Includes special debugging
facilities, and interesting and useful extensions to the standard.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n STLport-%{real_version}

%build
%{__make} %{?_smp_mflags} -C src -f gcc.mak CXX=g++33 CC=gcc33

%install
%{__rm} -rf %{buildroot}
%makeinstall -C src -f gcc.mak INSTALLDIR=%{buildroot}/usr

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/stlport
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.0.0125-1.2
- Rebuild for Fedora Core 5.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> 5.0-0125-1
- Update to 5.0-0125
- Some fixes

* Fri May 21 2004 Dries Verachtert <dries@ulyssis.org> 4.6.2-1
- Initial package.
