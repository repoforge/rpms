# $Id$
# Authority: matthias
# ExclusiveDist: fc5 fc6 el5 fc7

%define desktop_vendor rpmforge

%define majorminor   0.10
%define gstreamer    gstreamer

%define gst_minver   0.10.10.1
%define gstpb_minver 0.10.10.1

Summary: GStreamer streaming media framework "bad" plug-ins
Name: gstreamer-plugins-bad
Version: 0.10.8
Release: 3
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch0: gst-plugins-bad-0.10.3-faad2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: %{gstreamer} >= %{gst_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}

BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: gtk-doc
BuildRequires: PyXML
Buildrequires: libXt-devel

BuildRequires: bzip2-devel
BuildRequires: directfb-devel >= 1.0.1
BuildRequires: faac-devel
BuildRequires: faad2-devel
BuildRequires: gsm-devel
BuildRequires: libdca-devel
BuildRequires: libmms-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: liboil-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: neon-devel
BuildRequires: SDL-devel
BuildRequires: soundtouch-devel
#BuildRequires: swfdec-devel
#Buildrequires: wavpack-devel
BuildRequires: xvidcore-devel
BuildRequires: x264-devel

%ifarch %{ix86}
BuildRequires: divx4linux
%endif

Obsoletes: %{name}-devel <= %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n gst-plugins-bad-%{version}
#patch0 -p1 -b .faad2

### Patch old gstreamer for new x264
%{__perl} -pi.orig -e 's|encoder->x264param.b_bframe_adaptive|encoder->x264param.i_bframe_adaptive|g' ext/x264/gstx264enc.c

### Use correct soundtouch pkgconfig package name
%{__perl} -pi.orig -e 's|libSoundTouch|soundtouch-1.0|g' configure

%build
%configure \
    --disable-gtk-doc \
    --disable-static \
    --enable-debug \
    --with-package-name="gst-plugins-bad %{desktop_vendor} rpm" \
    --with-package-origin="http://www.rpmforge.net/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang gst-plugins-bad-%{majorminor}

%clean
%{__rm} -rf %{buildroot}

%files -f gst-plugins-bad-%{majorminor}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README REQUIREMENTS
%{_libdir}/gstreamer-%{majorminor}/libgstalsaspdif.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrwb.so
%{_libdir}/gstreamer-%{majorminor}/libgstapp.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdirac.so
%ifarch %{ix86}
%{_libdir}/gstreamer-%{majorminor}/libgstdivxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdivxenc.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstflvdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeze.so
#%{_libdir}/gstreamer-%{majorminor}/libgstglimagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgsth264parse.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstmetadata.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg4videoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstmve.so
#%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstnsf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstoss4audio.so
#%{_libdir}/gstreamer-%{majorminor}/libgstpitch.so
#%{_libdir}/gstreamer-%{majorminor}/libgstqtdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstreal.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdl.so
#%{_libdir}/gstreamer-%{majorminor}/libgstsdlvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstselector.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeexresample.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
#%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so
%{_libdir}/gstreamer-%{majorminor}/libgsttrm.so
%{_libdir}/gstreamer-%{majorminor}/libgsttta.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so
#%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
#%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so
#%{_libdir}/gstreamer-%{majorminor}/libgstxingheader.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvid.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so

%{_libdir}/libgstapp-0.10.so.*

%exclude %{_libdir}/gstreamer-%{majorminor}/*.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gstreamer-%{majorminor}/
%{_libdir}/libgstapp-0.10.so
%exclude %{_libdir}/libgstapp-0.10.la

%changelog
* Thu Jul 09 2009 Dag Wieers <dag@wieers.com> - 0.10.8-3
- Rebuild against x264-0.4.20090708.

* Sun Apr 12 2009 Dag Wieers <dag@wieers.com> - 0.10.8-2
- Added divx support for arch i386 using divx4linux.

* Thu Apr 02 2009 Dag Wieers <dag@wieers.com> - 0.10.8-1
- Updated to release 0.10.8.

* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 0.10.3-8
- Rebuild against directfb-1.2.4.

* Wed Jul 09 2008 Dag Wieers <dag@wieers.com> - 0.10.3-7
- Rebuild against directfb-1.0.1.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.10.3-6
- Rebuild against libmpcdec 1.2.6.

* Thu Jun 14 2007 Dag Wieers <dag@wieers.com> - 0.10.3-5
- Disable swfdec.

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 0.10.3-4
- Remove (empty) devel package.
- Rebuild against swfdec 0.4.3 on EL5.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 0.10.3-3
- Update faad2 patch to also update the plugin sources, not just configure.

* Mon Dec 18 2006 Matthias Saou <http://freshrpms.net/> 0.10.3-2
- Try to rebuild against new wavpack 4.40 from Extras : Fails.
- Try to update to 0.10.3.2 pre-release : Fails, it needs a more recent gst.
- Try to include patch to update wavpack plugin source from 0.10.3.2
  pre-release : Fails to find wavpack/md5.h.
- Give up and disable wavpack support for now, sorry! Patches welcome.
- Include patch to fix faad2 2.5 detection.
- Add soundtouch support.

* Thu Jun  1 2006 Matthias Saou <http://freshrpms.net/> 0.10.3-1
- Update to 0.10.3.
- Add new translations.
- Add libgstmodplug.so, libgstvideo4linux2.so and libgstxingheader.so.
- Add new libmusicbrainz support.

* Thu Mar 23 2006 Matthias Saou <http://freshrpms.net/> 0.10.1-2
- Add libmms support, thanks to Daniel S. Rogers.

* Wed Feb 22 2006 Matthias Saou <http://freshrpms.net/> 0.10.1-1
- Update to 0.10.1.
- Add libgstcdxaparse.so and libgstfreeze.so.
- Enable libgstbz2.so, libgstglimagesink.so and libgstneonhttpsrc.so.

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

