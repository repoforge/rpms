# $Id$
# Authority: dries
# Upstream: Jeroen <jeroen$fox-toolkit,org>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh8:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Toolkit for GUI development
Name: fox
Version: 1.6.33
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.fox-toolkit.com

Source: ftp://ftp.fox-toolkit.com/pub/fox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, automake, autoconf, zlib-devel, bzip2-devel
BuildRequires: libpng-devel, libjpeg-devel, libtiff-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, mesa-libGLU-devel mesa-libGL-devel, libXext-devel}

%description
FOX is a C++-based toolkit for GUI development. It includes a rich set
of widgets and has powerful yet simple layout managers, MDI widgets,
and mega-widgets. FOX incorporates support for XDND for drag and
drop, X clipboard and X Selection, watching other I/O channels and
sockets, timers and idle processing, object serialization and
deserialization, a registry to save persistent settings, and 3D
widgets using Mesa or OpenGL. FOX works on Linux, IRIX, Solaris,
HP/UX, AIX, Tru64 Unix, Windows 9x,NT,2K (VC++, GNUWIN32, Borland,
VisualAge C++), FreeBSD, and Sequent.

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
%{__mv} %{buildroot}%{_datadir}/doc/fox-* rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS INSTALL LICENSE README rpmdocs/*
%doc %{_mandir}/man1/PathFinder*
%doc %{_mandir}/man1/PathFinder*
%doc %{_mandir}/man1/adie*
%doc %{_mandir}/man1/calculator*
%doc %{_mandir}/man1/reswrap*
%doc %{_mandir}/man1/shutterbug*
%{_bindir}/Adie.stx
%{_bindir}/PathFinder
%{_bindir}/adie
%{_bindir}/calculator
%{_bindir}/fox-config
%{_bindir}/reswrap
%{_bindir}/shutterbug
%{_libdir}/libCHART-*.so.*
%{_libdir}/libFOX-*.so.*

%files devel
%{_includedir}/fox-*/
%{_libdir}/libCHART-*.so
%{_libdir}/libFOX-*.so
%{_libdir}/pkgconfig/fox.pc
%exclude %{_libdir}/libCHART-*.a
%exclude %{_libdir}/libFOX-*.a
%exclude %{_libdir}/*.la

%changelog
* Sun May  4 2008 Dries Verachtert <dries@ulyssis.org> - 1.6.33-1
- Updated to release 1.6.33.

* Thu Mar 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.6.32-1
- Updated to release 1.6.32.

* Tue Oct 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.6.30-1
- Updated to release 1.6.30.

* Sun Jun 10 2007 Dries Verachtert <dries@ulyssis.org> - 1.6.28-1
- Updated to release 1.6.28.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.19-1
- Updated to release 1.6.19.

* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.13-1
- Updated to release 1.6.13.

* Sat Jul 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.10-1
- Updated to release 1.6.10.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.4-1
- Updated to release 1.6.4.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.2-1
- Updated to release 1.6.2.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.1-1
- Updated to release 1.6.1.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0-1
- Updated to release 1.6.0.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.27-1
- Updated to release 1.4.27-1

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.24-1
- Initial package.
