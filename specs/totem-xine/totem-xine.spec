# $Id$
# Authority: matthias

Summary: Movie player for GNOME 2 based on the Xine engine
Name: totem-xine
Version: 0.99.22
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.hadess.net/totem.php3
Source: http://ftp.gnome.org/pub/GNOME/sources/totem/0.99/totem-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): GConf2
Requires: gnome-desktop >= 2.6.0
%{!?_without_lirc:Requires: lirc}
BuildRequires: gcc-c++, pkgconfig, gettext, scrollkeeper
BuildRequires: xine-lib-devel >= 1.0.0
BuildRequires: gnome-desktop-devel >= 2.6.0, gnome-vfs2-devel, libglade2-devel
BuildRequires: nautilus-cd-burner-devel >= 2.8.1
BuildRequires: perl(XML::Parser)
%{!?_without_lirc:BuildRequires: lirc}
Conflicts: totem, totem-gstreamer

%description
Totem is simple movie player for the Gnome desktop based on xine. It features a
simple playlist, a full-screen mode, seek and volume controls, as well as
a pretty complete keyboard navigation.

Available rpmbuild rebuild options :
--without : lirc


%package -n mozilla-totem-xine
Summary: Totem plugin for multimedia playback in the mozilla web browser
Group: Applications/Multimedia
Requires: %{name} = %{version}
BuildRequires: mozilla-devel
Conflicts: mozilla-totem

%description -n mozilla-totem-xine
Totem is simple movie player for the Gnome desktop. It features a simple
playlist, a full-screen mode, seek and volume controls, as well as a pretty
complete keyboard navigation.

This package contains a plugin which embeds Totem inside the mozilla web
browser for multimedia playback.


%package -n vanity-xine
Summary: Simple webcam application
Group: Applications/Multimedia
Requires: gnome-desktop >= 2.6.0
Conflicts: vanity

%description -n vanity-xine
Vanity is a webcam application that is supposed to provide the same kind of
service the programs originally shipped with the webcam do. It features
watching and resizing live video.


%prep
%setup -n totem-%{version}


%build
%configure \
    --enable-vanity \
    --enable-mozilla \
    %{?_without_lirc:--disable-lirc}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
%find_lang totem


%post
scrollkeeper-update
update-desktop-database %{_datadir}/applications || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="totem.schemas totem-video-thumbnail.schemas"
for S in $SCHEMAS; do
  gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S >/dev/null
done

%postun
scrollkeeper-update
update-desktop-database %{_datadir}/applications || :


%clean
%{__rm} -rf %{buildroot}


%files -f totem.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/totem
%{_bindir}/totem-video-thumbnailer
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/totem-properties-page
%{_datadir}/application-registry/totem.applications
%{_datadir}/applications/totem.desktop
%{_datadir}/gnome/help/totem/
%{_datadir}/mime-info/totem.keys
%{_datadir}/omf/totem/
%{_datadir}/pixmaps/media-player-48.png
%{_datadir}/totem/
%exclude %{_datadir}/totem/vanity.*
%{_mandir}/man1/totem.1*

%files -n mozilla-totem-xine
%defattr(-, root, root, 0755)
%exclude %{_libdir}/mozilla/plugins/libtotem_mozilla.a
%exclude %{_libdir}/mozilla/plugins/libtotem_mozilla.la
%{_libdir}/mozilla/plugins/libtotem_mozilla.so
%{_libexecdir}/totem-mozilla-viewer

%files -n vanity-xine
%defattr(-, root, root, 0755)
%{_bindir}/vanity
%{_datadir}/applications/vanity.desktop
%{_datadir}/pixmaps/vanity.png
%dir %{_datadir}/totem/
%{_datadir}/totem/vanity.*


%changelog
* Fri Dec 10 2004 Matthias Saou <http://freshrpms.net/> 0.99.22-0
- Update to 0.99.22.

* Mon Nov  8 2004 Matthias Saou <http://freshrpms.net/> 0.99.20-1
- Quick strip of the spec to only build the Xine backend as FC ships with
  totem based on GStreamer dy default now.
- Rename all the (sub-)pachages *-xine and add conflicts.

* Mon Nov  1 2004 Matthias Saou <http://freshrpms.net/> 0.99.20-0
- Update to 0.99.20.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 0.99.19-0
- Update to 0.99.19.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 0.99.17-0
- Update to 0.99.17.
- Added scrollkeeper-update and update-desktop-database scriplet calls.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.99.15.1-1
- Updated to release 0.99.15.1.

* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 0.99.12-1
- Update to 0.99.12.
- Split off vanity at last.
- Enable mozilla plugin build and add mozilla-totem sub-package.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 0.99.11-1
- Update to 0.99.11.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 0.99.10-1
- Update to 0.99.10, rebuild against GNOME 2.6.

* Fri Feb 13 2004 Matthias Saou <http://freshrpms.net/> 0.99.9-1
- Update to 0.99.9, rebuild against gstreamer 0.7.4.
- New required perl-XML-Parser build dep (!?).
- Added missing defattr for the gstreamer sub-package.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.99.8-2
- Disable the obsolete xinitthreads patch.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.99.8-1
- Update to 0.99.8.
- Added help and omf files.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.99.7-2
- Rebuild for Fedora Core 1.

* Thu Oct 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.7.

* Tue Oct 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.6.
- Added missing build dependencies, thanks to mach.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.5.
- Now default to build the gstreamer package too.

* Thu Sep  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.4.
- Add if to the sub-package description to avoid build dep problem.

* Sun Jul 27 2003 Peter Oliver <rpms@mavit.freeserve.co.uk> 0.99.2-4.fr
- Fixed wrapper's handling of spaces in filenames.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Added gstreamer build option and sub-package + wrapper script.

* Tue Jul  8 2003 Matthias Saou <http://freshrpms.net/>
- Added an updated patch since the problem was in fact *not* fixed.

* Sat Jul  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.2.
- Removed the xinit threads patch.

* Sun Jun 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.1.

* Wed May 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.0.
- Added --without lirc build option.
- Added gnome-desktop-devel build dep and vanity desktop file.

* Sun May 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.98.0.
- Included new bonobo files.

* Tue Apr 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.97.0.
- Added xinitthreads patch to fix potential hang.

* Thu Apr 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.96.0.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Feb 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.95.1.

* Thu Jan 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90.0.
- Requirements (glib, libgnomeui) are too recent for Red Hat Linux 8.0.

* Wed Oct 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.0.
- Added the new xineplug_inp_gnomevfs modules.

* Mon Sep 30 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

