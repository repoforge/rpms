# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: GNOME binary editor
Name: ghex
Version: 2.8.2
Release: 1
License: GPL
Group: Applications/Editors
URL: http://pluton.ijs.si/~jaka/gnome.html#GHEX

Source: http://ftp.gnome.org/pub/GNOME/sources/ghex/2.8/ghex-%{version}.tar.bz2
Patch0: ghex-no-scrollkeeper.patch
Patch1: ghex-search-crash.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper, gcc-c++, libgnomeui-devel
BuildRequires: libgnomeprintui22-devel, gail-devel
BuildRequires: intltool, gettext, perl-XML-Parser, desktop-file-utils

%description
GHex allows the user to load data from any file, view and edit it in either
hex or ascii. A must for anyone playing games that use non-ascii format for
saving.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtk2-devel, gail-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .noscrollkeeper
%patch1 -b .searchcrash

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

desktop-file-install --delete-original \
	--vendor %{desktop_vendor} \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/ghex.desktop

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :
scrollkeeper-update -q || :

%postun
/sbin/ldconfig
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_sysconfdir}/gconf/schemas/ghex2.schemas
%{_bindir}/ghex2
%{_datadir}/applications/rpmforge-ghex.desktop
%{_datadir}/gnome/help/ghex2/
%{_datadir}/gnome-2.0/ui/ghex-ui.xml
%{_datadir}/omf/ghex/
%{_datadir}/pixmaps/gnome-ghex.png
%{_libdir}/libgtkhex.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gtkhex/
%exclude %{_libdir}/libgtkhex.a
%exclude %{_libdir}/libgtkhex.la
%{_libdir}/libgtkhex.so
%{_libdir}/pkgconfig/gtkhex.pc

%changelog
* Sun May 06 2007 Dag Wieers <dag@wieers.com> - 2.8.2-1
- Updated to release 2.8.2.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Updated to release 2.8.1.

* Mon Apr 14 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Initial package. (using DAR)
