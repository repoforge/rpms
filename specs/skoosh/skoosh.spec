# $Id$
# Authority: dag
# Upstream: Timothy Musson <trmusson$ihug,co,nz>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Simple, friendly, sliding tile puzzle
Name: skoosh
Version: 2.5.0
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://homepages.ihug.co.nz/~trmusson/programs.html#skoosh

Source: http://homepages.ihug.co.nz/~trmusson/stuff/skoosh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libgnomeui-devel >= 2.0
BuildRequires: scrollkeeper
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

Requires(post): scrollkeeper

%description
A simple, friendly, sliding tile puzzle.

%prep
%setup

%{__cat} <<EOF >skoosh.desktop
[Desktop Entry]
Name=Skoosh Tile Puzzle
Comment=Slide tiles to complete a picture
Icon=skoosh.png
Exec=skoosh
Terminal=false
Type=Application
Categories=GNOME;Application;Game;PuzzleGame;
StartupNotify=true
X-GNOME-DocPath=skoosh/skoosh.xml
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/skoosh.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/skoosh/
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gconf/schemas/*.schemas
%config %{_sysconfdir}/sound/events/skoosh.soundlist
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/skoosh/
%{_datadir}/omf/skoosh/
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1.2
- Rebuild for Fedora Core 5.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 2.5.0-1
- Updated to release 2.5.0.

* Fri Jan 23 2004 Dag Wieers <dag@wieers.com> - 2.0.8-1
- Remove duplicate desktop file.

* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 2.0.8-0
- Updated to release 2.0.8.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 2.0.7-0
- Initial package. (using DAR)
