# $Id$
# Authority: dag

%define real_name carvfs

Summary: Fuse carving filesystem
Name: fuse-carvfs
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: System/Libraries
URL: http://sourceforge.net/projects/carvpath/

Source: carvfs%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libcarvpath-devel
BuildRequires: fuse-devel

%description
Fuse carving filesystem

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}%{version}

%{__perl} -pi -e 's|/lib\b|/%{_lib}|g' src/CMakeLists.txt

%build
cmake src -DCMAKE_C_FLAGS="%{optflags} -I$PWD/src" -DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#%ifarch x86_64
#mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}
#%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc COPYING INSTALL NEWS README.TXT 
%{_bindir}/carvfs
%{_libdir}/libmodblkdev.so.*
%{_libdir}/libmodraw.so.*

%files devel
%defattr (-, root, root, 0755)
%{_includedir}/carvfsmod.h
%{_libdir}/libmodblkdev.so
%{_libdir}/libmodraw.so

%changelog
* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
