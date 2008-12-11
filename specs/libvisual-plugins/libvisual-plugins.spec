# $Id$
# Authority: dries
# Screenshot: http://libvisual.sourceforge.net/v2/images/jess1.png
# ScreenshotURL: http://libvisual.sourceforge.net/v2/index.php?page=screenshots

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

Summary: Plugins for libvisual
Name: libvisual-plugins
Version: 0.4.0
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://libvisual.sourceforge.net/v2/

Source: http://dl.sf.net/libvisual/libvisual-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvisual-devel, gcc-c++, esound-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_with_gl:BuildRequires: %{_with_gl}}

%description
This package contains many plugins for libvisual.

Libvisual is a library that acts as a middle layer between applications that
wish to display audio visualisation and audio visualisation plugins. It is
aimed at developers who have a need for audio visualisation, and those who
write visualisation plugins. By writing an audio visualisation plugin for
libvisual, the developer allows every application that uses libvisual to use
their plugin. The application handles the actual drawing of the graphics,
allowing rendering done by plugins to be drawn anywhere... as ASCII art, in
SDL, as a surface on an OpenGL object, etc.

%prep
%setup

%build
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
%{_datadir}/libvisual-plugins-0.4/
%{_libdir}/libvisual-0.4/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Update to release 0.2.0.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1
- Initial package.
