# $Id$
# Authority: rudolf

Summary: Graphical User Interface based on SDL
Name: paragui
Version: 1.1.8
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.bms-austria.com/projects/paragui/

Source: http://savannah.nongnu.org/download/paragui/paragui-%{version}.tar.gz
#Patch: gcc34-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, libpng-devel, SDL_image-devel, libtiff-devel, freetype-devel
BuildRequires: gcc-c++, expat-devel, physfs-devel, readline-devel, libsigc++-devel

%description
ParaGUI is a cross-platform high-level application framework and GUI
(graphical user interface) library. ParaGUI's cross-platform nature is
completely based on the Simple DirectMedia Layer (SDL).

%package devel
Summary: Headers for developing programs that will use paragui
Group: Development/Libraries
Requires: %{name} = %{version} expat-devel
Provides: %{name}-devel = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use paragui, a GUI on top of SDL.

%prep
%setup
#%patch -p1

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
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.*a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_datadir}/paragui/
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.8-1
- Updated to release 1.1.8.

* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Added a small patch so moagg builds ok.

* Wed Oct 30 2002 Che
- initial rpm release
