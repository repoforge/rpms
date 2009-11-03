# $Id$
# Authority: dries

# Screenshot: http://kaffeine.sourceforge.net/pics/05/kaffeine05-1.png
# ScreenshotURL: http://kaffeine.sourceforge.net/screenshots.html

##ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%{?el4:%define _without_gstreamer 1}
%{?el3:%define _without_gstreamer 1}

%{?el4:%define _kdelibs_without_mplayer2_desktop_file 1}
%{?el3:%define _kdelibs_without_mplayer2_desktop_file 1}

Summary: Media player based on xine-lib
Name: kaffeine
Version: 0.8.7
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kaffeine.sourceforge.net/

Source: http://dl.sf.net/kaffeine/kaffeine-%{version}.tar.bz2
#Source: http://hftom.free.fr/kaffeine-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kdelibs-devel
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
BuildRequires: libvorbis-devel
BuildRequires: xine-lib-devel >= 1.0.0
%{!?_without_modxorg:BuildRequires: libXext-devel libXinerama-devel libXtst-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_gstreamer:BuildRequires: gstreamer-devel >= 0.10}
%{!?_without_gstreamer:BuildRequires: gstreamer-plugins-base-devel >= 0.10}

%description
Kaffeine is a simple and easy to use media player based on the xine-lib and
full integrated in KDE3. It supports drag and drop and provides an editable
playlist, a Konqueror plugin, a Mozilla plugin, OSD, and much more.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### Fix 0.8.6 references throughout sources
grep -rl 'kaffeine-0.8.6' . | xargs perl -pi -e 's|kaffeine-0.8.6|kaffeine-%{version}|g'

%build
source /etc/profile.d/qt.sh
export CPPFLAGS="-I%{_includedir}/cdda"
%configure \
%{?_without_gstreamer:--without-gstreamer}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}-%{version}

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :
update-desktop-database &>/dev/null || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :
update-desktop-database &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-%{version}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_datadir}/doc/HTML/*/kaffeine
%{_bindir}/kaffeine
%{_datadir}/applications/kde/kaffeine.desktop
%{_datadir}/apps/gstreamerpart/gstreamer_part.rc
%{_datadir}/apps/kaffeine/
%{_datadir}/apps/konqueror/servicemenus/kaffeine*.desktop
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mimelnk/application/*.desktop
%{!?_kdelibs_without_mplayer2_desktop_file:%exclude %{_datadir}/mimelnk/application/x-mplayer2.desktop}
%{_datadir}/services/gstreamer_part.desktop
%{_datadir}/services/kaffeinemp3lame.desktop
%{_datadir}/services/kaffeineoggvorbis.desktop
%{_datadir}/services/xine_part.desktop
%{_datadir}/servicetypes/kaffeineaudioencoder.desktop
%{_datadir}/servicetypes/kaffeinedvbplugin.desktop
%{_datadir}/servicetypes/kaffeineepgplugin.desktop
%{_libdir}/kde3/libgstreamerpart.la
%{_libdir}/kde3/libgstreamerpart.so
%{_libdir}/kde3/libkaffeinemp3lame.la
%{_libdir}/kde3/libkaffeinemp3lame.so
%{_libdir}/kde3/libkaffeineoggvorbis.la
%{_libdir}/kde3/libkaffeineoggvorbis.so
%{_libdir}/kde3/libxinepart.la
%{_libdir}/kde3/libxinepart.so
%{_libdir}/libkaffeineaudioencoder.la
%{_libdir}/libkaffeineaudioencoder.so.*
%{_libdir}/libkaffeinedvbplugin.la
%{_libdir}/libkaffeinedvbplugin.so.*
%{_libdir}/libkaffeinepart.la
%{_libdir}/libkaffeinepart.so
%{_libdir}/libkaffeineepgplugin.la
%{_libdir}/libkaffeineepgplugin.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kaffeine/
%{_libdir}/libkaffeineaudioencoder.so
%{_libdir}/libkaffeinedvbplugin.so
%{_libdir}/libkaffeineepgplugin.so

%changelog
* Sun Sep 06 2009 Dag Wieers <dag@wieers.com> - 0.8.7-1
- Updated to release 0.8.7.

* Sat Sep 05 2009 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sun Mar 02 2008 Dries Verachtert <dries@ulyssis.org> - 0.7.1-2
- Added exclude for the mplayer2 desktop file for newer kdelibs versions.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 0.7-1
- Update to 0.7, which doesn't build on FC4 it seems.
- Remove unnecessary build requirements.

* Sun Mar 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-2
- Added a devel subpackage so it can update and can be updated by
  the kaffeine package of kde-redhat.

* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.

