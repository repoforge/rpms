# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Frontend for the xine multimedia library
Name: gxine
Version: 0.5.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/

Source: http://dl.sf.net/xine/gxine-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, xine-lib-devel >= 1.0.0
BuildRequires: glib2-devel >= 2.6, mozilla-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: gtk2 >= 2.0, xine-lib >= 1.0.0

%description
xine is a fully-featured free audio/video player for unix-like systems which
uses libxine for audio/video decoding and playback. For more informations on
what formats are supported, please refer to the libxine documentation.
gxine is a gtk based gui for this xine-library alternate to xine-ui.

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup

%{__perl} -pi.orig -e 's|(\@XTEST_LIBS\@)|$1 \@X_LIBS\@|g' Makefile.in */Makefile.in

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >gxine.desktop
[Desktop Entry]
Name=GXine Movie Player
Comment=Play movies and songs
Icon=gxine.png
Exec=gxine
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;AudioVideo;
MimeType=video/mpeg;video/msvideo;video/quicktime;video/x-avi;video/x-ms-asf;video/x-ms-wmv;video/x-msvideo;application/x-ogg;application/ogg;audio/x-mp3;audio/x-mpeg;video/x-mpeg;video/x-fli;audio/x-wav;audio/x-mpegurl;audio/x-scpls;audio/x-ms-asx;application/vnd.rn-realmedia;audio/x-real-audio;audio/x-pn-realaudio;application/x-flac;audio/x-flac;application/x-shockwave-flash;audio/mpeg;audio/x-ms-asf;audio/x-m4a;audio/x-ms-wax;video/dv;video/x-anim;video/x-flc;misc/ultravox;application/x-matroska;audio/vnd.rn-realaudio;audio/x-pn-aiff;audio/x-pn-au;audio/x-pn-wav;audio/x-pn-windows-acm;image/vnd.rn-realpix;video/vnd.rn-realvideo
EOF

%{__cat} <<EOF >gxine.applications
gxine
	command=gxine
	name=GXine
	can_open_multiple_files=true
	expects_uris=yes
	requires_terminal=false
	all_gnome_vfs_schemes_supported=yes
	uses_gnomevfs=true
	startup_notify=false
	supported_uri_schemes=rtp,mms,net,rtsp,pnm
	mime_types=video/mpeg,video/msvideo,video/quicktime,video/x-avi,video/x-ms-asf,video/x-ms-wmv,video/x-msvideo,application/x-ogg,application/ogg,audio/x-mp3,audio/x-mpeg,video/x-mpeg,video/x-fli,audio/x-wav,audio/x-mpegurl,audio/x-scpls,audio/x-ms-asx,application/vnd.rn-realmedia,audio/x-real-audio,audio/x-pn-realaudio,application/x-flac,audio/x-flac,application/x-shockwave-flash,audio/mpeg,audio/x-ms-asf,audio/x-m4a,audio/x-ms-wax,video/dv,video/x-anim,video/x-flc,misc/ultravox,application/x-matroska,audio/vnd.rn-realaudio,audio/x-pn-aiff,audio/x-pn-au,audio/x-pn-wav,audio/x-pn-windows-acm,image/vnd.rn-realpix,video/vnd.rn-realvideo
EOF

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/gxine.png %{buildroot}%{_datadir}/pixmaps/gxine.png
%{__install} -Dp -m0644 gxine.applications %{buildroot}%{_datadir}/application-registry/gxine.applications

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 gxine.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/gxine.desktop
	%{__rm} -f %{buildroot}%{_datadir}/applications/gxine.desktop
%else
### Desktop entry
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --delete-original \
		--vendor %{desktop_vendor}                 \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		%{buildroot}%{_datadir}/applications/gxine.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%dir %{_sysconfdir}/gxine/
%config(noreplace) %{_sysconfdir}/gxine/gtkrc
%config(noreplace) %{_sysconfdir}/gxine/keypad.xml
%config(noreplace) %{_sysconfdir}/gxine/startup
%config(noreplace) %{_sysconfdir}/gxine/toolbar*.xml
%{_bindir}/gxine*
%{_libdir}/gxine/
#%exclude %{_libdir}/gxine/*.a
%exclude %{_libdir}/gxine/*.la
%{_mandir}/man1/gxine*.1*
%lang(de) %{_mandir}/de/man1/gxine*.1*
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gxine.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/gxine.desktop}
%{_datadir}/application-registry/gxine.applications
%{_datadir}/gxine/
%{_datadir}/pixmaps/gxine.png
%{_datadir}/icons/*/*/apps/gxine.png
%{_datadir}/locale/*/LC_MESSAGES/gxine.*

%changelog
* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Thu Dec 22 2005 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.3.3-3
- Added gxine.applications to application-registry.

* Mon Jun 07 2004 Dag Wieers <dag@wieers.com> - 0.3.3-3
- Added improved desktop file.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.3-2
- Rebuild for Fedora Core 1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.2.

* Sun Mar 16 2003 Matthias Saou <http://freshrpms.net/>
- Added freedesktop build option.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Sun Mar  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.

* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Converted desktop entry.

* Mon Dec 16 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- removed alle packman specific and added to gnome-xine cvs

* Sat Dec 07 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- Update to gxine 0.2

* Thu Dec 05 2002 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- initial release

