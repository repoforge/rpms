# $Id$
# Authority: dag
# Upstream: <icewm-devel$lists,sourceforge,net>

### FIXME: Building icewm adds build env. stuff inside /usr/share/icewm/menu (Jonathan Underwood)

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Fast and small X11 window manager
Name: icewm
Version: 1.2.37
Release: 1%{?dist}
License: LGPL
Group: User Interface/Desktops
URL: http://www.icewm.org/

Source: http://dl.sf.net/sourceforge/icewm/icewm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake, libtool
BuildRequires: gcc-c++, gettext
BuildRequires: imlib-devel, imlib2-devel, libpng-devel, kdelibs
BuildRequires: giflib-devel, esound-devel
%{!?_without_gnome2:BuildRequires: gnome-desktop-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel, XFree86-font-utils}
%{!?_without_modxorg:BuildRequires: libX11-devel, xorg-x11-font-utils}
Obsoletes: icewm-common <= %{version}
Obsoletes: icewm-l10n <= %{version}
Obsoletes: icewm-menu-gnome2 <= %{version}
Obsoletes: icewm-themes <= %{version}

%description
A lightweight window manager for the X Window System. Optimized for
"feel" and speed, not looks. Features multiple workspaces, opaque
move/resize, task bar, window list, clock, mailbox, CPU, Network, APM
status.

%prep
%setup

%{__cat} <<EOF >icewm.switchdesk
#!/bin/sh
exec %{_bindir}/icewm
EOF

%{__cat} <<EOF >icewm.gdm
#!/bin/sh
exec %{_sysconfdir}/X11/xdm/Xsession icewm
EOF

%build
%configure \
   --enable-corefonts \
   --enable-gradients \
   --enable-guievents \
   --enable-menus-gnome2 \
   --enable-shaped-decorations \
   --with-icesound="ESound" \
   --with-docdir="%{_docdir}" \
%{!?_without_gnome2:--enable-menus-gnome2}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/icewm/
%{__install} -Dp -m0755 icewm.switchdesk %{buildroot}%{_datadir}/apps/switchdesk/Xclients.icewm
%{__install} -Dp -m0755 icewm.gdm %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Icewm

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING README doc/*.html doc/icewm.sgml
%config %{_datadir}/icewm/keys
%config %{_datadir}/icewm/menu
%config %{_datadir}/icewm/preferences
%config %{_datadir}/icewm/toolbar
%config %{_datadir}/icewm/winoptions
%config(noreplace) %{_sysconfdir}/icewm/
%{_datadir}/apps/switchdesk/Xclients.icewm
%{_sysconfdir}/X11/gdm/Sessions/Icewm
%{_bindir}/ice*
%{_datadir}/icewm/

%changelog
* Wed Oct 28 2009 Steve Huff <shuff@vecna.org> - 1.2.37-1
- Updated to release 1.2.37-1.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.2.30-1
- Updated to release 1.2.30.

* Mon Apr 17 2006 Dag Wieers <dag@wieers.com> - 1.2.26-1
- Updated to release 1.2.26.

* Thu Feb 09 2006 Dag Wieers <dag@wieers.com> - 1.2.25-1
- Updated to release 1.2.25.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.2.23-1
- Updated to release 1.2.23.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 1.2.22-1
- Updated to release 1.2.22.

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 1.2.20-2
- Added files for icewm to work with switchdesk and GDM. (Troy Dawson)

* Tue Jan 11 2005 Dag Wieers <dag@wieers.com> - 1.2.20-1
- Updated to release 1.2.20.

* Thu Jan 06 2005 Dag Wieers <dag@wieers.com> - 1.2.19-1
- Updated to release 1.2.19.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 1.2.16-1
- Initial package. (using DAR)
