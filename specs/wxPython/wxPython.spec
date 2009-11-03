# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: GUI toolkit for the Python programming language
Name: wxPython
Version: 2.8.9.1
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://www.wxpython.org/

Source: http://dl.sf.net/wxpython/wxPython-src-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: wxGTK-devel >= 2.8.9
BuildRequires: wxGTK-gl
BuildRequires: zlib-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libGL-devel, libGLU-devel}

Provides: wxPythonGTK2 = %{version}-%{release}
Obsoletes: compat-wxPythonGTK < 2.8.4.0

%description
wxPython is a GUI toolkit for the Python programming language. It allows
Python programmers to create programs with a robust, highly functional
graphical user interface, simply and easily. It is implemented as a Python
extension module (native code) that wraps the popular wxWindows cross
platform GUI library, which is written in C++.

%package devel
Summary: Development files for wxPython add-on modules
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: wxGTK-devel

%description devel
This package includes C++ header files and SWIG files needed for developing
add-on modules for wxPython. It is NOT needed for development of most
programs which use the wxPython toolkit.

%prep
%setup -n wxPython-src-%{version}/wxPython

%build
%{__rm} -rf distutils/
python setup.py build WXPORT="gtk2" UNICODE="1"

%install
%{__rm} -rf %{buildroot}
python setup.py install --root="%{buildroot}" WXPORT="gtk2" UNICODE="1"

%if "%{python_sitelib}" != "%{python_sitearch}"
%{__mv} %{buildroot}%{python_sitelib}/wx.pth  %{buildroot}%{python_sitearch}
%{__mv} %{buildroot}%{python_sitelib}/wxversion.py* %{buildroot}%{python_sitearch}
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc demo/ docs/ licence/ samples/
%{_bindir}/*
%{python_sitearch}/wx.pth
%{python_sitearch}/wxversion.py*
%dir %{python_sitearch}/wx-2.8-gtk2-unicode/
%{python_sitearch}/wx-2.8-gtk2-unicode/wx/
%{python_sitearch}/wx-2.8-gtk2-unicode/wxPython/
%{python_sitelib}/wxaddons/

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/wx-2.8/
%dir %{_includedir}/wx-2.8/wx/
%dir %{_includedir}/wx-2.8/wx/wxPython/
%{_includedir}/wx-2.8/wx/wxPython/*.h
%dir %{_includedir}/wx-2.8/wx/wxPython/i_files/
%{_includedir}/wx-2.8/wx/wxPython/i_files/*.i
%{_includedir}/wx-2.8/wx/wxPython/i_files/*.py*
%{_includedir}/wx-2.8/wx/wxPython/i_files/*.swg

%changelog
* Mon May 25 2009 Dag Wieers <dag@wieers.com> - 2.8.9.1-1
- Initial package. (based on Fedora)
