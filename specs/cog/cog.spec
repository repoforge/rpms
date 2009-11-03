# $Id$
# Authority: dag
# Upstream: <maxx$daimi,au,dk>

Summary: Advanced GNOME configuration editor
Name: cog
Version: 0.7.1
Release: 2.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.krakoa.dk/linux-software.html#COG

Source: http://www.krakoa.dk/progs/cog/cog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.3, glib2-devel >= 2.0.1, GConf2-devel >= 1.1.11
BuildRequires: libxml2-devel >= 2.4.21, libgnomeui-devel
BuildRequires: libglade2-devel
BuildRequires: desktop-file-utils

%description
COG is a GNOME configurator program. A program for editing advanced
GNOME settings in an easy way.

%prep
%setup

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >cog.desktop
[Desktop Entry]
Name=GNOME Configurator
Comment=Edit advanced GNOME settings
Icon=cog.png
Exec=cog
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;System;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 pixmaps/cog-icon-2-48x48.png %{buildroot}%{_datadir}/pixmaps/cog.png

### Desktop entry
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--dir %{buildroot}%{_datadir}/applications    \
	--add-category X-Red-Hat-Base                 \
	%{buildroot}%{_datadir}/applications/cog.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/cog/
%{_datadir}/pixmaps/cog.png
%{_datadir}/applications/gnome-cog.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-2.2
- Rebuild for Fedora Core 5.

* Wed Jun 09 2004 Dag Wieers <dag@wieers.com> - 0.7.1-2
- Added improved desktop file.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Thu Jul 24 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.5.3-0
- Initial package. (using DAR)
