# $Id$
# Authority: dries

Summary: Python bindings for wxWindows
Name: wxpython
Version: 2.8.8.1
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.wxpython.org/

Source: http://dl.sf.net/wxpython/wxPython-src-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: python
BuildRequires: python-devel
BuildRequires: wxGTK-devel

%description
wxPython is a GUI toolkit for the Python programming language. It allows
Python programmers to create programs with a robust, highly functional
graphical user interface, simply and easily. It is implemented as a Python
extension module (native code) that wraps the popular wxWidgets cross
platform GUI library, which is written in C++.

Like Python and wxWidgets, wxPython is Open Source which means that it is
free for anyone to use and the source code is available for anyone to look
at and modify. Or anyone can contribute fixes or enhancements to the
project.

wxPython is a cross-platform toolkit. This means that the same program will
run on multiple platforms without modification. Currently supported
platforms are 32-bit Microsoft Windows, most Unix or unix-like systems, and
Macintosh OS X.

%prep
%setup -n wxPython-src-%{version}/wxPython

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/python*/site-packages/wxPython
%{_libdir}/python*/site-packages/wx
%{_bindir}/helpviewer
%{_bindir}/img2png
%{_bindir}/img2xpm
%{_bindir}/img2py
%{_bindir}/xrced
%{_bindir}/pyshell
%{_bindir}/pycrust
%{_bindir}/pywrap
%{_bindir}/pyalacarte
%{_bindir}/pyalamode

%changelog
* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 2.8.8.1-1
- Updated to release 2.8.8.1.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 2.6.1.0-1
- Update to release 2.6.1.0.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> - 2.5.1.5-1
- Update to release 2.5.1.5.

* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> - 2.1.4-1
- First packaging for Fedora Core 1.
