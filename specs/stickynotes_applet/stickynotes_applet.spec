# $Id$
# Authority: dag

# ExcludeDist: fc3

Summary: Simple sticky notes applet for the GNOME desktop
Name: stickynotes_applet
Version: 1.2.3
Release: 0.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://loban.caltech.edu/stickynotes/

Source: http://loban.caltech.edu/stickynotes/packages/stickynotes_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper, pkgconfig, libgnome-devel, libgnomecanvas-devel, atk-devel
BuildRequires: libbonoboui-devel, pango-devel, gnome-panel, libgnomeui-devel
BuildRequires: scrollkeeper, gnome-panel-devel, gettext

Requires(post): scrollkeeper

Obsoletes: goats

%description
An GNOME 2 applet that allows you to create, view and manage
sticky notes on your desktop.

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
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_datadir}/gnome/help/stickynotes_applet/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/omf/stickynotes_applet/
%{_datadir}/pixmaps/stickynotes/
%{_datadir}/stickynotes/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.3-0.2
- Rebuild for Fedora Core 5.

* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Updated to release 1.2.3.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.0.11-0
- Updated to release 1.0.11.

* Tue Jan 14 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
