# $Id$
# Authority: matthias

# ExclusiveDist: fc5

%define desktop_vendor rpmforge

%define majorminor   0.10
%define gstreamer    gstreamer

%define gst_minver   0.10.0
%define gstpb_minver 0.10.0

Summary: GStreamer streaming media framework "bad" plug-ins
Name: %{gstreamer}-plugins-bad
Version: 0.10.0.1
Release: 1
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.freedesktop.org/
Source: http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch: gst-plugins-bad-0.10.0.1-noWerror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: %{gstreamer} >= %{gst_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}

BuildRequires: gcc-c++
BuildRequires: gtk-doc
BuildRequires: PyXML
Buildrequires: libXt-devel

BuildRequires: liboil-devel
BuildRequires: directfb-devel
BuildRequires: libdca-devel
BuildRequires: faac-devel
BuildRequires: faad2-devel
BuildRequires: gsm-devel
BuildRequires: libmpcdec-devel
BuildRequires: SDL-devel
BuildRequires: swfdec-devel
Buildrequires: wavpack-devel
BuildRequires: xvidcore-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.


%package devel
Summary: Development files for GStreamer Bad Plugins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.

This package contains development files and documentation.


%prep
%setup -q -n gst-plugins-bad-%{version}
%patch -p1 -b .noWerror


%build
%configure \
    --with-package-name='gst-plugins-ugly %{desktop_vendor} rpm' \
    --with-package-origin='http://www.rpmforge.net/' \
    --enable-debug \
    --enable-gtk-doc
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Clean out files that should not be part of the rpm.
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.{a,la}
%{__rm} -f %{buildroot}%{_libdir}/*.{a,la}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README REQUIREMENTS

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstqtdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgsttta.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdlvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvid.so


%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-plugins-%{majorminor}/


%changelog
* Wed Jan 25 2006 Matthias Saou <http://freshrpms.net/> 0.10.0.1-1
- Update to 0.10.0.1, add new plugins.
- Spec file cleanup and rebuild for FC5.

* Mon Dec 05 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.1
- new release

* Thu Dec 01 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.7-0.gst.1
- new release with 0.10 major/minor

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- new release
- remove tta patch
- don't check for languages, no translations yet
- added gtk-doc

* Wed Oct 26 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.4-0.gst.1
- new release
- added speed plugin

* Mon Oct 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.3-0.gst.1
- new release

