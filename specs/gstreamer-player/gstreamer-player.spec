# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%define real_name gst-player

Summary: GStreamer Streaming media framework player
Name: gstreamer-player
Version: 0.6.0
Release: 0
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.net/apps/gst-player/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gstreamer/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.2, glib2-devel, libgnomeui-devel, libglade2-devel
BuildRequires: gstreamer-devel >= 0.6.0, gstreamer-plugins-devel >= 0.6.0
#BuildRequires: gstreamer-play, gstreamer-GConf
BuildRequires: gettext, eel2-devel, gail-devel, zlib-devel
%{?fc1:BuildRequires: nautilus-devel}
%{?el3:BuildRequires: nautilus-devel}
%{?rh9:BuildRequires: nautilus-devel}
%{?rh8:BuildRequires: nautilus-devel}
%{?rh7:BuildRequires: nautilus2-devel}

%description
This package contains the GStreamer media player and libgstplay, a simple
GStreamer playback wrapper library.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n nautilus-gstreamer
Summary: GStreamer nautilus view
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description -n nautilus-gstreamer
GStreamer nautilus view for media files.

%package -n mozilla-gstreamer
Summary: GStreamer plugin for Mozilla
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}

%description -n mozilla-gstreamer
This package contains a plugin for the Mozilla browser that makes it
possible to use the gstreamer-player in Mozilla.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-debug \
	--enable-static \
	--with-configdir="%{_sysconfdir}/gstreamer" \
	--disable-tests \
	--disable-examples \
	--disable-debug-color \
	--enable-docs-build \
	--disable-schemas-install

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{real_name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}{,/gst}/*.la \
		%{buildroot}%{_libdir}/mozilla/plugins/*.{a,la} \
		%{buildroot}%{_libdir}/mozilla/plugins/*.so{,.0}

### Clean up mozilla plugin
%{__mv} -f %{buildroot}%{_libdir}/mozilla/plugins/libmozstreamer.so* %{buildroot}%{_libdir}/mozilla/plugins/libmozstreamer.so

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{real_name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop
%{_datadir}/gst-player/
%{_datadir}/mime-info/*.keys
%{_datadir}/pixmaps/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/gst-player-%{version}/

%files -n mozilla-gstreamer
%defattr(-, root, root, 0755)
%{_libdir}/mozilla/plugins/*.so

%files -n nautilus-gstreamer
%defattr(-, root, root, 0755)
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*
%{_datadir}/gnome-2.0/ui/gst-player-view-ui.xml

%changelog
* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Initial package. (using DAR)
