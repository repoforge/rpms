# $Id: $

# Authority: newrpms


Summary: Graphical User Interface based on SDL
Name: 	 paragui
Version: 1.0.4
Release: 1
License: LGPL
Group: 	 System Environment/Libraries
Source:  http://savannah.nongnu.org/download/paragui/%{name}-%{version}.tar.gz
URL: 	 http://www.bms-austria.com/projects/paragui/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel libpng-devel SDL_image-devel libtiff-devel, freetype-devel, gcc-c++, expat-devel, physfs-devel, readline-devel

Packager: Rudolf Kastl <che666 at uni.de>
Vendor: http://newrpms.sunsite.dk/

%description
ParaGUI is a cross-platform high-level application framework and GUI
(graphical user interface) library. ParaGUI's cross-platform nature is
completely based on the Simple DirectMedia Layer (SDL).

%package -n %{name}-devel
Summary: Headers for developing programs that will use paragui
Group: Development/C
Requires: %{name} = %{version} expat-devel
Provides: %{name}-devel = %{version}-%{release}

%description -n %{name}-devel
This package contains the headers that programmers will need to develop
applications which will use paragui, a GUI on top of SDL.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files -n %{name}-devel
%defattr(-, root, root)
%doc README
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.*a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}
%{_libdir}/pkgconfig/paragui.pc

%changelog
* Wed Oct 30 2002 Che
- initial rpm release
