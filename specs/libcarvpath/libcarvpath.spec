# $Id$
# Authority: dag

Summary: Library for computer forensics carving tools
Name: libcarvpath
Version: 2.3.0
Release: 1%{?dist}
License: Commercial
Group: System/Libraries
URL: http://sourceforge.net/projects/carvpath/

Source: http://dl.sf.net/project/carvpath/LibCarvPath/libcarvpath%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: sqlite-devel >= 3.0

%description
LibCarvpath is a library for computer forensics carving tools.It provides
the low level needs of zero-storage carving using virtual paths. These
virtual file paths can be used in conjunction with the CarvFS filesystem.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: sqlite-devel >= 3.0

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}%{version}

%{__perl} -pi -e 's|/lib\b|/%{_lib}|g' src/CMakeLists.txt

%build
cmake src -DCMAKE_C_FLAGS="%{optflags} -I$PWD/src" -DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr (-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%{_libdir}/libcarvpath.so.*

%files devel
%defattr (-, root, root, 0755)
%{_includedir}/libcarvpath.h
%{_libdir}/libcarvpath.so
#%exclude %{_libdir}/libcarvpath.a
#%exclude %{_libdir}/libcarvpath.la

%changelog
* Tue Nov 23 2010 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
