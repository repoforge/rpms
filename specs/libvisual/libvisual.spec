# $Id$

# Authority: dries
# Screenshot: http://libvisual.sourceforge.net/v2/images/jess1.png
# ScreenshotURL: http://libvisual.sourceforge.net/v2/index.php?page=screenshots

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}


Summary: Abstraction library between applications and visualisation plugins
Name: libvisual
Version: 0.2.0
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://libvisual.sourceforge.net/v2/

Source: http://dl.sf.net/libvisual/libvisual-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}

%description
Libvisual is a library that acts as a middle layer between applications that
wish to display audio visualisation and audio visualisation plugins. It is
aimed at developers who have a need for audio visualisation, and those who
write visualisation plugins. By writing an audio visualisation plugin for
libvisual, the developer allows every application that uses libvisual to use
their plugin. The application handles the actual drawing of the graphics,
allowing rendering done by plugins to be drawn anywhere... as ASCII art, in
SDL, as a surface on an OpenGL object, etc. 

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
%{expand: %%define optflags -mmmx -O2} 
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/libvisual.pc
%{_includedir}/libvisual
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Update to release 0.2.0.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1
- Initial package.
