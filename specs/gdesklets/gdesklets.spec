# $Id$
# Authority: dag

%define real_name gDesklets

Summary: Advanced architecture for desktop applets
Name: gdesklets
Version: 0.26.2
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pycage.de/download/gdesklets/gDesklets-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgtop2-devel >= 2.0.0, python-devel >= 2.0.0, gcc-c++
BuildRequires: gnome-python2 >= 1.99.17, gnome-python2-gconf >= 2.0
BuildRequires: perl(XML::Parser)
Requires: python >= 2.2, gnome-python2 >= 1.99.17, gnome-python2-gconf >= 2.0

%description
gDesklets provides an advanced architecture for desktop applets - tiny
displays sitting on your desktop in a symbiotic relationship of eye candy 
and usefulness.

Populate your desktop with status meters, icon bars, weather sensors,
news tickers... whatever you can imagine! Virtually anything is possible 
and maybe even available some day.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\@coredir\@|\$(datadir)/gdesklets|g;
		s|\@gnulocaledir\@|\$(datadir)/gdesklets/locale|g;
		s|\@localedir\@|\$(datadir)/gdesklets/locale|g;
		s|\@PIXMAPDIR\@|\$(datadir)/pixmaps|g;
	' Makefile.in */Makefile.in */*/Makefile.in

%build
%configure \
	--disable-dependency-tracking \
	--disable-install-schemas
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

### FIXME: Fix symlinks pointing to BuildRoot. (Please fix upstream somehow)
%{__ln_s} -f %{_datadir}/gdesklets/gdesklets %{buildroot}%{_bindir}
%{__ln_s} -f %{_datadir}/pixmaps/gdesklets.png %{buildroot}%{_datadir}/gdesklets/data/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gdesklets-display-thumbnail.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gconf/schemas/gdesklets-display-thumbnail.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/gdesklets/
%{_datadir}/icons/gnome/48x48/mimetypes/*.png
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*.png
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.26.2-1
- Updated to release 0.26.2.

* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.26.1-0
- Updated to release 0.26.1.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.25.1-0
- Updated to release 0.25.1.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 0.25-0
- Updated to release 0.25.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.24.1-0
- Initial package. (using DAR)
