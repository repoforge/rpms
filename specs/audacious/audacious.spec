# $Id$
# Authority: hadams

%define desktop_vendor rpmforge
%define plugin_version 1.4.5

Summary: Graphical media player similar to xmms
Name: audacious
Version: 1.4.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/

#Source0: http://static.audacious-media-player.org/release/audacious-%{version}.tgz
Source0: http://distfiles.atheme.org/audacious-%{version}.tbz2
Patch0: audacious-1.3.1-xmms-skins.patch
Patch1: audacious-1.4.0-default-skin.patch
#Patch2: audacious-1.1.0-no-rpath.patch
Patch3: audacious-1.2.1-relative-links.patch
#Patch4: audacious-1.1.0-quoting.patch
#Patch5: audacious-1.1.0-amidi-backend.patch
Patch6: audacious-1.2.1-shaded-skin.patch
#Patch7: audacious-1.1.1-controlsocket-name.patch
#Patch8: audacious-1.1.1-playlist-twenty.patch
Patch9: audacious-1.4.2-id3tag-close-file.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils >= 0.9
BuildRequires: GConf2-devel
BuildRequires: gettext
BuildRequires: gtk2-devel >= 2.6
BuildRequires: libglade2-devel >= 2.4
BuildRequires: libmowgli-devel >= 0.4
BuildRequires: libmcs-devel >= 0.4.1
BuildRequires: zlib-devel

Requires: audacious-plugins >= %{plugin_version}
Requires: desktop-file-utils >= 0.9

Obsoletes: bmp <= 0.9.7.1
Provides: bmp = 0.9.7.1

%description
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on BMP.

%package libs
Summary: Library files for Audacious
Group: System Environment/Libraries
Requires: /sbin/ldconfig

%description libs
Library files for Audacious

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
Requires: GConf2-devel
Requires: glib2-devel
Requires: gtk2-devel >= 2.6
Requires: libglade2-devel >= 2.4
Requires: libmowgli-devel >= 0.4
Requires: libmcs-devel >= 0.4.1
Requires: pkgconfig

Obsoletes: bmp-devel <= 0.9.7.1
Provides: bmp-devel = 0.9.7.1

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

# Read xmms skins directory
%patch0 -p1 -b .xmms-skins

# Use bluecurve as default skin
%patch1 -p1 -b .default-skin

# No rpath in binaries
# %patch2 -p1 -b .no-rpath

# Relative symlink paths
# %patch3 -p1 -b .relative-links

# Filename quoting
# %patch4 -p1 -b .quoting

# Amidi backends path
# %patch5 -p1 -b .amidi-backend

# Shaded playlist window decorations
# %patch6 -p1 -b .shaded-skin

# Controlsocket named "xmms" instead of "audacious"
# %patch7 -p1 -b controlsocket-name

# Fix "%20" in playlist entries
# %patch8 -p1 -b playlist-twenty

%{__perl} -pi -e 's|^\.SILENT:.*$||' buildsys.mk.in

%build
%configure \
    --disable-dependency-tracking \
    --disable-gnome-vfs \
    --disable-rpath \
    --enable-chardet \
    --enable-dbus \
    --enable-gconf
%{__make} %{?_smp_mflags} V="1"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/audacious.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/audacious.png

desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications  \
    --vendor %{desktop_vendor} \
    %{buildroot}%{_datadir}/applications/audacious.desktop

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/audacious.1*
%doc %{_mandir}/man1/audtool.1*
%{_bindir}/audacious
%{_bindir}/audtool
%{_datadir}/applications/%{desktop_vendor}-audacious.desktop
%{_datadir}/audacious/
%{_datadir}/pixmaps/audacious.png
%{_datadir}/icons/hicolor/48x48/apps/audacious.png

%files libs
%defattr(-, root, root, 0755)
%{_libdir}/audacious/
%{_libdir}/libaudclient.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/audacious/
%{_libdir}/libaudclient.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 1.4.6-1
- Updated to release 1.4.6.

* Sat Jun 14 2008 Heiko Adams <info@fedora-blog.de> - 1.3.2-6
- force to require mcs-devel = 0.4.1 and mcs = 0.4.1

* Mon Mar 31 2008 Heiko Adams <info@fedora-blog.de> - 1.3.2-5
- bugfix

* Sun Mar 23 2008 Heiko Adams <info@fedora-blog.de> - 1.3.2-4
- some small improvements to the specfile

* Sat Mar 22 2008 Heiko Adams <info@fedora-blog.de> - 1.3.2-3
- bugfixes

* Thu Aug 30 2007 Heiko Adams <info@fedora-blog.de> - 1.3.2-2
- Rebuild for RPMforge.

* Mon Apr 16 2007 Ralf Ertzinger <ralf@skytale.net> 1.3.2-1.fc6
- Update to 1.3.2

* Sun Dec 24 2006 Ralf Ertzinger <ralf@skytale.net> 1.2.2-2.fc6
- Remove audacious-1.1.1-controlsocket-name.patch due to request
  from upstream, xmms and audacious are not entirely compatible

* Sun Nov 30 2006 Ralf Ertzinger <ralf@skytale.net> 1.2.2-1.fc6
- Update to 1.2.2
- Split off libaudacious into a separate package to handle the
  (now externally provided and built) plugins better

* Tue Nov 7 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.2-4.fc6
- Disable gnome-vfs, it causes too much trouble
- Add --enable-chardet

* Wed Oct 18 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.2-2.fc6
- Add Obsoletes/Provides for BMP

* Wed Sep 06 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.2-1.fc6
- Update to 1.1.2

* Thu Aug 17 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.1-6.fc6
- Another go at the %%20 problem

* Mon Aug 14 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.1-4.fc6
- Fix %%20 in playlist entries

* Sun Jul 30 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.1-3.fc6
- Bump for rebuild

* Sun Jul 30 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.1-2.fc6
- Change the name of the control socket to "xmms" instead of
  audacious. This makes programs that remote control xmms
  (and compatibles) work.

* Sun Jul 30 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.1-1.fc6
- Update to 1.1.1
- Drop amidi path patch
- Add shaded playlist skin patch (seems like audacious needs it,
  too)

* Fri Jul 21 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.0-1.fc6
- Update to 1.1.0 final
- Rediff some patches

* Sun Jul 9 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.0-0.2.dr2.fc6
- Fix quoting of filenames

* Thu Jun 29 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.0-0.1.dr2.fc6
- Fixed version for Extras review
  - Build OSS, arts and jack output plugins
  - Split esd, arts and jack into separate packages
  - Fix rpath issue
  - Fix absolute symlinks

* Sat Jun 24 2006 Ralf Ertzinger <ralf@skytale.net> 1.1.0-0.0.dr2.fc6
- Initial build for Fedora Extras
