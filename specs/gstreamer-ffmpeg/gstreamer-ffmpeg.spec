%define		gst_minver	0.8.0
%define		gstp_minver	0.8.0
%define		majorminor	0.8
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1 || :

Name: 		%{gstreamer}-ffmpeg
Version: 	0.8.1
Release: 	0
Summary: 	GStreamer FFmpeg-based streaming media framework plugin

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://gstreamer.freedesktop.org/src/gst-ffmpeg/gst-ffmpeg-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}
Requires:	%{gstreamer}-plugins >= %{gstp_minver}

BuildRequires:	%{gstreamer}-devel >= %{gst_minver}
# libtool needs this, sigh
BuildRequires:	gcc-c++

# all of the FFmpeg dependencies we need to get the codecs we want
BuildRequires:	freetype-devel
BuildRequires:	imlib2-devel
BuildRequires:	SDL-devel

# Dear Red Hat.  Please get your Requires for -devel packages straight.
# This time, you forgot to make SDL-devel require alsa-lib-devel.
# Love, Thomas.
%{expand:%%define buildforfc2 %(A=$(awk '{print $4}' /etc/fedora-release); if [ "$A" = 2 ]; then echo 1; else echo 0; fi)}

%if %{buildforfc2}
BuildRequires:  alsa-lib-devel
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gst-ffmpeg-%{version}

%build
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{register}

%postun
%{register}

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-%{majorminor}/libgstffmpeg.so

%changelog
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
