%define		gst_minver	0.8.0
%define		gstp_minver	0.8.0
%define		majorminor	0.8
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1 || :

Name: 		%{gstreamer}-monkeysaudio
Version: 	0.8.0
Release: 	0
Summary: 	GStreamer Monkey's Audio Plugin

Group: 		Applications/Multimedia
License: 	Free To Use (Monkey's Audio License)
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gst-monkeysaudio/gst-monkeysaudio-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}
Requires:	%{gstreamer}-plugins >= %{gstp_minver}

BuildRequires: 	%{gstreamer}-devel >= %{gst_minver}
BuildRequires: 	%{gstreamer}-plugins-devel >= %{gst_minver}
BuildRequires: 	gcc-c++

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
* Fri Apr 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: First package
