# $Id$
# Authority: dag
# Upstream: Mike Newman <mike$gtnorthern,demon,co,uk>

Summary: Tool for determining versions of installed GNOME packages
Name: gnome-pkgview
Version: 1.0.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.greatnorthern.demon.co.uk/gnome-pkgview.html

Source: http://www.greatnorthern.demon.co.uk/packages/gnome-pkgview/gnome-pkgview-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2 >= 2.0.0, libxml2 >= 2.0.0, libgnomeui >= 2.0
BuildRequires: perl(XML::Parser), intltool, pkgconfig, gtk2-devel
BuildRequires: libxml2-devel, libgnome-devel, libgnomeui-devel
BuildRequires: gettext, autoconf, automake

%description
Displays version information for desktop components, and determines the
overall desktop version from the gnome-version.xml file.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
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
%doc AUTHORS ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/pixmaps/gnome-pkgview/
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1.2
- Rebuild for Fedora Core 5.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Updated to release 1.0.5.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
