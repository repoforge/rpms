# $Id$
# Authority: dag
# Upstream: Richard Hult <richard$imendio,com>

Summary: Music player
Name: jamboree
Version: 0.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.imendio.com/projects/jamboree/

Source: http://ftp.gnome.org/pub/gnome/sources/jamboree/%{version}/jamboree-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.2.0, libgnomeui-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: gstreamer-devel >= 0.7, libogg-devel >= 1.0, libvorbis-devel >= 1.0
BuildRequires: libid3tag-devel >= 0.12, gdbm-devel >= 1.8.0, gcc-c++
BuildRequires: intltool, perl-XML-Parser, gettext
%{?fc4:BuildRequires: gstreamer-plugins-devel, gstreamer-devel}

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
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/jamboree.schemas
%{_bindir}/jamboree
%{_datadir}/jamboree/
%{_datadir}/applications/jamboree.desktop
%{_datadir}/pixmaps/jamboree.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1.2
- Rebuild for Fedora Core 5.

* Tue Sep 28 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Tue Sep 30 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
