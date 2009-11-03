# $Id$
# Authority: matthias

%define gst_minver 0.10.0
%define gstpb_minver 0.10.0
%define majorminor 0.10
%define gstreamer gstreamer

Summary: GStreamer streaming media framework DLL loader plugin
Name: %{gstreamer}-pitfdll
Version: 0.9.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://ronald.bitfreak.net/pitfdll
#Source: http://dl.sf.net/pitfdll/pitfdll-%{version}.tar.bz2
Source: pitfdll-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: %{gstreamer} >= %{gst_minver}
Requires: %{gstreamer}-plugins-base >= %{gstpb_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}
# libtool needs this, sigh
BuildRequires: gcc-c++
# at least for now, this is i386 only, sorry
ExclusiveArch: i386

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains a DLL loader plugin to provide media playback for some
proprietary formats.


%prep
%setup -n pitfdll-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Create empty directory so that people can guess where DLLs should go
%{__mkdir_p} %{buildroot}%{_libdir}/win32/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README RELEASE TODO
%{_libdir}/gstreamer-%{majorminor}/libpitfdll.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libpitfdll.la
%dir %{_libdir}/win32/


%changelog
* Thu Apr 20 2006 Matthias Saou <http://freshrpms.net/> 0.9.1.1-1
- Update to gst 0.10 compatible CVS snapshot.

* Fri Dec  2 2005 Matthias Saou <http://freshrpms.net/> 0.8.2-1
- Update to 0.8.2.
- Drop gcc4 patch.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Initial RPM release.
- Include gcc4 patch from sf.net tracker bug #1188654.
- Make the package i386 exclusive.

