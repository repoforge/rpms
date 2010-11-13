# $Id$
# Authority: matthias

Summary: Real-time visual space simulation
Name: celestia
Version: 1.3.2
Release: 2%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://www.shatters.net/celestia/
Source: http://dl.sf.net/celestia/celestia-%{version}.tar.gz
Patch0: celestia-1.3.2-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgnomeui-devel, gtkglext-devel, freeglut-devel
BuildRequires: libpng-devel, libjpeg-devel, gcc-c++, zlib-devel
BuildRequires: gtk2-devel
Requires(post): GConf2
Requires(preun): GConf2

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
%patch0 -p1 -b .gcc34
%{__perl} -pi -e "s|StarDetails::StarDetails|StarDetails|g;" src/celengine/star.h
%{__perl} -pi -e "s|CommandGotoLongLat::CommandGotoLongLat|CommandGotoLongLat|g;" src/celengine/command.h

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure --with-gnome
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR=%{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :

%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/celestia.schemas &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog controls.txt COPYING NEWS README TODO
%{_sysconfdir}/gconf/schemas/celestia.schemas
%{_bindir}/celestia
%{_datadir}/applications/celestia.desktop
%dir %{_datadir}/celestia/
%config %{_datadir}/celestia/celestia.cfg
%{_datadir}/celestia/celestia.png
%doc %{_datadir}/celestia/controls.txt
%{_datadir}/celestia/data/
%{_datadir}/celestia/*.cel
%{_datadir}/celestia/extras/
%{_datadir}/celestia/fonts/
%doc %{_datadir}/celestia/manual/
%{_datadir}/celestia/models/
%{_datadir}/celestia/shaders/
%{_datadir}/celestia/textures/
%{_datadir}/pixmaps/celestia.png
%exclude %{_datadir}/celestia/COPYING

%changelog
* Wed Nov 23 2005 Matthias Saou <http://freshrpms.net/> 1.3.2-2
- Add -fno-strict-aliasing since -O2 breaks things (rh#171636).

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-1
- Added GCC 3.4 patch from Marius L. Jøhndal.
- Back from the kde to the gnome version.
- Remove translations, as they seem to be only for the kde version (?).

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

