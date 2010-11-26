# $Id$
# Authority: dries

# Screenshot: http://kaffeine.sourceforge.net/pics/05/kaffeine05-1.png
# ScreenshotURL: http://kaffeine.sourceforge.net/screenshots.html

%{?el4:%define _kdelibs_without_mplayer2_desktop_file 1}
%{?el4:%define _without_gstreamer 1}
%{?el4:%define _without_modxorg 1}

%{?el3:%define _kdelibs_without_mplayer2_desktop_file 1}
%{?el3:%define _without_gstreamer 1}
%{?el3:%define _without_modxorg 1}

Summary: Media player based on xine-lib
Name: kaffeine
Version: 1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://kaffeine.sourceforge.net/

Source: http://dl.sf.net/project/kaffeine/kaffeine/kaffeine-%{version}/kaffeine-%{version}.tar.gz
#Source: http://dl.sf.net/kaffeine/kaffeine-%{version}.tar.bz2
#Source: http://hftom.free.fr/kaffeine-%{version}.tar.bz2
Source1: kaffeine.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kdelibs4-devel
%{?el4:BuildRequires: libselinux-devel}
BuildRequires: libvorbis-devel
BuildRequires: xine-lib-devel >= 1.0.0
%{!?_without_modxorg:BuildRequires: libXext-devel libXinerama-devel libXtst-devel libXScrnSaver-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_gstreamer:BuildRequires: gstreamer-devel >= 0.10}
%{!?_without_gstreamer:BuildRequires: gstreamer-plugins-base-devel >= 0.10}

Obsoletes: kaffeine-libs < 1.0
Obsoletes: kaffeine-devel < 1.0
Requires: kdebase-runtime
%{?_kde4_version:Requires: kdelibs4 >= %{_kde4_version}}

%description
Kaffeine is a simple and easy to use media player based on the xine-lib and
full integrated in KDE3. It supports drag and drop and provides an editable
playlist, a Konqueror plugin, a Mozilla plugin, OSD, and much more.

%prep
%setup

%build
%{cmake_kde4}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install/fast DESTDIR="%{buildroot}"

%{__mv} %{buildroot}%{_kde4_iconsdir}/oxygen %{buildroot}%{_kde4_iconsdir}/hicolor

%{__install} -Dp -m644 %{SOURCE1} %{buildroot}%{_kde4_iconsdir}/hicolor/48x48/apps/kaffeine.png

%find_lang %{name} --with-kde

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :
touch --no-create %{_kde4_iconsdir}/hicolor &>/dev/null || :
gtk-update-icon-cache -q %{_kde4_iconsdir}/icons/hicolor 2>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    update-desktop-database %{_datadir}/applications &>/dev/null ||:
    touch --no-create %{_kde4_iconsdir}/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog COPYING* INSTALL NOTES TODO
%{_kde4_bindir}/kaffeine
%{_kde4_bindir}/kaffeine-xbu
%{_kde4_appsdir}/kaffeine/
%{_kde4_appsdir}/solid/actions/*.desktop
%{_kde4_datadir}/applications/kde4/kaffeine.desktop
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_appsdir}/profiles/kaffeine.profile.xml

%changelog
* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

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

