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
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Libvisual port of the G-Force visualisation plugin
Name: libvisual-gforce
Version: 0.1.1
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://libvisual.sourceforge.net/v2/

Source: http://dl.sf.net/libvisual/libvisual-gforce-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvisual-devel, gcc-c++
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif

%description
Libvisual-gforce is the libvisual port of the well-known G-Force
visualization plugin from the Windows/Apple world.

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
%{__install} -d %{buildroot}%{_datadir}/libvisual-gforce
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/*.so*
%{_libdir}/*.la
%{_datadir}/libvisual-gforce
%{_datadir}/libvisual/actor/actor_gforce

%changelog
* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.1-1
- Initial package.
