# $Id$
# Authority:    hadams

Name:           audacious
Version:        1.3.2
Release:        2
Summary:        A GTK2 based media player similar to xmms

Group:          Applications/Multimedia
License:        GPL
URL:            http://audacious-media-player.org/

Source0:        http://static.audacious-media-player.org/release/audacious-%{version}.tgz
Patch0:         audacious-1.3.1-xmms-skins.patch
Patch1:         audacious-1.3.1-default-skin.patch
# Patch2:         audacious-1.1.0-no-rpath.patch
Patch3:         audacious-1.2.1-relative-links.patch
# Patch4:         audacious-1.1.0-quoting.patch
# Patch5:         audacious-1.1.0-amidi-backend.patch
Patch6:         audacious-1.2.1-shaded-skin.patch
# Patch7:         audacious-1.1.1-controlsocket-name.patch
# Patch8:         audacious-1.1.1-playlist-twenty.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel >= 2.6
BuildRequires:  zlib-devel, desktop-file-utils >= 0.9
BuildRequires:  libglade2-devel >= 2.4
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  mcs-devel >= 0.1

Requires:       audacious-plugins >= 1.3.0

Requires(post):   desktop-file-utils >= 0.9
Requires(postun): desktop-file-utils >= 0.9

Obsoletes:      bmp <= 0.9.7.1
Provides:       bmp = 0.9.7.1

%description
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.


%package        libs
Summary:        Library files for Audacious
Group:          System Environment/Libraries

%description    libs
Library files for Audacious


%package        devel
Summary:        Development files for Audacious
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       glib2-devel, gtk2-devel >= 2.6, GConf2-devel, libglade2-devel >= 2.4
Requires:       mcs-devel >= 0.1
Requires:       pkgconfig

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Obsoletes:      bmp-devel <= 0.9.7.1
Provides:       bmp-devel = 0.9.7.1

%description    devel
Development files for Audacious


%prep
%setup -q

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

%build
%configure \
    --disable-rpath \
    --enable-gconf \
    --disable-gnome-vfs \
    --enable-chardet \
    --disable-dependency-tracking
make V=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

desktop-file-install --vendor fedora \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
    --delete-original \
    --remove-mime-type audio/x-scpls \
    --remove-mime-type audio/x-mpegurl \
    --remove-mime-type audio/mpegurl \
    --remove-mime-type audio/mp3 \
    --remove-mime-type audio/x-mp3 \
    --remove-mime-type audio/mpeg \
    --remove-mime-type audio/x-mpeg \
    --remove-mime-type audio/x-wav \
    --remove-mime-type application/x-ogg \
    --remove-category Application \
    $RPM_BUILD_ROOT%{_datadir}/applications/audacious.desktop

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/audacious.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%post
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/audacious
%{_bindir}/audtool
%{_datadir}/audacious
%{_mandir}/man[^3]/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/audacious
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/audacious
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Thu Aug 30 2007 Heiko Adams <info@fedora-blog.de> 1.3.2-2
- rebuild for rpmforge

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
