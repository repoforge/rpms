# $Id$
# Authority: rudolf
# Upstream: <gnomeicu-support$lists,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_applet 1}
%{?fc3:%define _without_applet 1}
%{?fc2:%define _without_applet 1}

Summary: Clone of Mirabilis' popular ICQ
Name: gnomeicu
Version: 0.99.10
Release: 1%{?dist}
Epoch: 1
License: GPL
Group: Applications/Communications
URL: http://gnomeicu.sourceforge.net/

Source: http://download.sourceforge.net/gnomeicu/gnomeicu-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.16, libgnomeui-devel >= 2.0.0, gnet-devel >= 1.1.3
BuildRequires: libxml2-devel >= 2.4.7, scrollkeeper >= 0.3.5
BuildRequires: gtkspell-devel >= 2.0.4

Requires(post): scrollkeeper

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.


%package applet
Summary: GNOME applet for GnomeICU
Group: Applications/Communications
Requires: %{name} = %{epoch}:%{version}-%{release}

%description applet
The is the gnome2 applet for GnomeICU. It is now deprecated.
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
The original source was taken from Matt Smith's mICQ.

%prep
%setup

%build
%configure \
%{!?_without_applet:--enable-applet} \
	--enable-spell
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_datadir}/gnome/help/gnomeicu/
%config %{_sysconfdir}/gconf/schemas/gnomeicu.schemas
%config %{_sysconfdir}/sound/events/GnomeICU.soundlist
%{_bindir}/gnomeicu
%{_bindir}/gnomeicu-client
%{_datadir}/applications/GnomeICU.desktop
%{_datadir}/gnomeicu/
%{_datadir}/omf/gnomeicu/
%{_datadir}/pixmaps/gnome-gnomeicu.png
%{_datadir}/sounds/gnomeicu/

%if %{!?_without_applet:1}0
%files applet
%defattr(-, root, root, 0755)
%{_libexecdir}/gnomeicu-applet
%{_datadir}/gnome-2.0/ui/GNOME_GnomeICUApplet.xml
%{_libdir}/bonobo/servers/GNOME_GnomeICUApplet.server
%endif

%changelog
* Sat Feb 18 2006 Dag Wieers <dag@wieers.com> - 0.99.10-1
- Updated to release 0.99.10.

* Mon Feb 13 2006 Dag Wieers <dag@wieers.com> - 0.99.9-1
- Updated to release 0.99.9.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.99.5-1
- Updated to release 0.99.5.
- Merged with SPEC file contributed by Andreas Rogge.

* Wed Nov 19 2003 Dag Wieers <dag@wieers.com> - 0.99-2
- Fix incredibly stupid epoch problem with Fedora. (Axel Thimm)

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.99-1
- Added the deprecated applet sub-package.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.99-0
- Initial package. (using DAR)
