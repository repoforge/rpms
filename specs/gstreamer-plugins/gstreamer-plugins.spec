# $Id$
# Authority: dag

%define major 0.7

Summary: GStreamer Streaming-media framework plugins
Name: gstreamer-plugins
Version: 0.7.1
Release: 0
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: gst-plugins-%{version}.tar.bz2
Patch1: gst-plugins-0.4.2-pthread-includes.patch
#Patch2: gstreamer-plugins-0.5.0-libdirfix.patch
#Patch3: gstreamer-plugins-0.6.0-fPIC.patch
#Patch4: gstreamer-plugins-0.6.0-noffmpeg.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: glib2-devel >= 2.0.0
BuildRequires: gstreamer-devel = %{version}, libjpeg-devel, SDL-devel >= 1.2.0
BuildRequires: arts-devel, cdparanoia-devel >= alpha9.7, esound-devel >= 0.2.8
BuildRequires: xmms-devel, mikmod, audiofile-devel >= 0.2.1
BuildRequires: libogg-devel >= 1.0, libvorbis-devel >= 1.0
BuildRequires: libmad-devel, libsidplay-devel, libshout-devel, mpeg2dec-devel
BuildRequires: Hermes-devel, gsm-devel, ladspa-devel
%{!?rh73:BuildRequires: swfdec-devel, libshout-devel}
#BuildRequires: openquicktime
#BuildRequires: gnome-vfs2-devel >= 2.1.3

Requires: gstreamer, swh-plugins
#Requires: gstreamer = %{version}
PreReq: /usr/bin/gst-register
PreReq: GConf2
PreReq: /usr/bin/gconftool-2

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gstreamer-devel >= %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n gst-plugins-%{version}
%patch1 -p1 -b .pthread-includes
#%patch2 -p1 -b .libdirfix
#%patch3 -p1 -b .fPIC
#%patch4 -p1 -b .noffmpeg

%build
#{__aclocal}
#{__automake}
#{__autoconf}
%configure \
	--disable-dependency-tracking \
	--disable-vorbistest \
	--disable-tests \
	--disable-examples \
	--disable-ffmpeg
### FIXME: Disable ffmpeg to make it build properly ;-(
#	--enable-DEBUG
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gstreamer-%{major}/*.a \
		%{buildroot}%{_libdir}/gstreamer-%{major}/*.la \
		%{buildroot}%{_includedir}/gstreamer-%{major}/gst/media-info/media-info.h \
		%{buildroot}%{_libdir}/libgstmedia-info*.so*

%post
/sbin/ldconfig 2>/dev/null
DISPLAY="" /usr/bin/gst-register &>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gstreamer.schemas &>/dev/null
scrollkeeper-update -q

%postun
/sbin/ldconfig 2>/dev/null
DISPLAY="" /usr/bin/gst-register &>/dev/null
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README RELEASE REQUIREMENTS TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gconf/schemas/gstreamer.schemas
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/gstreamer-%{major}/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gstreamer-%{major}/

%changelog
* Tue Oct 21 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to release 0.6.4.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.6.3-3
- Build against ladspa-devel.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 0.6.3-2
- Build against gsm-devel and swfdec-devel.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Build against Hermes for the colorspace plugin. (Eelco Hoekema)

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Updated to release 0.6.3.

* Tue Jun 10 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Fri May 09 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Initial package. (using DAR)
