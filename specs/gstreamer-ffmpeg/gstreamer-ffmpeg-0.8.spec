# $Id$
# Authority: matthias

%define gst_minver 0.8.0
%define gstp_minver 0.8.0
%define majorminor 0.8
%define gstreamer gstreamer
%define register %{_bindir}/gst-register-%{majorminor}

Summary: GStreamer streaming media framework FFmpeg-based plugin
Name: %{gstreamer}-ffmpeg
Version: 0.8.7
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://gstreamer.net/
Source: http://gstreamer.freedesktop.org/src/gst-ffmpeg/gst-ffmpeg-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): %{register}
Requires(post): %{register}
Requires: %{gstreamer} >= %{gst_minver}
Requires: %{gstreamer}-plugins >= %{gstp_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-devel >= %{gstp_minver}
# libtool needs this, sigh
BuildRequires: gcc-c++
# The FFmpeg dependencies we need to get the codecs we want
BuildRequires: freetype-devel
BuildRequires: imlib2-devel
BuildRequires: SDL-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.


%prep
%setup -n gst-ffmpeg-%{version}


%build
%ifarch ppc
%configure --disable-altivec
%else
%configure
%endif
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
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/gstreamer-%{majorminor}/libgstffmpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstpostproc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstffmpeg.la
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstpostproc.la


%changelog
* Fri Dec  2 2005 Matthias Saou <http://freshrpms.net/> 0.8.7-1
- Update to 0.8.7.

* Tue Aug 16 2005 Matthias Saou <http://freshrpms.net/> 0.8.6-2
- Force --disable-altivec on ppc, as the build fails otherwise.

* Sat Aug  6 2005 Matthias Saou <http://freshrpms.net/> 0.8.6-1
- Update to 0.8.6.
- Include new postproc plugin.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 0.8.4.1-1
- Update to 0.8.4.1 snapshot that builds on FC4test.
- Added some docs to be included, the mandatory license for instance.
- Change the license from LGPL to GPL, as that's what COPYING states.
- Spec file cleanup, as it's in fact here to stay.

* Tue Apr 12 2005 Matthias Saou <http://freshrpms.net/> 0.8.4-0
- Update to 0.8.4.

* Wed Jan  5 2005 Matthias Saou <http://freshrpms.net/> 0.8.3-0
- Update to 0.8.3.

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 0.8.2-0
- Figure out at last that gcc 3.4's -mtune=pentium4 makes the build fail for
  x86, so replace with -mtune=pentium3 for now.

* Wed Oct 20 2004 Matthias Saou <http://freshrpms.net/> 0.8.2-0
- Update to 0.8.2.

* Thu Jul 29 2004 Matthias Saou <http://freshrpms.net/> 0.8.1-0
- Update to 0.8.1.

* Fri May 21 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.2: update for FC2 and SDL-devel not requiring alsa-lib-devel

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: new source release, changed base name to gstreamer

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.1-0.lvn.2: sync with FreshRPMS

* Tue Mar 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.1-0.lvn.1: First package for rpm.livna.org
