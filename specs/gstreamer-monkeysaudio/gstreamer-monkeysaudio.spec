%define		gst_minver	0.8.0
%define		gstp_minver	0.8.0
%define		majorminor	0.8
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1 || :

Name: 		%{gstreamer}-monkeysaudio
Version: 	0.8.0
Release: 	1
Summary: 	GStreamer Monkey's Audio Plugin

Group: 		Applications/Multimedia
License: 	Freeware
URL:		http://gstreamer.net/
Source:		http://gstreamer.freedesktop.org/src/gst-monkeysaudio/gst-monkeysaudio-%{version}.tar.bz2
Patch:		gst-monkeysaudio-0.8.0-64bit.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}
Requires:	%{gstreamer}-plugins >= %{gstp_minver}

BuildRequires:	%{gstreamer}-devel >= %{gst_minver}
BuildRequires:	%{gstreamer}-plugins-devel >= %{gst_minver}
BuildRequires:	gcc-c++

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

This package provides a plugin to decode Monkey's Audio (.ape) files.

%prep
%setup -q -n gst-monkeysaudio-%{version}
%patch -p1 -b .64bit

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
%{_libdir}/gstreamer-%{majorminor}/libgstmonkeysaudio.so

%changelog
* Wed May  4 2005 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Add patch to fix compilation on 64bit with gcc4, thanks to Ronald.

* Fri Apr 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: First package

