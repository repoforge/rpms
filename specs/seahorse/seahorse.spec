# $Id$
# Authority: dag

### EL6 ships with seahorse-2.28.1-4.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: GNOME gnupg interface
Name: seahorse
Version: 0.8
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://seahorse.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/seahorse/0.8/seahorse-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gpgme-devel >= 0.3.14
BuildRequires: scrollkeeper, pkgconfig, GConf2, gnupg, gcc-c++
BuildRequires: libgnomeui-devel, libglade2-devel, gtk2-devel >= 2.4
BuildRequires: libbonobo-devel, libbonoboui-devel, eel2-devel
BuildRequires: gedit-devel, gettext, nautilus
BuildRequires: intltool, perl(XML::Parser)

Requires(post): scrollkeeper

%description
Seahorse is a GNOME interface for gnupg.
It uses gpgme as the backend.

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
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper
%{__rm} -f %{buildroot}%{_libdir}/bonobo/*.a \
        %{buildroot}%{_libdir}/bonobo/*.la
%{__rm} -Rf %{buildroot}%{_datadir}/mime/XMLnamespaces \
    %{buildroot}%{_datadir}/mime/aliases \
    %{buildroot}%{_datadir}/mime/globs \
    %{buildroot}%{_datadir}/mime/magic \
    %{buildroot}%{_datadir}/mime/subclasses \
    %{buildroot}%{_datadir}/mime/application

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/seahorse/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
#%{_libdir}/bonobo/*.so
%{_libdir}/gedit-2/plugins/libseahorse*
%{_libdir}/gedit-2/plugins/seahorse-pgp.gedit-plugin
%{_libdir}/libseahorse*
#%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*.desktop
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/mime-info/*
%{_datadir}/mime/packages/seahorse.xml
%{_datadir}/omf/seahorse/
%{_datadir}/pixmaps/*
%{_datadir}/seahorse/
%{_libdir}/nautilus/extensions-1.0/libnautilus-seahorse.*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1.2
- Rebuild for Fedora Core 5.

* Mon Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.8-0
- Updated to release 0.7.8.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Updated to release 0.6.3.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
