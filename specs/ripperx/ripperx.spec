# $Id$
# Authority: dries

%define desktop_vendor rpmforge
%define real_name ripperX

Summary: GTK program to rip CD audio and encode to mp3, ogg, or flac
Name: ripperx
Version: 2.6.7
Release: 2%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://ripperx.sourceforge.net/

Source:	http://dl.sf.net/ripperx/ripperX-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: cdparanoia
BuildRequires: desktop-file-utils, glib-devel, gtk+-devel

%description
GTK program to rip CD audio and encode to mp3, ogg, and flac.
Supports parallel ripping/encoding, has plugins for cdparanoia,
BladeEnc, Lame, GoGo, FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3,
FLAC, and the ISO encoder.  Also has support for CDDB and ID3 tags.

%prep
%setup -n %{real_name}-%{version}

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=ripperX
Comment=rip CDs and encode to mp3, ogg, or flac
Exec=ripperX
Icon=/usr/share/pixmaps/ripperX-icon.xpm
Terminal=false
MultipleArgs=false
Type=Application
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_datadir}/applications
%makeinstall
%{__install} -D src/xpms/ripperX-icon.xpm %{buildroot}%{_datadir}/pixmaps/ripperX-icon.xpm

# Install menu entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%{_bindir}/ripperX
%{_bindir}/ripperX_plugin-cdparanoia
%{_bindir}/ripperX_plugin-encode
%{_bindir}/ripperX_plugin-8hz-mp3
%{_bindir}/ripperX_plugin-lame
%{_bindir}/ripperX_plugin-flac
%{_bindir}/ripperX_plugin-gogo
%{_bindir}/ripperX_plugin-oggenc
%{_bindir}/ripperX_plugin-toolame
%{_bindir}/ripperX_plugin-bladeenc
%{_bindir}/ripperX_plugin-xingmp3enc
%{_bindir}/ripperX_plugin-l3enc
%{_bindir}/ripperX_plugin-mp3enc
%{_datadir}/pixmaps/ripperX-icon.xpm
%{_datadir}/applications/*ripperx.desktop

%changelog
* Tue Oct 10 2006 Dag Wieers <dag@wieers.com> - 2.6.7-2
- Fixed group name.

* Sat Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.7-1
- Adapted for rpmforge, thanks to Mat Fletcher!

* Wed Jun 01 2005 tony mancill <tony@mancill.com>
- version 2.6.6
- fixes for cdparanoia output on Fedora Core 3

* Wed Jun 01 2005 tony mancill <tony@mancill.com>
- version 2.6.5

* Sun Jan 04 2004 tony mancill <tony@mancill.com>
- version 2.6.1

* Thu Sep 25 2003 tony mancill <tony@mancill.com>
- version 2.6

* Tue Apr 04 2001 Jos Dehaes <jos.dehaes@bigfoot.com>
-version 2.1

* Mon Jan 03 2000 Dax Kelson <dax@gurulabs.com>
- Version 1.9
- Updated SPEC to use a $RPM_BUILD_ROOT, changelog, docs, and the strip binaries
- Created GNOME ".desktop" file so ripperX shows up on the menu
- Patch so cdparanoia fills files that are group writable, enabling shared directory ripping
