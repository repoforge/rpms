# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

%define real_name PyOpenGL

Summary: OpenGL bindings for Python
Name: python-opengl
Version: 2.0.1.09
Release: 1
License: BSD
Group: Development/Libraries
URL: http://pyopengl.sourceforge.net

Source: http://dl.sf.net/pyopengl/PyOpenGL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, glut-devel, python-numeric
BuildRequires: tcl >= 8.3, tk >= 8.3
BuildRequires: XFree86-devel
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
python setup.py build_w
python setup.py build_py
python setup.py build_clib
python setup.py build_ext
python setup.py build_togl -L/usr/X11R6/lib
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--prefix="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/python*/site-packages/OpenGL/

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 2.0.1.09-1
- Contributed by Edward Rudd.
