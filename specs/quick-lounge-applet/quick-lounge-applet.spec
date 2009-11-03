# $Id$
# Authority: dag
# Upstream: Paolo Bacchilega <paolo,bacch$tin,it>

Summary: Organize your preferred applications on the GNOME Panel
Name: quick-lounge-applet
Version: 2.2.0
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://quick-lounge.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/quick-lounge-applet/2.2/quick-lounge-applet-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.1.0, gtk2-devel >= 2.1.1, libgnome-devel >= 2.1.1
BuildRequires: gnome-desktop-devel >= 2.1.1, gnome-vfs2-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: libgnomeui-devel >= 2.1.1, gnome-panel >= 2.0.0, gnome-panel-devel
BuildRequires: gcc-c++, intltool, perl-XML-Parser

%description
The Quick Lounge applet is an applet for the GNOME Panel. With this
applet you can organize your preferred applications in a single place.
You can add spaces between applications, they can be used to group
together applications with similar tasks.

%prep
%setup

### FIXME: Fix the localedir to use $(datadir). (Please fix upstream)
%{__perl} -pi.orig -e 's|^(localedir =) \$\(libdir\)/locale|$1 \$(datadir)/locale|' po/Makefile.in.in

%build
%configure \
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
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_datadir}/gnome/help/quick-lounge/
%config %{_sysconfdir}/gconf/schemas/quick-lounge.schemas
%{_datadir}/gnome-2.0/ui/GNOME_QuickLoungeApplet.xml
%{_datadir}/omf/quick-lounge-applet/
%{_datadir}/pixmaps/quick-lounge-applet.png
%{_datadir}/quick-lounge/
%{_libdir}/bonobo/servers/GNOME_QuickLoungeApplet_Factory.server
%{_libexecdir}/quick-lounge-applet
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Updated to release 2.0.3.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Updated to release 2.0.3.

* Tue Nov 18 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.

* Sat Sep 20 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sun Jul 06 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0
- Updated to release 2.0.0.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Updated to release 1.1.4.

* Tue Apr 01 2003 Dag Wieers <dag@wieers.com> - 1.1.3-0
- Updated to release 1.1.3.

* Tue Jan 28 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Initial package. (using DAR)
