# $Id$
# Authority: dag
# Upstream: Jorn Baayen <muine-list@gnome.org>

Summary: Simple music player
Name: muine
Version: 0.5.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://muine.gooeylinux.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://muine.gooeylinux.org/muine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, mono-devel, gtk-sharp-devel >= 0.17, gstreamer-devel
BuildRequires: gstreamer-plugins-devel, libvorbis-devel, libid3tag-devel, flac-devel
#BuildRequires: libxine
Requires: mono, gtk-sharp >= 0.17

%description
Muine is an innovative music player. It is much easier and comfortable to
use than the iTunes model, which is used by both Rhythmbox and Jamboree.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/muine/*.a
%{_libdir}/muine/*.la
%{_libdir}/muine/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop

%changelog
* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Updated to release 0.3.2.

* Sun Feb 01 2004 Dag Wieers <dag@wieers.com> - 0.3.1.1-0
- Added a new covers patch.
- Updated to release 0.3.1.1.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Updated to release 0.3.1.
- Updated to release 0.3.0.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
