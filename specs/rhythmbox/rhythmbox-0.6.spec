# $Id$
# Authority: matthias

# Do we build with mp3 and flac support?
%define id3tag 1
%define flac   1
# Enable "--with xine" conditional build
%{?_with_xine:  %{expand: %%define xine 1}}
%{!?_with_xine: %{expand: %%define xine 0}}

Name: rhythmbox
Summary: Music Management Application
Version: 0.6.10
Release: 0.2%{?_with_xine:xine}%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.rhythmbox.org/

#Source: ftp://ftp.gnome.org/pub/GNOME/sources/rhythmbox/0.6/%{name}-%{version}.tar.bz2
Source: http://dl.sf.net/rhythmbox/rhythmbox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: libvorbis-devel
BuildRequires: libmusicbrainz-devel >= 2.0.0
BuildRequires: gettext, scrollkeeper, gcc-c++
Requires: gtk2 >= 2.0.3
Requires: libgnomeui >= 2.0.0
Requires: eel2 >= 2.0.0

%if %{xine}
BuildRequires: xine-lib-devel >= 1.0.0
BuildRequires: faad2-devel
%else
BuildRequires: gstreamer-plugins-devel >= 0.6.2
%endif

%if %{id3tag}
BuildRequires: libid3tag-devel
%endif
%if %{flac}
BuildRequires: flac-devel
%endif

%description
Rhythmbox is an integrated music management application based on the powerful
GStreamer media framework. It has a number of features, including and easy to
use music browser, searching and sorting, comprehensive audio format support
through GStreamer, Internet Radio support, playlists and more.

%prep
%setup

%build
%configure %{?_with_xine:--enable-xine}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR="%{buildroot}"
%find_lang %name
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%{__rm} -f %{buildroot}%{_libdir}/bonobo/*.{a,la}

%{__rm} %{buildroot}%{_datadir}/rhythmbox/iradio-initial.pls
touch %{buildroot}%{_datadir}/rhythmbox/iradio-initial.pls

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="rhythmbox.schemas"
for S in $SCHEMAS; do
  gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S >/dev/null
done

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_sysconfdir}/gconf/schemas/rhythmbox.schemas
%{_datadir}/rhythmbox/*
%{_datadir}/applications/rhythmbox.desktop
%{_datadir}/pixmaps/rhythmbox.png
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/application-registry/*
%{_datadir}/gnome/help/rhythmbox
%{_datadir}/omf/rhythmbox/*
%{_datadir}/idl/Rhythmbox.idl
%{_datadir}/mime-info/rhythmbox.keys
%{_libdir}/bonobo/librb-nautilus-context-menu.so
%{_libdir}/bonobo/servers/*.server
%{_libdir}/pkgconfig/rhythmbox.pc

%changelog
* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 0.6.10-0.2
- Rebuild against newer faad2 2.7.

* Mon Mar 29 2004 Matthias Saou <http://freshrpms.net/> 0.6.10-0.1
- Update to 0.6.10.
- Use sf.net source URL for now since ftp.gnome.org isn't up-to-date.

* Mon Mar 15 2004 Matthias Saou <http://freshrpms.net/> 0.6.8-0.1
- Update to 0.6.8.

* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net/> 0.6.7-0.1
- Update to 0.6.7.

* Thu Jan 22 2004 Matthias Saou <http://freshrpms.net/> 0.6.5-0.1
- Update to 0.6.5.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 0.6.4-0.1
- Update to 0.6.4.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 0.6.3-0.1
- Update to 0.6.3.

* Thu Dec 18 2003 Matthias Saou <http://freshrpms.net/> 0.6.2-0.1
- Update to 0.6.2.

* Sat Nov 22 2003 Matthias Saou <http://freshrpms.net/> 0.6.1-0.1
- Update to 0.6.1.

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-0.1
- Rebuild for Fedora Core 1.
- Add xine backend build time support.
- Include xine backend fix patch.

* Tue Oct 28 2003 Jonathan Blandford <jrb@redhat.com> 0.5.4-1
- new version
- remove smp_flags

* Fri Oct 24 2003 Jonathan Blandford <jrb@redhat.com> 0.5.3-5
- remove the initial iradio channels as they all are mp3 based.

* Wed Oct  8 2003 Matthias Saou <matthias@rpmforge.net> 0.5.3-3
- Fix category from Development/Libraries to Applications/Multimedia.
- Use bz2 instead of gz as ftp.gnome.org has both, 300k saved in the src.rpm.
- Fix SCHEMES vs. SCHEMAS in the post scriplet.
- Added gstreamer-plugins-devel, libvorbis-devel, scrollkeeper and gettext deps.
- Removed unnecessary date expansion define.
- Updated description, including mp3 reference removal.
- Added libid3tag and flac optional support for convenient rebuild.
- Removed obsolete omf.make and xmldocs.make (included ones are the same now).

* Mon Sep 22 2003 Jonathan Blandford <jrb@redhat.com> 0.5.3-1
- new version
- use %{_sysconfdir} instead of /etc

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 18 2002 Jonathan Blandford <jrb@redhat.com>
- gave up on other archs for the Beta
- new version
- remove werror and add missing files

* Thu Nov  7 2002 Jeremy Katz <katzj@redhat.com>
- update to newer cvs snap

* Mon Sep 23 2002 Jeremy Katz <katzj@redhat.com>
- update to cvs snap

* Sun Sep 22 2002 Jeremy Katz <katzj@redhat.com>
- use %%(lang)

* Sun Aug 11 2002 Jeremy Katz <katzj@redhat.com>
- fix post to actually install the schema

* Sat Jun 22 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Added gconf file
- Added i18n directory

* Sat Jun 15 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Updated for new rewrite of rhythmbox, thanks to Jeroen

* Mon Mar 18 2002 Jorn Baayen <jorn@nl.linux.org>
- removed bonobo dependency

* Sat Mar 02 2002 Christian Schaller <Uraeus@linuxrising.org>
- created new spec file

