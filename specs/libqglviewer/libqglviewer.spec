# $Id$
# Authority: dries
# Upstream: Gilles Debunne <gilles,debunne$laposte,net>


%define real_version 2.2.3-1

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Library for quick creation of OpenGL 3D viewers
Name: libqglviewer
Version: 2.2.3
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://artis.imag.fr/Members/Gilles.Debunne/QGLViewer

Source: http://artis.imag.fr/Members/Gilles.Debunne/QGLViewer/src/libQGLViewer-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++
%{!?_without_modxorg:BuildRequires: libXmu-devel }

%description
libQGLViewer is a C++ library based on Qt that enables the quick
creation of OpenGL 3D viewers. Simple applications only require an
implementation of the drawing method; the camera trackball does the
rest. Features also include screenshot saving, mouse manipulated
frames, stereo display, interpolated keyFrames, object selection, and
much more. It is fully customizable and easy to extend to create
complex applications. It ships with many examples and comprehensive
documentation.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libQGLViewer-%{real_version}

%build
cd QGLViewer
export INSTALL_ROOT=%{buildroot}
qmake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd QGLViewer
export INSTALL_ROOT=%{buildroot}
%makeinstall
%{__mv} %{buildroot}%{_docdir}/QGLViewer/ generateddocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README QGLViewer/generateddocs/*
%{_libdir}/libQGLViewer.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer.so
%{_libdir}/libQGLViewer.prl

%changelog
* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Updated to release 2.2.3.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.1-1
- Updated to release 2.2.1.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Initial package.
