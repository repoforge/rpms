# $Id$

# Authority: dag

%define mversion 38:1.6

Summary: GNOME browser based on Gecko (Mozilla rendering engine).
Name: galeon
Version: 1.3.14
Release: 0.a
License: GPL
Group: Applications/Internet
URL: http://galeon.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/galeon/galeon-%{version}a.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mozilla-devel = %{mversion}, gtk2-devel >= 2.0, libxml2-devel >= 2.4
BuildRequires: libgnomeui-devel >= 2.0.5, libbonoboui-devel >= 2.1.1, libglade2-devel >= 2.0.0
BuildRequires: gnome-vfs2-devel >= 2.0, GConf2-devel >= 2.0, bonobo-activation-devel >= 2.0.0
BuildRequires: scrollkeeper

Requires: mozilla = %{mversion}
Requires(post): scrollkeeper

%description
Galeon is a browser written in GTK+ which uses Gecko, the Mozilla rendering
engine, for rendering Web pages. It is developed to be fast and lightweight.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--disable-werror \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}-2.0

%post
%{_bindir}/galeon-config-tool --fix-gconf-permissions
%{_bindir}/galeon-config-tool --pkg-install-schemas
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ* NEWS README* THANKS TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/galeon/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%config %{_sysconfdir}/sound/events/*.soundlist
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_libdir}/galeon/
%{_datadir}/applications/*.desktop
%{_datadir}/galeon/
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/omf/galeon/
%{_datadir}/pixmaps/*
%{_datadir}/sounds/galeon/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.3.14-0.a
- Updated to release 1.3.14a.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.3.13-0.a
- Updated to release 1.3.13a.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.3.12-0
- Updated to release 1.3.12.

* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 1.3.11-0.a
- Updated to release 1.3.11a.
- Updated to release 1.3.11.

* Sat Nov 29 2003 Dag Wieers <dag@wieers.com> - 1.3.10-1
- Rebuild against 1.5.

* Mon Oct 27 2003 Dag Wieers <dag@wieers.com> - 1.3.10-0
- Updated to release 1.3.10.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 1.3.9-1
- Rebuild against mozilla-1.4.1.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 1.3.9-0
- Updated to release 1.3.9.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 1.3.8-0
- Updated to release 1.3.8.

* Wed Jul 23 2003 Dag Wieers <dag@wieers.com> - 1.3.7-0
- Updated to release 1.3.7.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 1.3.6-0
- Updated to release 1.3.6.

* Wed Jul 02 2003 Dag Wieers <dag@wieers.com> - 1.3.5-1
- Rebuild against mozilla-1.4.

* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Updated to release 1.3.5.

* Mon May 12 2003 Dag Wieers <dag@wieers.com> - 1.3.4-0
- Initial package. (using DAR)
