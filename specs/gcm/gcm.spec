# $Id$

# Authority: dag

# Upstream: Philip Van Hoof <me$freax,org>

Summary: GNOME Clipboard Manager
Name: gcm
Version: 2.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://gcm.sourceforge.net/

Source: http://dl.sf.net/gcm/gcm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnomeui-devel >= 1.96.0, GConf2-devel >= 1.0.8
BuildRequires: gtkhtml2-devel >= 2.0, libxml2-devel >= 2.0
#BuildRequires: mozilla-devel >= 1.1
Obsoletes: gcmapplet

%description
GNOME Clipboard Manager is a selection and clipboard manager.

It collects copy-selections and has the option to choose which selection is
to be pasted. Selections can be edited, manually created, deleted, copied,
and pasted. The available selection types are clipboard, primary, secondary,
or a custom atom.

%package devel
Summary: GNOME Clipboard Manager development files
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains de header-files and static libraries for
GNOME Clipboard Manager development.

%prep
%setup

%build
./autogen.sh
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

### FIXME: Remove locale-files because they're named: LC_MESSAGES/@GETTEXT_PACKAGE@.mo
#find_lang %{name}
%{__rm} -rf %{buildroot}%{_datadir}/locale/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gcm/Plugins/*.a \
		%{buildroot}%{_libdir}/gcm/Plugins/*.la

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --install-schema-file="%{_sysconfdir}/gconf/schemas/%{name}.schemas" &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_mandir}/man1/gcm.*
%dir %{_libdir}/gcm/
%config %{_sysconfdir}/gconf/schemas/*
%{_libexecdir}/gcmapplet
%{_bindir}/gcm
%{_bindir}/gcmui
%{_libdir}/bonobo/servers/*
%{_libdir}/gcm/Plugins/*.so
%{_libdir}/*.so.*
%{_datadir}/gnome/apps/Applications/Other/*.desktop
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/pixmaps/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.png doc/HACKING
%doc %{_mandir}/man1/gcm-config.*
%{_bindir}/gcm-config
%{_includedir}/libgcm/*.h
%{_includedir}/librtftohtml/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la
#exclude %{_libdir}/gcm/Plugins/*.a
#exclude %{_libdir}/gcm/Plugins/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Updated to release 2.0.4.

* Fri Jan 18 2003 Dag Wieers <dag@wieers.com> - 2.0.3.20030118-0
- Merged gcmapplet into gcm package.
- Fixed the plugin files.
- Temporarily remove static plugins.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Initial package.
