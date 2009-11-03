# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

%{?el5:%define _with_gl libGLU-devel}
%{?el4:%define _with_gl xorg-x11-Mesa-libGLU}
%{?el3:%define _with_gl XFree86-Mesa-libGLU}
%{?rh9:%define _with_gl XFree86-Mesa-libGLU}
%{?rh7:%define _with_gl Glide3-devel}
%{?el2:%define _with_gl Mesa-devel}

Summary: GUI toolkit based on Xlib
Name: xforms
Version: 1.0.91
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://world.std.com/~xforms/

Source: http://savannah.nongnu.org/download/xforms/xforms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXpm-devel libICE-devel}
%{?_with_gl:BuildRequires: %{_with_gl}}

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It features a
rich set of objects, such as buttons, scrollbars, and menus etc. integrated
into an easy and efficient object/event callback execution model that allows
fast and easy construction of X-applications. In addition, the library is
extensible and new objects can easily be created and added to the library.

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
%configure \
    --disable-static \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL NEWS README
%doc %{_mandir}/man1/fd2ps.1*
%doc %{_mandir}/man1/fdesign.1*
%doc %{_mandir}/man5/xforms.5*
%{_bindir}/fd2ps
%{_bindir}/fdesign
%{_libdir}/libflimage.so.*
%{_libdir}/libforms.so.*
%{_libdir}/libformsGL.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/flimage.h
%{_includedir}/forms.h
%{_includedir}/glcanvas.h
%{_libdir}/libflimage.so
%{_libdir}/libforms.so
%{_libdir}/libformsGL.so
%exclude %{_libdir}/libflimage.la
%exclude %{_libdir}/libforms.la
%exclude %{_libdir}/libformsGL.la

%changelog
* Thu Dec 04 2008 Dag Wieers <dag@wieers.com> - 1.0.91-1
- Updated to release 1.0.91.

* Sat Jul 31 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.90-1
- Initial package.
