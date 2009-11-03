# $Id$

# Authority: dag

Summary: GNOME browser based on Gecko (Mozilla rendering engine)
Name: galeon
Version: 1.2.11
Release: 0%{?dist}
License: GPL
Group: Applications/Internet
URL: http://galeon.sourceforge.net/

Source: http://dl.sf.net/galeon/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mozilla-devel >= 1.3, gtk+-devel >= 1.2.9, libxml-devel >= 1.8.14
BuildRequires: gnome-libs-devel >= 1.2.11, libglade-devel >= 0.13, glib-devel
BuildRequires: gnome-vfs-devel >= 1.0.1, GConf-devel >= 1.0.4
BuildRequires: oaf-devel >= 0.6.5, gdk-pixbuf-devel >= 0.14.0, ORBit-devel >= 0.5.7
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
Galeon is a web browser built around Gecko (Mozilla 's rendering engine)
and Necko (Mozilla's networking engine). It's a GNOME web browser,
designed to take advantage of as many GNOME technologies as makes sense.
Galeon was written to do just one thing - browse the web.

%prep
%setup

%build
%configure \
	--disable-install-schemas \
	--disable-scrollkeeper-update \
	--with-gnome \
	--without-debug \
	--disable-werror \
	--with-mozilla-snapshot="1.4b"
#	--enable-nautilus-view \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%post
%{_bindir}/galeon-config-tool --fix-gconf-permissions
%{_bindir}/galeon-config-tool --pkg-install-schemas
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ* NEWS README* THANKS TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/galeon/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%config %{_sysconfdir}/sound/events/*
%{_bindir}/*
%{_libdir}/galeon/
%{_datadir}/galeon/
%{_datadir}/gnome/apps/Internet/*.desktop
%{_datadir}/gnome/ui/*
%{_datadir}/oaf/*
%{_datadir}/omf/galeon/
%{_datadir}/pixmaps/*
%{_datadir}/sounds/galeon/

%changelog
* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 1.2.11-0
- Updated to release 1.2.11.

* Mon May 12 2003 Dag Wieers <dag@wieers.com> - 1.2.10-0.a
- Updated to release 1.2.10a.

* Sat Mar 25 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Initial package. (using DAR)
