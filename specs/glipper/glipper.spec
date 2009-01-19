# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Simple clipboard manager for GNOME
Name: glipper
Version: 1.0
Release: 1
License: GPL
Group: Applications/Text
URL: http://sourceforge.net/projects/glipper/

Source: http://dl.sf.net/sourceforge/glipper/glipper-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnome-doc-utils
BuildRequires: gnome-python2-applet
BuildRequires: intltool
BuildRequires: libglade2-devel
BuildRequires: libgnome-devel
BuildRequires: pygtk2-devel
Requires: desktop-file-utils
Requires: GConf2

%description
Glipper is a simple Clipboardmanager for the GNOME Desktop Environment

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

update-desktop-database &> /dev/null || :

touch --no-create %{_datadir}/icons/hicolor
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :

touch --no-create %{_datadir}/icons/hicolor
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/glipper/
%config %{_sysconfdir}/gconf/schemas/glipper.schemas
%{_datadir}/glipper/
%{_datadir}/icons/hicolor/*/apps/glipper.*
%{_libdir}/glipper/
%{_libdir}/bonobo/servers/Glipper.server
%{python_sitelib}/glipper/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 02 2009 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
