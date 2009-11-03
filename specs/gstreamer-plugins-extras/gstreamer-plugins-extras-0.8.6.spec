# $Id: gstreamer-plugins-extras.spec 5241 2007-03-25 20:32:19Z dag $
# Authority: matthias

# ExclusiveDist: el4


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define gst_minver 0.8.6.1
%define gstp_minver 0.8.7
%define majorminor 0.8
%define gstreamer gstreamer
%define register %{_bindir}/gst-register-%{majorminor}

# gst plugins we want (this is passed to configure with spaces converted to
# commas, don't mangle them)
%define gstplugs mpeg1sys mpeg1videoparse mpeg2sub mpegaudio mpegaudioparse mpegstream
# external plugin directories that we want built
%define extplug_dirs a52dec dvdnav dvdread faad gsm lame libfame mad mpeg2dec swfdec
# corresponding external plugin names
%define extplug_names a52dec dvdnavsrc dvdreadsrc faad gsmenc gsmdec lame libfame mad mpeg2dec swfdec

Summary: GStreamer streaming media framework extra plugins
Name: gstreamer-plugins-extra
Version: 0.8.6
Release: 3%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.net/
Source: http://gstreamer.freedesktop.org/src/gst-plugins/gst-plugins-%{version}.tar.bz2
Patch0: gst-plugins-0.8.6-faad2-test.patch
Patch1: gst-plugins-0.8.8-mpcdec.patch
Patch2: gst-plugins-0.8.6-dvdread.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
# libtool needs this, sigh
BuildRequires: gcc-c++
# so gst-libs can build
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
# so configure passes
BuildRequires: GConf2-devel
# because we patch configure.in
BuildRequires: autoconf, automake, libtool, gettext-devel, which, cvs

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.


%package audio
Summary: Extra audio plugins for GStreamer
Group: Applications/Multimedia

BuildRequires: a52dec-devel >= 0.7.3
BuildRequires: faad2-devel >= 2.0
BuildRequires: gsm-devel >= 1.0.10
BuildRequires: lame-devel >= 3.89
BuildRequires: libmad-devel >= 0.15.0, libid3tag-devel >= 0.15.0
BuildRequires: libmpcdec-devel >= 1.2
BuildRequires: libmusepack-devel

Requires: %{gstreamer}-plugins >= %{gstp_minver}
Requires(pre): %{register}
Requires(post): %{register}

Provides: %{gstreamer}-a52dec = %{version}-%{release}
Provides: %{gstreamer}-faad = %{version}-%{release}
Provides: %{gstreamer}-gsm = %{version}-%{release}
Provides: %{gstreamer}-lame = %{version}-%{release}
Provides: %{gstreamer}-mad = %{version}-%{release}
Provides: %{gstreamer}-musepack = %{version}-%{release}

%description audio
This package contains extra audio plugins for GStreamer, including :
- a52 decoding
- faad2 decoding
- gsm decoding
- lame mp3 encoding
- mad mp3 decoding

%post audio
%{register} &>/dev/null || :

%postun audio
%{register} &>/dev/null || :

%files audio
%defattr(-, root, root, 0755)
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so


%package dvd
Summary: DVD plugins for GStreamer
Group: Applications/Multimedia

BuildRequires: libdvdnav-devel >= 0.1.3
BuildRequires: libdvdread-devel >= 0.9.0

Requires: %{gstreamer}-plugins >= %{gstp_minver}
Requires: %{gstreamer}-plugins-extra-audio >= %{gstp_minver}
Requires: %{gstreamer}-plugins-extra-video >= %{gstp_minver}
Requires(pre): %{register}
Requires(post): %{register}

Provides: %{gstreamer}-dvd = %{version}-%{release}
Provides: %{gstreamer}-dvdnavsrc = %{version}-%{release}
Provides: %{gstreamer}-dvdreadsrc = %{version}-%{release}

%description dvd
This package contains dvd plugins for GStreamer, including :
- libdvdnav
- libdvdread

%post dvd
%{register} &>/dev/null || :

%postun dvd
%{register} &>/dev/null || :

%files dvd
%defattr(-, root, root, 0755)
%{_libdir}/gstreamer-%{majorminor}/libgstdvdnavsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdreadsrc.so


