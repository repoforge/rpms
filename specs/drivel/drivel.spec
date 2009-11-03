# $Id$
# Authority: dag
# Upstream: Todd Kulesza <todd$dropline,net>

Summary: LiveJournal client for GNOME
Name: drivel
Version: 1.2.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.dropline.net/drivel/

Source: http://dl.sf.net/drivel/drivel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, perl(XML::Parser), intltool, pkgconfig
BuildRequires: gtk2-devel, GConf2-devel, gnome-vfs2-devel, glib2 >= 2.4
BuildRequires: libgnome-devel, libgnomeui-devel
Requires: gtk2 >= 2.0.0, curl >= 7.10.0

%description
Drivel is an advanced LiveJournal client for the GNOME desktop.  While
maintaining a full set of features, it had been designed with usability
in mind, and presents an elegant user interface.

%prep
%setup

%build
%configure \
	--disable-desktop-update \
	--disable-mime-update \
        --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
s &>/dev/null
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_datadir}/gnome/help/drivel/
%config %{_sysconfdir}/gconf/schemas/drivel.schemas
%{_bindir}/drivel
%{_datadir}/application-registry/drivel.applications
%{_datadir}/applications/drivel.desktop
%{_datadir}/drivel/
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-x-drivel.png
%{_datadir}/mime-info/drivel.*
%{_datadir}/mime/packages/drivel.xml
%{_datadir}/omf/drivel/
%{_datadir}/pixmaps/drivel/
%{_datadir}/pixmaps/livejournal.png
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.4-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Mon May 24 2004 Dag Wieers <dag@wieers.com> - 0.90.0-1
- Updated to release 0.90.0.

* Thu Mar 25 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
