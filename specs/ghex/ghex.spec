# $Id$
# Authority: dag

Summary: GNOME binary editor
Name: ghex
Version: 2.8.1
Release: 1
License: GPL
Group: Applications/Editors
URL: http://pluton.ijs.si/~jaka/gnome.html#GHEX

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/ghex/2.8/ghex-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnome-devel, ORBit
BuildRequires: gtk2-devel >= 1.2.0
BuildRequires: gnome-print-devel >= 0.24
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

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
%find_lang %{name}-2.0
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_sysconfdir}/gconf/schemas/ghex2.schemas
%{_bindir}/ghex2
%{_datadir}/applications/ghex.desktop
%{_datadir}/gnome/help/ghex2/
%{_datadir}/pixmaps/gnome-ghex.png
%{_datadir}/gnome-2.0/ui/ghex-ui.xml
%{_datadir}/omf/ghex/
%{_includedir}/gtkhex/
%{_libdir}/libgtkhex.a
%exclude %{_libdir}/libgtkhex.la
%{_libdir}/libgtkhex.so*
%{_libdir}/pkgconfig/gtkhex.pc


%changelog
* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Updated to release 2.8.1.

* Mon Apr 14 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Initial package. (using DAR)
