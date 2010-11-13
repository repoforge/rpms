# $Id$
# Authority: dag

### EL6 ships with fontforge-20090622-2.1.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Outline and bitmap font editor
Name: fontforge
%define real_version 20080828
Version: 0.0.20080828
Release: 1%{?dist}
License: BSD
Group: Applications/Publishing
URL: http://fontforge.sourceforge.net/

Source: http://dl.sf.net/fontforge/fontforge_full-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel, libuninameslist-devel
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel, libungif-devel
BuildRequires: libxml2-devel
%{!?_without_modxorg:BuildRequires: libX11-devel, libSM-devel, libXi-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
BuildRequires: desktop-file-utils

Obsoletes: pfaedit <= %{version}-%{release}
Provides: pfaedit = %{version}-%{release}

%description
FontForge (former PfaEdit) is a font editor for outline and bitmap
fonts. It supports a range of font formats, including PostScript
(ASCII and binary Type 1, some Type 3 and Type 0), TrueType, OpenType
(Type2) and CID-keyed fonts.

%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e 's|-rpath \$\(libdir\)||' fontforge/Makefile*.in
%{__perl} -pi.orig -e 's|("mozilla", "opera",)|"htmlview", "firefox", $1|' fontforge/uiutil.c

%{__cat} <<EOF >fontforge.desktop
[Desktop Entry]
Name=FontForge Font Editor
Comment=Edit and convert fonts
Exec=fontforge
Icon=icon-accessories.png
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
MimeType=application/x-font;application/x-font-bdf;application/x-font-ttf;application/x-font-truetype;application/x-truetype-font;application/font-tdpfr;application/x-font-afm;application/x-font-type1;application/x-font-bdf
EOF

%build
export LIBS="-lgif"
%configure \
    --with-freetype-bytecode="no"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang FontForge

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 fontforge.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/fontforge.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install \
        --vendor %{desktop_vendor} \
        --add-category X-Red-Hat-Base \
        --dir %{buildroot}%{_datadir}/applications \
        fontforge.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/sbin/ldconfig 2>/dev/null
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files -f FontForge.lang
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README-unix
%doc %{_mandir}/man1/fontforge.1*
%doc %{_mandir}/man1/fontimage.1*
%doc %{_mandir}/man1/sfddiff.1*
%{_bindir}/fontforge
%{_bindir}/fontimage
%{_bindir}/sfddiff
%{_datadir}/fontforge/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-fontforge.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/fontforge.desktop}
%{_libdir}/libgdraw.so.*
%{_libdir}/libgunicode.so.*
%{_libdir}/pkgconfig/fontforge.pc
%exclude %{_libdir}/libgdraw.la
%exclude %{_libdir}/libgdraw.so
%exclude %{_libdir}/libgunicode.la
%exclude %{_libdir}/libgunicode.so

%changelog
* Sat Sep 20 2008 Dag Wieers <dag@wieers.com> - 0.0.20080828-1
- Updated to release 20080828.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.0.20061025-1
- Updated to release 20061025.

* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 0.0-0.20050502
- Initial package. (using DAR)
