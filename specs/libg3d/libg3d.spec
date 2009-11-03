# $Id$
# Authority: dries
# Upstream: Markus Dahms <fm$automagically,de>

Summary: Library for loading and manipulating 3D objects
Name: libg3d
Version: 0.0.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://automagically.de/index.shtml?g3dviewer

Source: http://automagically.de/files/libg3d-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, gtk2-devel, glib2-devel, gcc-c++

%description
Libg3d is a glib-based library for loading and manipulating 3D objects.
It supports a wide range of file formats for 3D objects and textures.
Its plugin interface makes it easily expandable. The code has been split
off from the g3dviewer project, which now depends on this library.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libg3d.so.*
%{_libdir}/libg3d/
%{_datadir}/gtk-doc/html/libg3d/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/g3d/
%{_libdir}/libg3d.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/libg3d.pc

%changelog
* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.6-1
- Updated to release 0.0.6.

* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.5-1
- Updated to release 0.0.5.

* Sun May 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1
- Updated to release 0.0.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.2-1
- Initial package.
