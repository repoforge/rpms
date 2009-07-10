# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Set of tools to create, alter and inspect Matroska files
Name: mkvtoolnix
Version: 2.9.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.bunkus.org/videotools/mkvtoolnix/

Source0: http://www.bunkus.org/videotools/mkvtoolnix/sources/mkvtoolnix-%{version}.tar.bz2
Source1: mkvmerge-gui.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ImageMagick
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: flac-devel
BuildRequires: libebml-devel
BuildRequires: libmatroska-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
Buildrequires: lzo-devel
BuildRequires: pcre-devel
BuildRequires: wxGTK-devel, gcc-c++
BuildRequires: zlib-devel

%description
MKVToolnix is a set of tools to create, alter and inspect Matroska files.

%package gui
Summary: Graphical User Interface to the mkvtoolnix set of tools
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description gui
MKVToolnix is a set of tools to create, alter and inspect Matroska files.
This package contains a Graphical User Interface for those tools.

%prep
%setup
### Remove hardcoded -O3
%{__perl} -pi -e 's|"-O3"|""|g' configure*

### Rename the gui like SuSE does
%{__patch} -p1 < contrib/suse-mmg-rename.diff

%{__cat} <<EOF >mkvmerge-gui.desktop
[Desktop Entry]
Name=MKV Merge
Comment=Merge multimedia streams into Matroska files
Exec=mkvmerge-gui
Icon=mkvmerge-gui
Terminal=false
Type=Application
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
%configure
### V="1" is for verbose build mode
%{__make} %{?_smp_mflags} V="1"

%install
%{__rm} -rf %{buildroot} mkvmerge-gui.png

### Execute /bin/true instead of stripping the binaries to get debuginfo data
%{__make} install DESTDIR="%{buildroot}" STRIP="/bin/true"
%find_lang %{name}

### Install the desktop file
desktop-file-install \
    --vendor="%{desktop_vendor}" \
    --dir="%{buildroot}%{_datadir}/applications" \
    --mode="0644" \
    mkvmerge-gui.desktop

# Install the desktop file's icon
convert src/mmg/matroskalogo.xpm mkvmerge-gui.png
%{__install} -Dp -m0644 mkvmerge-gui.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/mkvmerge-gui.png

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/mkvextract.1*
%doc %{_mandir}/man1/mkvinfo.1*
%doc %{_mandir}/man1/mkvmerge.1*
%{_bindir}/mkvextract
%{_bindir}/mkvinfo
%{_bindir}/mkvmerge

%files gui
%defattr(-, root, root, 0755)
%doc doc/mkvmerge-gui.html
%doc %{_mandir}/man1/mkvmerge-gui.1*
%{_bindir}/mkvmerge-gui
%{_datadir}/applications/%{desktop_vendor}-mkvmerge-gui.desktop
%{_datadir}/icons/hicolor/32x32/apps/mkvmerge-gui.png
%{_datadir}/mkvtoolnix/

%changelog
* Sun May 24 2009 Dag Wieers <dag@wieers.com> - 2.9.0-1
- Updated to release 2.9.0.

* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Updated to release 2.7.0.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 2.4.2-1
- Updated to release 2.4.2.

* Fri Dec 05 2008 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Updated to release 2.4.1.

* Sun Oct 12 2008 Dag Wieers <dag@wieers.com> - 2.4.0-1
- Updated to release 2.4.0.

* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 2.1.0-2
- Updated to release 2.1.0.

* Sat Jan 20 2007 Dag Wieers <dag@wieers.com> - 1.7.0-2
- Rebuild against wxGTK 2.6.3.

* Mon Oct 23 2006 Matthias Saou <http://freshrpms.net/> 1.7.0-1
- Spec file cleanup.
- Split off GUI sub-package like the Extras package is likely to do (#177134).

* Mon Aug 22 2005 Madcat <madcat@mymadcat.com>
- Build rpm for Fedora Core 4

* Sat Jan 2 2004 Ronald Bultje <rbultje@ronald.bitfreak.net
- set this thing up

