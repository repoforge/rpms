# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_arts 1}
%{?rh9:%define _without_arts 1}
%{?rh8:%define _without_arts 1}
%{?rh7:%define _without_arts 1}

%define desktop_vendor rpmforge

Summary: Real-time visual space simulation
Name: celestia
Version: 1.3.2
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://www.shatters.net/celestia/
Source: http://dl.sf.net/celestia/celestia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: freeglut-devel, kdelibs-devel
BuildRequires: libpng-devel, libjpeg-devel, fam-devel
BuildRequires: desktop-file-utils, unzip, gcc-c++, libstdc++-devel

%{!?dist:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
%{!?_without_arts:BuildRequires: arts-devel}

%description
Celestia is a free real-time space simulation that lets you experience our
universe in three dimensions. Unlike most planetarium software, Celestia
doesn't confine you to the surface of the Earth. You can travel throughout
the solar system, to any of over 100,000 stars, or even beyond the galaxy.
All travel in Celestia is seamless; the exponential zoom feature lets you
explore space across a huge range of scales, from galaxy clusters down to
spacecraft only a few meters across. A 'point-and-goto' interface makes it
simple to navigate through the universe to the object you want to visit.

%prep
%setup


%build
%configure \
    --with-kde \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --with-qt-libraries="${QTDIR}/lib"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_SCHEMA_FILE_DIR="%{buildroot}%{_sysconfdir}/gconf/schemas"
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category Graphics \
    --delete-original \
    %{buildroot}%{_datadir}/applnk/Edutainment/Science/celestia.desktop


%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :


%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/celestia
%{_datadir}/applications/%{desktop_vendor}-celestia.desktop
%dir %{_datadir}/apps/celestia/
%config %{_datadir}/apps/celestia/celestia.cfg
%config %{_datadir}/apps/celestia/bookmarks.xml
%doc %{_datadir}/apps/celestia/controls.txt
%doc %{_datadir}/apps/celestia/COPYING
%config %{_datadir}/apps/celestia/celestiaui.rc
%{_datadir}/apps/celestia/*.cel
%{_datadir}/apps/celestia/celestia-splash.jpg
%{_datadir}/apps/celestia/celestia.png
%{_datadir}/apps/celestia/data/
%{_datadir}/apps/celestia/extras/
%{_datadir}/apps/celestia/favicons/
%{_datadir}/apps/celestia/fonts
%doc %{_datadir}/apps/celestia/manual
%{_datadir}/apps/celestia/models/
%{_datadir}/apps/celestia/shaders/
%{_datadir}/apps/celestia/textures/
%config %{_datadir}/config/celestiarc
%doc %{_defaultdocdir}/HTML/en/celestia/
%{_datadir}/icons/hicolor/*/apps/celestia.png
%{_datadir}/mimelnk/application/x-celestia-script.desktop
%{_datadir}/services/celestia.protocol
%{_sysconfdir}/gconf/schemas/celestia.schemas


%changelog
* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> -  1.3.2-1
- Updated to release 1.3.2.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.3.1-2
- Add Qt lib fix for x86_64 build.

* Thu Jul  8 2004 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Switch from gtk to kde GUI for now, as the gtk build seems broken.
- Remove the additionnal extras, they're now bundled in.
- Major spec update to finalize 1.3.1 changes.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Update to 1.3.1.
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Rebuild for Fedora Core 1.

* Thu Apr 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.3.0.
- Added numberedmoons.ssc addon.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.5.
- Included "Minor Moons of the Giant Planets" extra file.
- New icon from the KDE part of the source.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New style menu entry.

* Wed Jul  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt to remove the NVidia dependency (oops!).

* Wed May 15 2002 Matthias Saou <http://freshrpms.net/>
- Sorry, I'm a maniac ;-)

* Tue May 14 2002 Julien MOUTTE <julien@moutte.net>
- Initial RPM release.

