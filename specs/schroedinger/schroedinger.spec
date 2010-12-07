# $Id$
# Authority: dag

Summary: Portable libraries for the high quality Dirac video codec
Name: schroedinger
Version: 1.0.10
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.diracvideo.org/

Source: http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk-doc
BuildRequires: liboil-devel >= 0.3.16
BuildRequires: orc-devel

%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: liboil-devel >= 0.3.16

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-gtk-doc \
    --disable-static
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
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-1.0.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-1.0/
%{_libdir}/libschroedinger-1.0.so
%{_libdir}/pkgconfig/schroedinger-1.0.pc
%exclude %{_libdir}/libschroedinger-1.0.la

%changelog
* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Updated to release 1.0.10.

* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Initial packages. (using DAR)
