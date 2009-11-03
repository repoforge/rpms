# $Id$
# Authority: dag
# Upstream: Josh Buhl <jbuhl$users,sourseforge,net>

%define po_version 0.32

Summary: Display the current phase of the Moon as an applet for the gnome panel
Name: glunarclock
Version: 0.32.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://glunarclock.sourceforge.net/

Source: http://dl.sf.net/glunarclock/glunarclock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gail-devel, libxklavier-devel, scrollkeeper, gcc-c++
BuildRequires: gnome-panel-devel, gettext, intltool, perl(XML::Parser)
%{?fc4:BuildRequires: gettext-devel}
Requires(post): scrollkeeper

%description
GNOME Lunar Clock displays the current phase of the Moon as an applet
for the gnome panel.

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
%find_lang %{name}-%{po_version}

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-%{po_version}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
#%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/glunarclock-applet-2/
%config %{_sysconfdir}/gconf/schemas/glunarclock.schemas
%{_libexecdir}/glunarclock-applet-2
%{_libdir}/bonobo/servers/GNOME_GLunarclockApplet_Factory.server
%{_datadir}/glunarclock/
%{_datadir}/gnome-2.0/ui/GNOME_GLunarclockApplet.xml
%{_datadir}/pixmaps/glunarclock-logo.png
%{_datadir}/pixmaps/glunarclock/
%{_datadir}/omf/glunarclock/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.32.4-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.32.4-0
- Updated to release 0.32.4.

* Wed Jan 12 2005 Dag Wieers <dag@wieers.com> - 0.32.2-0
- Updated to release 0.32.2.

* Thu Jun 26 2004 Dag Wieers <dag@wieers.com> - 0.32.1-0
- Updated to release 0.32.1.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.30.3-0
- Updated to release 0.30.3.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 0.30.2-0
- Updated to release 0.30.2.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.30.1-0
- Initial package. (using DAR)
