# $Id$
# Authority: dries

# Screenshot: http://pwp.netcabo.pt/users/51/0251296501/tagtool/tt_edit.png
# ScreenshotURL: http://pwp.netcabo.pt/users/51/0251296501/tagtool/Default.htm#shots

%define desktop_vendor rpmforge

Summary: Manage the information fields in MP3 and Ogg Vorbis files
Name: tagtool
Version: 0.12.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://pwp.netcabo.pt/paol/tagtool/

Source: http://dl.sf.net/tagtool/tagtool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: automake, autoconf, glib2-devel >= 2.4, gtk2-devel >= 2.4, libglade2-devel >= 2.4
BuildRequires: automake, autoconf, glib2-devel, gtk2-devel, libglade2-devel
BuildRequires: id3lib-devel, libogg-devel, libvorbis-devel, perl-XML-Parser
BuildRequires: gettext, desktop-file-utils

%description
Audio Tag Tool is a program to manage the information fields in MP3 and Ogg
Vorbis files.

%prep
%setup

%{__cat} <<EOF >data/tagtool.desktop.in
[Desktop Entry]
_Name=Audio Tag Tool
_Comment=MP3 and Ogg Vorbis tag editor
Exec=tagtool
Icon=TagTool
Terminal=false
Type=Application
Categories=Audio;AudioVideo;AudioVideoEditing;
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--add-category Application                 \
	--add-category AudioVideo                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/tagtool.desktop

%pre
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/tagtool
%{_datadir}/applications/%{desktop_vendor}-tagtool.desktop
%{_datadir}/pixmaps/TagTool.png
%{_datadir}/tagtool/

%changelog
* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 0.12.2-1
- Updated to release 0.12.2.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.11.1-1
- Initial package.
