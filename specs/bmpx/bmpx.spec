# $Id$
# Authority: matthias

# ExclusiveDist: fc5

%define prever pre1

Summary: Media player with the WinAmp GUI
Name: bmpx
Version: 0.20
Release: 0.1.%{prever}
License: GPL
Group: Applications/Multimedia
URL: http://www.beep-media-player.org/
Source: http://dl.sf.net/beepmp/bmpx-%{version}%{?prever}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: gettext-devel, libXt-devel
BuildRequires: gstreamer-devel >= 0.10.4
BuildRequires: gstreamer-plugins-base-devel >= 0.10.4
BuildRequires: dbus-devel, hal-devel, gamin-devel, libmusicbrainz-devel
BuildRequires: taglib-devel, neon-devel
BuildRequires: boost-devel, glibmm24-devel, gtkmm24-devel, libglademm24-devel
BuildRequires: startup-notification-devel, sqlite-devel, alsa-lib-devel
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
%setup -n %{name}-%{version}%{?prever}


%build
%configure \
    --enable-hal \
    --enable-amazon
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &>/dev/null ||:

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &>/dev/null ||:


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/beep-media-player-2
%{_bindir}/bmp-enqueue-files-2.0
%{_bindir}/bmp-enqueue-uris-2.0
%{_bindir}/bmp-play-files-2.0
%{_libdir}/bmpx/
%exclude %{_libdir}/bmpx/plugins/*/*.la
%{_libexecdir}/beep-media-player-2-bin
%{_datadir}/applications/bmp-2.0.desktop
%{_datadir}/applications/bmp-enqueue-2.0.desktop
%{_datadir}/applications/bmp-play-2.0.desktop
%{_datadir}/bmpx/
%{_datadir}/dbus-1/services/org.beepmediaplayer.bmp.service
%{_datadir}/icons/hicolor/48x48/apps/bmpx.png
%{_mandir}/man1/beep-media-player-2.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/bmp-2.0/
%{_libdir}/pkgconfig/bmp-2.0.pc


%changelog
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

