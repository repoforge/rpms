# Authority: dag
# Upstream: Paolo Bacchilega <paolo.bacch@tin.it>

Summary: Organize your preferred applications on the GNOME Panel.
Name: quick-lounge-applet
Version: 2.0.3
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://quick-lounge.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/quick-lounge-applet/2.0/quick-lounge-applet-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib2-devel >= 2.1.0, gtk2-devel >= 2.1.1, libgnome-devel >= 2.1.1
BuildRequires: gnome-desktop-devel >= 2.1.1, gnome-vfs2-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: libgnomeui-devel >= 2.1.1, gnome-panel >= 2.0.0

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

%{__mv} -f %{buildroot}%{_libdir}/*.so.0.0.0 %{buildroot}%{_libdir}/*.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.{a,la,so.*}

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
%config %{_sysconfdir}/gconf/schemas/*
%{_libdir}/*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/quick-lounge/
%{_datadir}/pixmaps/*
#exclude %{_libdir}/*.a
#exclude %{_libdir}/*.la
#exclude %{_libdir}/*.so.*

%changelog
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
