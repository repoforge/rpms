# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Vector drawing application.
Name: inkscape
Version: 0.37
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://inkscape.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/inkscape/inkscape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Inkscape is a SVG based generic vector-drawing program.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop.in
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

%if %{dfi}
%else
        desktop-file-install --vendor gnome --delete-original \
                --add-category X-Red-Hat-Base                 \
                --dir %{buildroot}%{_datadir}/applications    \
                %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* HACKING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/inkscape/
%{_datadir}/applications/*.desktop
%{_datadir}/inkscape/
%{_datadir}/pixmaps/*.png

%changelog
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
