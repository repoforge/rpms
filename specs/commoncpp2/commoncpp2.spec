# $Id$
# Authority: dag

Summary: GNU Common C++ class framework
Name: commoncpp2
Version: 1.6.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/commoncpp/

Source: http://ftp.gnu.org/pub/gnu/commoncpp/commoncpp2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, zlib-devel, doxygen

%description
GNU Common C++ is a portable and highly optimized class framework for writing
C++ applications that need to use threads, sockets, XML parsing, serialization,
config files, etc.

This framework offers a class foundation that hides platform differences from
your C++ application so that you need not write platform specific code. GNU
Common C++ has been ported to compile natively on most platforms which support
posix threads.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, libxml2-devel, zlib-devel
Requires: /sbin/install-info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-static \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/commoncpp2.info %{_infodir}/dir || :

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/commoncpp2.info %{_infodir}/dir || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README THANKS TODO
%{_libdir}/libccext2-1.6.so.*
%{_libdir}/libccgnu2-1.6.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/
%doc %{_infodir}/commoncpp2.info*
%{_bindir}/ccgnu2-config
%{_datadir}/aclocal/ost_check2.m4
%{_includedir}/cc++/
%{_libdir}/libccext2.so
%{_libdir}/libccgnu2.so
%{_libdir}/pkgconfig/libccext2.pc
%{_libdir}/pkgconfig/libccgnu2.pc
%exclude %{_libdir}/libccext2.la
%exclude %{_libdir}/libccgnu2.la

%changelog
* Fri May 30 2008 Dag Wieers <dag@wieers.com> - 1.6.2-1
- Updated to release 1.6.2.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.5.5-1
- Initial package. (using DAR)
