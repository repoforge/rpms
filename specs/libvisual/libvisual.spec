# $Id$
# Authority: dries
# Screenshot: http://libvisual.sourceforge.net/v2/images/jess1.png
# ScreenshotURL: http://libvisual.sourceforge.net/v2/index.php?page=screenshots

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?el5:%define _with_gl libGLU-devel}
%{?el4:%define _with_gl xorg-x11-Mesa-libGLU}
%{?el3:%define _with_gl XFree86-Mesa-libGLU}
%{?rh9:%define _with_gl XFree86-Mesa-libGLU}
%{?rh7:%define _with_gl Glide3-devel}
%{?el2:%define _with_gl Mesa-devel}

Summary: Abstraction library between applications and visualisation plugins
Name: libvisual
Version: 0.4.0
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://libvisual.sourceforge.net/v2/

Source: http://dl.sf.net/libvisual/libvisual-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_with_gl:BuildRequires: %{_with_gl}}

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
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%ifarch %{ix86}
export CFLAGS="%{optflags} -mmmx"
%endif
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}-0.4

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-0.4.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libvisual-0.4.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libvisual-0.4/
%{_libdir}/pkgconfig/libvisual-0.4.pc
%{_libdir}/libvisual-0.4.so
%exclude %{_libdir}/libvisual-0.4.la

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Update to release 0.2.0.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1
- Initial package.

