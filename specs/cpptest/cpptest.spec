# $Id$
# Authority: dag

Summary: Portable and powerful and simple unit testing framework for C++
Name: cpptest
Version: 1.1.1
Release: 1%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://cpptest.sourceforge.net/

Source: http://downloads.sourceforge.net/project/cpptest/cpptest/cpptest-%{version}/cpptest-%{version}.tar.gz
Patch0: cpptest-1.1.0-libcpptest_pc_in.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: doxygen

%description
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .libcpptest_pc_in

%build
%configure \
    --disable-static \
    --enable-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__rm} %{buildroot}%{_datadir}/cpptest/html/html-example.html
%{__rm} %{buildroot}%{_datadir}/cpptest/html/index.html
%{__rm} %{buildroot}%{_datadir}/cpptest/html/screenshot*png

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%{_libdir}/libcpptest.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
%{_includedir}/cpptest*.h
%{_libdir}/libcpptest.so
%{_libdir}/pkgconfig/libcpptest.pc
%exclude %{_libdir}/libcpptest.la

%changelog
* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Initial package (using DAR)
