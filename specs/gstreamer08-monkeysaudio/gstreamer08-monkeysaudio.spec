# $Id$
# Authority: matthias

# ExclusiveDist: fc5

%define gst_minver 0.8.0
%define gstp_minver 0.8.0
%define majorminor 0.8
%define gstreamer gstreamer08
%define register %{_bindir}/gst-register-%{majorminor}

Summary: GStreamer streaming media framework Monkey's Audio plugin
Name: %{gstreamer}-monkeysaudio
Version: 0.8.2
Release: 1%{?dist}
License: Freeware
Group: Applications/Multimedia
URL: http://gstreamer.net/
Source: http://gstreamer.freedesktop.org/src/gst-monkeysaudio/gst-monkeysaudio-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): %{register}
Requires(post): %{register}
Requires: %{gstreamer} >= %{gst_minver}
Requires: %{gstreamer}-plugins >= %{gstp_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-devel >= %{gstp_minver}
Buildrequires: mac-devel
# libtool needs this, sigh
BuildRequires: gcc-c++
Obsoletes: gstreamer-monkeysaudio <= 0.8.2

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package provides a plugin to decode Monkey's Audio (.ape) files.


%prep
%setup -n gst-monkeysaudio-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
%{register} &>/dev/null || :

%postun
%{register} &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING GStreamer-monkeysaudio-permit MAINTAINERS README RELEASE
%{_libdir}/gstreamer-%{majorminor}/libgstmonkeysaudio.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmonkeysaudio.a
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmonkeysaudio.la


%changelog
* Fri Jan 20 2006 Matthias Saou <http://freshrpms.net/> 0.8.2-1
- Rename to gstreamer08-monkeysaudio for 0.8.x compatibility on FC5.

* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net/> 0.8.2-1
- Update to 0.8.2.
- Remove no longer needed 64bit patch.
- Add new mac-devel build requirement.

* Wed May  4 2005 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Add patch to fix compilation on 64bit with gcc4, thanks to Ronald.
- Added some docs to be included, the mandatory license for instance.
- Spec file cleanup, as it's in fact here to stay.

* Fri Apr 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: First package

