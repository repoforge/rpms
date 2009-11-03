# $Id$
# Authority: thias

# ExclusiveDist: el4

Summary: Python bindings for GStreamer
Name: gstreamer-python
Version: 0.8.1
Release: 1%{?dist}
Group: Development/Languages
License: LGPL
URL: http://gstreamer.net/
Source: http://gstreamer.freedesktop.org/src/gst-python/gst-python-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gnome-python2, pygtk2
Requires: gstreamer, gstreamer-plugins
BuildRequires: gcc-c++, python, python-devel >= 2.3, pygtk2-devel >= 2.4.0
BuildRequires: gstreamer-devel, gstreamer-plugins-devel, xmlto, links
# xwindowlistener needs X11 headers
BuildRequires: XFree86-devel
Provides: python-gstreamer = %{version}-%{release}


%description
This module contains a wrapper that allows GStreamer applications to be
written in Python.


%prep
%setup -n gst-python-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# The __init__.py* files go into lib instead of lib64, so fix that
if [ "%{_lib}" != "lib" ]; then
    %{__mv} %{buildroot}%{_prefix}/lib/python?.?/site-packages/gst/__init__.* \
            %{buildroot}%{_libdir}/python?.?/site-packages/gst/
fi


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc examples/gst/*.py examples/gstplay/*.py
%{_libdir}/python?.?/site-packages/gst/
%{_datadir}/gst-python/
%{_libdir}/pkgconfig/*.pc


%changelog
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

