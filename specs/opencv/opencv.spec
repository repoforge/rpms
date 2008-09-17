# $Id$
# Authority: dag

%define _without_ffmpeg 1

%define pythondir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define pyexecdir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Collection of algorithms for computer vision
Name: opencv
Version: 1.0.0
Release: 1
Group: Development/Libraries
License: Intel Open Source License
URL: http://www.intel.com/technology/computing/opencv/index.htm

Source0: http://prdownloads.sourceforge.net/opencvlibrary/opencv-%{version}.tar.gz
Source1: opencv-samples-Makefile
Patch0: opencv-1.0.0-pythondir.diff
Patch1: opencv-1.0.0-configure.in.diff
Patch2: opencv-1.0.0-autotools.diff
Patch3: opencv-1.0.0-pkgconfig.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
#BuildRequires: swig >= 1.3.24
BuildRequires: swig
BuildRequires: zlib-devel
%{!?_without_ffmpeg:BuildRequires: ffmpeg-devel >= 0.4.9}

%description
OpenCV means Intel® Open Source Computer Vision Library. It is a collection of
C functions and a few C++ classes that implement some popular Image Processing
and Computer Vision algorithms.

%package devel
Summary: Development files for using the OpenCV library
Group: Development/Libraries
Requires: opencv = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the OpenCV C/C++ library and header files, as well as
documentation. It should be installed if you want to develop programs that
will use the OpenCV library.

%package python
Summary: Python bindings for apps which use OpenCV
Group: Development/Libraries
Requires: opencv = %{version}-%{release}

%description python
This package contains Python bindings for the OpenCV library.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi.orig -e 's|\r||' interfaces/swig/python/*.py samples/python/*.py
%{__perl} -pi.orig -e 's|^#!.*||' interfaces/swig/python/adaptors.py interfaces/swig/python/__init__.py

### Adjust timestamp on cvconfig.h.in
touch -r configure.in cvconfig.h.in

%build
%configure \
    --disable-static \
    --enable-apps \
    --enable-python \
%{?_without_ffmpeg:--without-ffmpeg}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/opencv/samples/c/GNUmakefile

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING THANKS TODO
%{_bindir}/opencv-*
%dir %{_datadir}/opencv/
%{_datadir}/opencv/haarcascades
%{_datadir}/opencv/readme.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/opencv/doc/
%doc %{_datadir}/opencv/samples/c/
%dir %{_datadir}/opencv/
%dir %{_datadir}/opencv/samples/
%{_includedir}/opencv
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/opencv.pc
%exclude %{_libdir}/lib*.a
%exclude %{_libdir}/lib*.la

%files python
%defattr(-, root, root, 0755)
%doc %{_datadir}/opencv/samples/python/
%dir %{_datadir}/opencv/
%dir %{_datadir}/opencv/samples/
%{pyexecdir}/opencv/
%exclude %{pyexecdir}/opencv/*.la

%changelog
* Tue Sep 16 2008 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package based on Fedora.
