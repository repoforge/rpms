# $Id: inkscape.spec 4930 2006-11-24 14:05:21Z dries $
# Authority: dag
# Upstream: <inkscape-devel$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh8:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Vector drawing application
Name: inkscape
Version: 0.43
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://inkscape.sourceforge.net/

Source: http://dl.sf.net/inkscape/inkscape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: libsigc++2-devel, gtkmm24-devel, glibmm-devel
BuildRequires: gtkmm2, lcms-devel
# >= 2.4
BuildRequires: libgc-devel,  perl(XML::Parser)
BuildRequires: gcc-c++, pkgconfig
BuildRequires: gettext, libpng-devel, freetype-devel, zlib-devel
BuildRequires: gtk2-devel, libxml2-devel, libxslt-devel
BuildRequires: python-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
#%{?_without_modxorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{?_without_modxorg:BuildRequires: XFree86-devel, xorg-x11-Mesa-libGLU}
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel}

%description
Inkscape is a SVG based generic vector-drawing program.

%prep
%setup

%{__cat} <<EOF >inkscape.desktop.in
[Desktop Entry]
Name=Inkscape Vector Drawing Program
Comment=Vector drawing program.
Type=Application
MimeType=image/svg+xml
FilePattern=inkscape
Icon=inkscape.png
Exec=inkscape %U
TryExec=inkscape
Terminal=false
StartupNotify=true
Encoding=UTF-8
Categories=Application;Graphics;
EOF

%build
%configure \
	--with-xinerama \
	--enable-static="no" \
	--with-inkjar
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
        desktop-file-install --delete-original             \
		--vendor %{desktop_vendor}                 \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                %{buildroot}%{_datadir}/applications/inkscape.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* HACKING*txt NEWS README TRANSLATORS
%doc %{_mandir}/man1/ink*.1*
%doc %{_mandir}/*/man1/ink*.1*
%{_bindir}/ink*
#%{_libdir}/inkscape
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-inkscape.desktop}
%{?_without_freedesktop:%{_datadir}/applications/inkscape.desktop}
%{_datadir}/inkscape/
%{_datadir}/pixmaps/inkscape.png

%changelog
* Mon Jul 30 2007 Dag Wieers <dag@wieers.com> - 0.43-2
- Rebuild against libgc-7.0.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-2
- Fixes by Brent Terp.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Thu Feb 10 2005 Dag Wieers <dag@wieers.com> - 0.41-1
- Updated to release 0.41.

* Tue Nov 30 2004 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.39-1
- Updated to release 0.39.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.38.1-1
- Updated to release 0.38.1.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.37-0
- Updated to release 0.37.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.36-0
- Updated to release 0.36.

* Thu May 01 2003 Christian Schaller <uraeus@gnome.org>
- Fix up the spec file for current release.

* Mon Sep 23 2002 Dag Wieers <dag@wieers.com> - 0.2.6-1
- Updated to release 0.2.6.

* Thu Sep 12 2002 Dag Wieers <dag@wieers.com> - 0.2.5-1
- Updated to release 0.2.5.
- Changed SPEC to benefit from macros.
