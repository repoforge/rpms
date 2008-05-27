# $Id$
# Authority: dag

Summary: Simple Wiimote Library for Linux
Name: libwiimote
Version: 0.4
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://libwiimote.sourceforge.net/

Source: http://dl.sf.net/libwiimote/libwiimote-%{version}.tgz
Patch0: libwiimote-0.4-fpic.patch
Patch1: libwiimote-0.4-includedir.patch
Patch2: libwiimote-0.4-dso-symlinks.patch
Patch3: libwiimote-0.4-soname.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: bluez-libs-devel

%description
Libwiimote is a C-library that provides a simple API for communicating with
the Nintendo Wii Remote (aka. wiimote) on a Linux system. The goal of this
library is to be a complete and easy to use framework for interfacing
applications with the wiimote.

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
%patch0 -p1 -b .fpic
%patch1 -p1 -b .includedir
%patch2 -p1 -b .dso-symlinks
%patch3 -p1 -b .soname

%build
autoconf
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/libcwiimote.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libcwiimote/
%{_libdir}/libcwiimote.so
%exclude %{_libdir}/libcwiimote.a

%changelog
* Sat May 24 2008 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
