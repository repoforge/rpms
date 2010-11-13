# $Id$
# Authority: dag

### EL6 ships with gstreamer-python-0.10.16-1.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

%define real_name gst-python

Summary: Python bindings for GStreamer
Name: gstreamer-python
Version: 0.10.7
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://gstreamer.net/

Source: http://gstreamer.freedesktop.org/src/gst-python/gst-python-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, python, python-devel >= 2.3, pygtk2-devel >= 2.4.0
BuildRequires: gstreamer-devel, gstreamer-plugins-base-devel, xmlto, links
# xwindowlistener needs X11 headers
BuildRequires: libX11-devel
Requires: gnome-python2, pygtk2
Requires: gstreamer, gstreamer-plugins-base-devel

Provides: python-gstreamer = %{version}-%{release}

%description
This module contains a wrapper that allows GStreamer applications to be
written in Python.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/gst-python/
%{_libdir}/pkgconfig/gst-python-0.10.pc
%{python_sitearch}/gst-0.10/
%{python_sitearch}/pygst.pth
%{python_sitearch}/pygst.py
%{python_sitearch}/pygst.pyc
%{python_sitearch}/pygst.pyo

%changelog
* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.10.7-1
- Updated to release 0.10.7.

* Thu Aug 25 2005 Matthias Saou <http://freshrpms.net> 0.8.2-1
- Update to 0.8.2.

* Thu Dec  9 2004 Matthias Saou <http://freshrpms.net> 0.8.1-1
- Update to 0.8.1.

* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net> 0.8.0-1
- Update to 0.8.0.

* Wed Oct 20 2004 Matthias Saou <http://freshrpms.net> 0.7.93-1
- Update to 0.7.93.

* Wed Jun 23 2004 Matthias Saou <http://freshrpms.net> 0.7.92-1
- Spec file changes.

* Mon Jun 21 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.92-0.fdr.1: new upstream release

* Wed Mar 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.91-0.fdr.1: new upstream release

* Tue Sep 02 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.0-0.fdr.1: first fedora release

