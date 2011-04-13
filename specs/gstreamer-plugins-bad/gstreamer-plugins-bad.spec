# $Id$
# Authority: dag
# ExclusiveDist: el6

%define _without_directfb 1

%{?el6:%define _without_jack 1}
%{?el6:%define _without_soundtouch 1}

%define desktop_vendor rpmforge

%define majorminor 0.10
%define gstreamer gstreamer

%define gst_minver 0.10.10.1
%define gstpb_minver 0.10.10.1

Summary: GStreamer streaming media framework "bad" plug-ins
Name: gstreamer-plugins-bad
Version: 0.10.19
Release: 3%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch0: gst-plugins-bad-0.10.4-faad2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}
Requires: %{gstreamer} >= %{gst_minver}

BuildRequires: bzip2-devel
%{!?_without_directfb:BuildRequires: directfb-devel}
BuildRequires: dirac-devel
BuildRequires: faac-devel
BuildRequires: faad2-devel
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: gsm-devel
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
BuildRequires: jasper-devel
BuildRequires: ladspa-devel
BuildRequires: libcdaudio-devel
BuildRequires: libdc1394-devel
BuildRequires: libdca-devel
BuildRequires: libid3tag-devel
BuildRequires: libkate-devel
BuildRequires: libmms-devel >= 0.5
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: liboil-devel
BuildRequires: libquicktime-devel
BuildRequires: libsndfile-devel
Buildrequires: libXt-devel
BuildRequires: mesa-libGLU-devel
%{!?_without_mjpegtools:BuildRequires: mjpegtools-devel}
BuildRequires: neon-devel
%{!?_without_orc:BuildRequires: orc-devel}
BuildRequires: PyXML
BuildRequires: SDL-devel
%{!?_without_schroedinger:BuildRequires: schroedinger}
%{!?_without_soundtouch:BuildRequires: soundtouch-devel}
#BuildRequires: swfdec-devel
Buildrequires: wavpack-devel
BuildRequires: x264-devel
BuildRequires: xvidcore-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.

%prep
%setup -n gst-plugins-bad-%{version}
#patch0 -p1 -b .faad2
### Use correct soundtouch pkgconfig package name
%{__perl} -pi.orig -e 's|libSoundTouch|soundtouch-1.0|g' configure

%build
%configure \
    --disable-static \
%{?_without_directfb:--disable-directfb} \
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
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstAmrwbEnc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdaudio.so
%{!?_without_orc:%{_libdir}/gstreamer-%{majorminor}/libgstcog.so}
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%{!?_without_directfb:%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so}
%{_libdir}/gstreamer-%{majorminor}/libgstdirac.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%{!?_without_jack:%{_libdir}/gstreamer-%{majorminor}/libgstjack.so}
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstqtmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstreal.so
%{!?_without_schroedinger:%{_libdir}/gstreamer-%{majorminor}/libgstschro.so}
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so
#%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so
%{_libdir}/gstreamer-%{majorminor}/libgsttrm.so
#%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvid.so
#%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so

%exclude %{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstalsaspdif.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstapexsink.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstaudioparsersbad.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstdccp.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstdtmf.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstfreeze.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgsth264parse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgsthdvparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstinvtelecine.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstjp2k.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstlegacyresample.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstliveadder.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmetadata.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmpeg4videoparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmpegdemux.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmve.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstnsf.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstrtpmux.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstscaletempoplugin.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstsdl.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstselector.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgsttta.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstvalve.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstvideomeasure.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%exclude %{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so

%exclude %{_libdir}/libgstbasevideo-%{majorminor}.so.*
%exclude %{_libdir}/libgstphotography-%{majorminor}.so.*
%exclude %{_libdir}/libgstsignalprocessor-%{majorminor}.so.*

%exclude %{_datadir}/gstreamer-%{majorminor}/camera-apps/gst-camera.ui
%exclude %{_includedir}/gstreamer-%{majorminor}/gst/
%exclude %{_libdir}/libgstbasevideo-%{majorminor}.so
%exclude %{_libdir}/libgstphotography-%{majorminor}.so
%exclude %{_libdir}/libgstsignalprocessor-%{majorminor}.so
%exclude %{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%exclude %{_libdir}/*.la
%exclude %{_libdir}/gstreamer-%{majorminor}/*.la

%changelog
* Sun Dec 05 2010 Dag Wieers <dag@wieers.com> - 0.10.19-3
- Disabled directfb support.

* Wed Nov 17 2010 Dag Wieers <dag@wieers.com> - 0.10.19-2
- Added libkate dependency.

* Sun Nov 14 2010 Dag Wieers <dag@wieers.com> - 0.10.19-1
- Updated to release 0.10.19.

* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 0.10.4-4
- Rebuild against newer faad2 2.7.

* Thu Jul 09 2009 Dag Wieers <dag@wieers.com> - 0.10.4-3
- Rebuild against x264-0.4.20090708.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.10.4-2
- Rebuild against libmpcdec 1.2.6.

* Wed Mar 30 2007 Matthias Saou <http://freshrpms.net/> 0.10.4-1
- Update to 0.10.4 for F7.
- Disable swfdec... does anything/anyone even use it here? Once it stabilizes
  somewhat more, maybe then it'll be worth re-enabling.
- Re-enable wavpack, it works again now.
- Enable libcdaudio support.
- Enable jack support.
- Enable ladspa support.
- Enable mpeg2enc (mjpegtools) support.
- Remove no longer present libgstvideo4linux2.so and add all new plugins.
- Remove all gtk-doc references (all gone...?) and devel package too.

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

