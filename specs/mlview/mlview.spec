# $Id$
# Authority: dag
# Upstream: Dodji Seketeli <dodji@gnome.org>

Summary: Graphical XML Editor
Name: mlview
Version: 0.6.3
Release: 1
License: GPL
Group: Applications/Editors
URL: http://www.mlview.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

#Source: http://savannah.gnu.org/download/mlview/tarballs/mlview-%{version}.tar.bz2
Source: http://ftp.gnome.org/pub/GNOME/sources/mlview/0.6/mlview-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel >= 2.4.30, libgnomeui-devel >= 2.0.3, libglade-devel >= 0.17
BuildRequires: eel2-devel, gettext, desktop-file-utils

%description
MlView is an XML editor for GNOME.
It include support to view, edit, validate and save xml document by graphical
manipulation the xml Document Object Model.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<'EOF' >mlview.desktop.in
[Desktop Entry]
Name=MlView XML Editor
Comment=Edit XML documents
Icon=mlview.png
Exec=mlv %%F
TryExec=mlv
Terminal=false
Encoding=UTF-8
Type=Application
Categories=GNOME;Application;Office;TextEditor;
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

%{__install} -D -m0644 pixmaps/mlview-app-icon.png %{buildroot}%{_datadir}/pixmaps/mlview.png

desktop-file-install --vendor gnome --delete-original \
  --dir %{buildroot}%{_datadir}/applications          \
  --add-category X-Red-Hat-Extra                      \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BRANCHES ChangeLog COPYING COPYRIGHT NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/mlview/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Wed Dec 10 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Added missing BuildRequires. (Dries Verachtert)
- Updated to release 0.6.2.

* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Fri Sep 05 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
