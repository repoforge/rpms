# $Id$
# Authority: dag

Summary: Library to access digital cameras via PTP
Name: libptp2
Version: 1.1.10
Release: 1%{?dist}
License: GPL
Group: System/Libraries
URL: http://sourceforge.net/projects/libptp/

Source: http://dl.sf.net/sourceforge/libptp/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libusb-devel

%description
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. This library contains a near complete remote
control command set for Canon digital cameras and also some stuff for
Nikon.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n ptpcam
Summary: Command line utility to access digital cameras via PTP
Group: Graphics

%description -n ptpcam
Many digital cameras communicate with computers via the Picture
Transfer Protocol (PTP). This protocol gives a standardized
manufacturer-independent set of camera operation commands, as
downloading pictures, remote capturing, ... Unfortunately
manufacturers added also there own non-standard commands, especially
for remote control. ptpcam makes use of the %name library which
contains a near complete remote control command set for Canon digital
cameras and also some stuff for Nikon.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libptp2.so.*

%files devel
%{_includedir}/libptp2/
%{_libdir}/libptp2.so
%exclude %{_libdir}/libptp2.la

%files -n ptpcam
%{_bindir}/ptpcam

%changelog
* Mon May 17 2010 Dag Wieers <dag@wieers.com> - 1.1.10-1
- Initial package. (using DAR)
