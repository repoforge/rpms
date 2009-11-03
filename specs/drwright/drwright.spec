# $Id$
# Authority: dag
# Upstream: Richard Hult <richard$imendio.com>

Summary: Tool to remind you to take wrist breaks
Name: drwright
Version: 0.18
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.imendio.com/projects/drwright/

Source: http://ftp.gnome.org/pub/GNOME/sources/drwright/%{version}/drwright-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pango-devel >= 1.0.99, gtk2-devel >= 2.0.4, GConf2-devel >= 1.2.0
BuildRequires: libglade2-devel >= 2.0.0, fontconfig, gcc-c++, dbus-devel
BuildRequires: intltool, perl-XML-Parser, libgnomeui-devel, gettext
BuildRequires: desktop-file-utils

%description
DrWright is a program that forces you to take wrist breaks to rest your hands.

%prep
%setup

%{__cat} <<EOF >drwright.desktop.in
[Desktop Entry]
Name=DrWright Break Reminder
Comment=Reminds you to take wrist breaks
Exec=drwright
Icon=redhat-accessories.png
Terminal=false
Type=Application
Categories=Application;Utility;
Encoding=UTF-8
EOF

# todo: possibly only needed on fc4, check
%{__perl} -pi -e 's|dbus_bus_acquire_service|dbus_bus_request_name|g;' src/*.c

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
  --dir %{buildroot}%{_datadir}/applications          \
  --add-category X-Red-Hat-Extra                      \
  %{buildroot}%{_datadir}/applications/*

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/drwright.schemas
%{_bindir}/drwright
%{_datadir}/applications/gnome-drwright.desktop
%{_datadir}/drwright/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1.2
- Rebuild for Fedora Core 5.

* Sat Oct 02 2004 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Updated to release 0.16.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.15-0
- Initial package. (using DAR)
