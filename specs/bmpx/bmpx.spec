# $Id$
# Authority: matthias
# ExclusiveDist: fc6 el5

Summary: Beep Media Player
Name: bmpx
Version: 0.36.1
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.beep-media-player.org/
Source: http://files.beep-media-player.org/releases/0.36/bmpx-%{version}.tar.bz2
Patch0: bmpx-0.36.0-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: gettext-devel, libXt-devel
BuildRequires: gstreamer-devel >= 0.10.4, gcc-c++
BuildRequires: gstreamer-plugins-base-devel >= 0.10.4
BuildRequires: dbus-devel, hal-devel, gamin-devel, libmusicbrainz-devel
BuildRequires: taglib-devel, neon-devel, libmp4v2-devel, libsidplay-devel
BuildRequires: boost-devel, glibmm24-devel, gtkmm24-devel, libglademm24-devel
BuildRequires: startup-notification-devel, sqlite-devel, alsa-lib-devel
BuildRequires: libnotify-devel, librsvg2-devel, cdparanoia-devel
# Needed for libhrel
BuildRequires: flex, bison

%description
BMPx is an audio player that features support for specifications like XDS DnD,
XSPF and DBus. BMPx is highly interoperable and integrates well with other
applications and a variety of desktop environments.


%package devel
Summary: Development files for the BMPx media player
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
Development files required for compiling BMPx media player plugins.


%prep
%setup
%patch0 -p1 -b .install


%build
%define optflags -Os
%configure \
    --disable-rpath \
    --enable-hal \
    --enable-mp4v2 \
    --enable-sid
# Remove %{?_smp_mflags} as the build takes up 2GB RAM with -j4
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Don't include this file as it's part of glibc-common
%{__rm} -f %{buildroot}%{_datadir}/locale/locale.alias


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &>/dev/null || :
update-mime-database  %{_datadir}/mime &>/dev/null || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &>/dev/null || :
update-mime-database  %{_datadir}/mime &>/dev/null || :


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/beep-media-player-2
%{_bindir}/bmp2
%{_bindir}/bmp-enqueue-files-2.0
%{_bindir}/bmp-enqueue-uris-2.0
%{_bindir}/bmp-play-files-2.0
%{_bindir}/bmp-play-lastfm-2.0
%{_libdir}/bmpx/
%exclude %{_libdir}/bmpx/plugins/*/*/*.la
%{_libexecdir}/beep-media-player-2-bin
%{_libexecdir}/beep-media-player-2-sentinel
%{_datadir}/applications/bmp-2.0.desktop
%{_datadir}/applications/bmp-2.0-offline.desktop
%{_datadir}/applications/bmp-enqueue-2.0.desktop
%{_datadir}/applications/bmp-play-2.0.desktop
%{_datadir}/bmpx/
%{_datadir}/dbus-1/services/org.beepmediaplayer.bmp.service
%{_datadir}/dbus-1/services/org.beepmediaplayer.sentinel.service
%{_datadir}/icons/hicolor/48x48/apps/bmpx.png
%{_mandir}/man1/beep-media-player-2.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/bmp-2.0/
%{_libdir}/pkgconfig/bmp-2.0.pc


%changelog
* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 0.36.1-2
- Rebuild against plain libmp4v2 instead of full faad2.

* Thu Dec 14 2006 Matthias Saou <http://freshrpms.net/> 0.36.1-1
- Update to 0.36.1.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 0.36.0-1
- Update to 0.36.0.
- Update install patch so that it still applies.
- Add new librsvg2-devel and cdparanoia-devel build requirements.
- Add new sentinel related files and remove no longer installed icon and mime.

* Mon Oct  2 2006 Matthias Saou <http://freshrpms.net/> 0.32.0-1
- Update to 0.32.0.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.30.3-1
- Update to 0.30.3.

* Mon Sep 25 2006 Matthias Saou <http://freshrpms.net/> 0.30.1-1
- Update to 0.30.1.

* Fri Jul 21 2006 Matthias Saou <http://freshrpms.net/> 0.20.3-1
- Update to 0.20.3.
- Drop no longer needed binpath patch.
- Remove no longer included bmp2 from bindir.

* Tue Jul 11 2006 Matthias Saou <http://freshrpms.net/> 0.20.2-1
- Update to 0.20.2.
- Enable M4A/AAC tag support with faad2.
- Enable SID/PSID taglib support with libsidplay.

* Sun Jul  9 2006 Matthias Saou <http://freshrpms.net/> 0.20.0-1
- Update to 0.20.0 final.
- Include patch to fix "bmp2" symlink to the build root.

* Tue Jul  4 2006 Matthias Saou <http://freshrpms.net/> 0.20-0.2.beta1.
- Update to 0.20beta1... first time I see "beta" _after_ "pre" releases...

* Mon Jun 26 2006 Matthias Saou <http://freshrpms.net/> 0.20-0.1.pre7
- Update to 0.20pre7.
- Add update-mime-database scriplet calls now that there is a mime types file.
- Remove installed locale.alias file (it's part of glibc-common).

* Sun Jun 25 2006 Matthias Saou <http://freshrpms.net/> 0.20-0.1.pre6
- Update to 0.20pre6.

* Thu Jun 22 2006 Matthias Saou <http://freshrpms.net/> 0.20-0.1.pre2
- Update to 0.20pre2.
- Add new libnotify-devel build requirement, but as 0.4.2 is required...

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.20-0.1.pre1
- Update to 0.20pre1.
- Update all build requirements for new c++ deps : boost and gtkmm stuff.
- Update %%files sections, notably for the removal of libs, hrel and chroma.

* Thu May  4 2006 Matthias Saou <http://freshrpms.net/> 0.14.4-1
- Update to 0.14.4.

* Tue Apr 11 2006 Matthias Saou <http://freshrpms.net/> 0.14.3-2
- Include COPYING file.
- Add update-desktop-database scriplet calls and post/postun deps.

* Wed Mar 29 2006 Matthias Saou <http://freshrpms.net/> 0.14.3-1
- Update to 0.14.3.

* Mon Mar 06 2006 Matthias Saou <http://freshrpms.net/> 0.14.2-1
- Major spec file cleanup, based on package from futurepast.free.fr (which
  contained no changelog).