%package video
Summary: Extra video plugins for GStreamer
Group: Applications/Multimedia

BuildRequires: libfame-devel >= 0.9.1
BuildRequires: mpeg2dec-devel >= 0.4.0
BuildRequires: swfdec-devel >= 0.3.1

Requires: %{gstreamer}-plugins >= %{gstp_minver}
Requires: %{gstreamer}-plugins-extra-audio >= %{gstp_minver}
Requires(pre): %{register}
Requires(post): %{register}

Provides: %{gstreamer}-libfame = %{version}-%{release}
Provides: %{gstreamer}-mpeg2dec = %{version}-%{release}
Provides: %{gstreamer}-swfdec = %{version}-%{release}

%description video
This package contains extra video plugins for GStreamer, including :
- libfame MPEG video encoding
- mpeg2dec MPEG-2 decoding

%post video
%{register} &>/dev/null || :

%postun video
%{register} &>/dev/null || :

%files video
%defattr(-, root, root, 0755)
%{_libdir}/gstreamer-%{majorminor}/libgstlibfame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstmp1videoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg1systemencode.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2subt.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegstream.so
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so


%prep
%setup -n gst-plugins-%{version}
%patch0 -p1 -b .faad2
#patch1 -p0 -b .mpcdec
%patch2 -p1 -b .dvdread


%build
./autogen.sh --noconfigure
%configure \
    --with-package-name='Fedora freshrpms rpm' \
    --with-package-origin='http://freshrpms.net/' \
    --with-plugins=$(echo %{gstplugs} | sed 's/ /,/g') \
    --enable-debug \
    --enable-DEBUG \
    --disable-tests \
    --disable-examples

# Die if any of the external plugins we want aren't configured properly
# This will fail silently if the configure script stops printing the
# "These plugins will not be built: blah blah blah" messages.
grep -oP "(?<=will not be built: )[[:alpha:] ]+" config.log | sort > notbuilt
BADPLUGS=$(echo %{extplug_names} | xargs -n1 echo | sort | join - notbuilt)
if [ "$BADPLUGS" != "" ]; then
 echo "Plugins not configured: $BADPLUGS"
 exit 1;
fi

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}

# We're better off manually installing the plugins we want to package

cd gst
for p in %{gstplugs}
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

cd ext
for p in %{extplug_dirs}
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

# Clean out files that should not be part of the rpm.
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.{a,la}


%clean
%{__rm} -rf %{buildroot}


%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.8.6-3
- Rebuild against libmpcdec 1.2.6.

* Mon Mar 26 2007 Dag Wieers <dag@wieers.com> - 0.8.6-2
- Updated to release 0.8.6.

* Wed Feb 23 2005 Matthias Saou <http://freshrpms.net/> 0.8.6-2
- Further fixes by Nicholas Miell merged at last.
- Disable swfdec for now, it's more hassles than it is useful.
- Disable musepack, as the plugin doesn't work with 1.1 (only 1.0).
- Rebuild against new libmusepack library.

* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net/> 0.8.6-1
- Include all changes by Nicholas Miell :
- Fix for faad2 detection (new and old).
- Have build die if any of the requested plugins aren't configured properly,
  since they could get built (because of the short circuiting of the built)
  but be totally broken.

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 0.8.6-0
- Update to 0.8.6.
- Sync with Thomas's current spec file.

* Mon Nov 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5.3-0.lvn.1
- new prerelease

* Wed Oct 06 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5-0.lvn.1: new release
- added GConf2 requirement to pass configure

* Tue Aug 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.4-0.lvn.1: new release

* Fri Aug 27 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3.2-0.lvn.1: new prerelease

* Mon Aug 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3-0.lvn.1: new source release

* Fri Jul 30 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.2.2-0.lvn.1: new prerelease

* Wed Jun 23 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.2-0.lvn.1: new source release

* Fri Jun 18 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1.2-0.lvn.1: new source prerelease

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.lvn.1: new source release

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: new source release, change base name to gstreamer

* Tue Mar 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.6-0.lvn.1: new source release

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.2: sync with FreshRPMS

* Tue Mar 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.1: First package for rpm.livna.org
