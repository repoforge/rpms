# $Id$

# Authority: dag

Summary: Music player.
Name: jamboree
Version: 0.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.gnome.org/~jdahlin/jamboree/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/jamboree/%{version}/jamboree-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.2.0, libgnomeui-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: gstreamer-devel >= 0.6.2, libogg-devel >= 1.0, libvorbis-devel >= 1.0
BuildRequires: libid3tag-devel >= 0.12, gdbm-devel >= 1.8.0

%description
Jamboree is a music player.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %name

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ README NEWS
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/jamboree
%{_datadir}/jamboree/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Tue Sep 30 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
