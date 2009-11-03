# $Id: inkscape.spec 1606 2004-07-20 08:18:01Z dag $
# Authority: dag
# Upstream: <inkscape-devel$lists,sf,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Vector drawing application
Name: inkscape
Version: 0.39
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://inkscape.sourceforge.net/

Source: http://dl.sf.net/inkscape/inkscape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(XML::Parser)
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

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
Categories=GNOME;Application;Graphics;
EOF

%build
%configure 
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
%doc AUTHORS ChangeLog COPYING* HACKING NEWS README
%doc %{_mandir}/man1/ink*.1*
%{_bindir}/ink*
#%{_libdir}/inkscape/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-inkscape.desktop}
%{?_without_freedesktop:%{_datadir}/applications/inkscape.desktop}
%{_datadir}/inkscape/
%{_datadir}/pixmaps/inkscape.png

%changelog
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
