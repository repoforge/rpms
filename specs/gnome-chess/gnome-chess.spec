# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: GNOME Chess game
Name: gnome-chess
Version: 0.3.3
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.gnome.org/

Source: http://ftp.acc.umu.se/pub/GNOME/sources/gnome-chess/0.3/gnome-chess-%{version}.tar.bz2
Source1: gnome-chess.png
Patch0: gnome-chess-mime.patch
Patch1: gnome-chess-0.3.3-quit.patch
### Fix scrollkeeper file to be DTD compliant
Patch2: gnome-chess-0.3.3-scrollkeeper.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, gdk-pixbuf-devel, gnome-print-devel, libglade-devel
BuildRequires: scrollkeeper, intltool

Requires(post): scrollkeeper

%description
GNOME Chess is part of the GNOME project and is a graphical chess interface. It
can provide and interface to GNU Chess, Crafty, chess servers and PGN files.

%prep
%setup
%patch0 -p1 -b .mimetypes
%patch1 -p1 -b .quit
%patch2 -p1 -b .scrollkeeper

%{__cat} <<EOF >gnome-chess.desktop
[Desktop Entry]
Name=Chess
Comment=Play chess against any opponent
Exec=gnome-chess
Icon=gnome-chess.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;Game;
EOF

%build
xml-i18n-toolize
%{__aclocal} -I macros
%{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/gnome-chess.png

%if %{!?_without_freedesktop:1}0
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
        %{buildroot}%{_datadir}/gnome/apps/Games/gnome-chess.desktop
%endif

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/gnome-chess-manual/
%{_bindir}/*
%{_datadir}/pixmaps/gnome-chess.png
%{_datadir}/pixmaps/gnome-chess./
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/gnome-chess.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/gnome-chess.desktop}
%{_datadir}/gnome-chess/
%{_datadir}/mime-info/*
%{_datadir}/omf/gnome-chess/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1.2
- Rebuild for Fedora Core 5.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Added improved desktop file.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Initial package. (using DAR)
