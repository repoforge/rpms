# Authority: dag

Summary: Small applications which embed themselves in the GNOME panel.
Name: gnome-applets
Version: 2.3.6
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://www.gnome.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnome.org/pub/GNOME/sources/unstable/gnome-applets/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel >= 2.1, gnome-panel >= 2.0
BuildRequires: libxml2-devel, libgtop2-devel, libghttp, gdk-pixbuf-devel >= 0.7.0
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

#Obsoletes: battstat_applet, stickynotes_applet

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on Open Source
software.  The gnome-applets package provides Panel applets which
enhance your GNOME experience.

You should install the gnome-applets package if you would like embed small
utilities in the GNOME panel.

%prep
%setup

%build
%configure \
	--disable-install-schemas \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}-2.0

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/ \
		%{buildroot}%{_libexecdir}/gnome-applets/

### FIXME: Conflicting files from gnome-panel
%if %{?rh90:1}%{!?rh90:0}
%{__rm} -f %{buildroot}%{_sysconfdir}/gconf/schemas/mailcheck.schemas \
		%{buildroot}%{_sysconfdir}/sound/events/mailcheck.soundlist \
		%{buildroot}%{_datadir}/gnome-2.0/ui/GNOME_MailCheckApplet.xml \
		%{buildroot}%{_datadir}/gnome/help/mailcheck/C/mailcheck.xml
%endif

%post 
export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
for file in %{_sysconfdir}/gconf/schemas/*.schema; do
	gconftool-2 --makefile-install-rule $file &>/dev/null
done
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/*/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%config %{_sysconfdir}/sound/events/*.soundlist
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gnome/gkb/
%{_datadir}/omf/gnome-applets/
%{_datadir}/pixmaps/*
%{_datadir}/battstat_applet/
%{_datadir}/gen_util/
%{_datadir}/geyes/
%{_datadir}/gweather/
%{_datadir}/stickynotes/
%{_datadir}/wireless-applet/
%{_datadir}/xmodmap/

%changelog
* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 2.2.3-0
- Initial package. (using DAR)
