# $Id$
# Authority: dag
# Upstream: <galeon-devel$lists,sourceforge,net>

%define mversion %(rpm -q mozilla-devel --qf '%{RPMTAG_EPOCH}:%{RPMTAG_VERSION}' | tail -1)
%define lversion %(rpm -q mozilla-devel --qf '%{RPMTAG_VERSION}' | tail -1)

Summary: GNOME browser based on Gecko (Mozilla rendering engine)
Name: galeon
Version: 1.3.19
Release: 1
License: GPL
Group: Applications/Internet
URL: http://galeon.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/galeon/galeon-%{version}.tar.bz2
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

%{__cat} <<'EOF' >galeon.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

if [ -z "$MOZILLA_FIVE_HOME" ]; then
	MOZILLA_FIVE_HOME="%{_libdir}/mozilla-%{lversion}"
fi

LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$LD_LIBRARY_PATH"

export LD_LIBRARY_PATH MOZILLA_FIVE_HOME

exec %{_libdir}/galeon/galeon $@
EOF

%build
%configure \
	--disable-werror \
	--disable-schemas-install \
	--with-mozilla-snapshot="1.7.2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}-2.0

#%{__mv} -f %{buildroot}%{_bindir}/galeon %{buildroot}%{_libdir}/galeon/galeon
#%{__install} -D -m0755 galeon.sh %{buildroot}%{_bindir}/galeon

%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/

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
%doc %{_mandir}/man1/galeon.1*
%doc %{_datadir}/gnome/help/galeon/
%config %{_sysconfdir}/gconf/schemas/galeon.schemas
%config %{_sysconfdir}/sound/events/galeon.soundlist
%{_bindir}/galeon*
%{_libdir}/bonobo/servers/*.server
#%{_libdir}/galeon/
%{_datadir}/applications/galeon.desktop
%{_datadir}/galeon/
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/omf/galeon/
%{_datadir}/pixmaps/galeon.png
%{_datadir}/sounds/galeon/
%dir %{_libdir}/mozilla/
%dir %{_libdir}/mozilla/plugins/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sun Jan 16 2005 Dag Wieers <dag@wieers.com> - 1.3.19-1
- Updated to release 1.3.19.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 1.3.18-1
- Updated to release 1.3.18.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 1.3.17-4
- Build against new mozilla.

* Thu Aug 12 2004 Dag Wieers <dag@wieers.com> - 1.3.17-3
- Another correction *sigh*. (Jorge Bartos)

* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 1.3.17-2
- Re-added the galeon startup script. (Darren Brierton)

* Mon Aug 09 2004 Dag Wieers <dag@wieers.com> - 1.3.17-1
- Updated to release 1.3.17.

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 1.3.16-1
- Updated to release 1.3.16.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 1.3.15-1
- Updated to release 1.3.15.

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
