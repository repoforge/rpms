# $Id$
# Authority: dag


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

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}
%{?rh6:%define _without_tcltk_devel 1}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyOpenGL

Summary: OpenGL bindings for Python
Name: python-opengl
Version: 2.0.1.09
Release: 1.2%{?dist}
License: BSD
Group: Development/Libraries
URL: http://pyopengl.sourceforge.net

Source: http://dl.sf.net/pyopengl/PyOpenGL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, glut-devel, python-numeric
BuildRequires: tcl >= 8.3, tk >= 8.3
%{!?_without_modxorg:BuildRequires: libX11-devel, libXext-devel, libXi-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
Requires: python-numeric, python-imaging

%description
OpenGL bindings for Python including support for GL extensions, GLU, WGL, GLUT,
GLE, and Tk

%prep
%setup -n %{real_name}-%{version}

%build
unset DISPLAY
#python setup.py build
### ugly kludge to get togl to build (tk bindings)
### as you can't pass -L to build, only build_togl
%{__python} setup.py build_w
%{__python} setup.py build_py
%{__python} setup.py build_clib
%{__python} setup.py build_ext
%{__python} setup.py build_togl -L/usr/X11R6/lib
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{python_sitearch}/OpenGL/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1.09-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 2.0.1.09-1
- Contributed by Edward Rudd.
