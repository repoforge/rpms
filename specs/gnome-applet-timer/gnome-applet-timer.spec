# $Id$
# Authority: dag
# Upstream: Jimmy Do <crispyleaves$gmail,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_gnome_panel_devel 1}
%{?rh9:%define _without_gnome_panel_devel 1}

%define real_name timer-applet

Summary: Countdown timer applet for GNOME
Name: gnome-applet-timer
Version: 2.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://timerapplet.sourceforge.net/

Source: http://dl.sf.net/timerapplet/timer-applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, intltool, perl(XML::Parser), gtk2-devel >= 2.8
%{!?_without_gnome_panel_devel:BuildRequires: gnome-panel-devel >= 2.6}
%{?_without_gnome_panel_devel:BuildRequires: gnome-panel >= 2.6}
Requires: scrollkeeper

Provides: timer-applet = %{version}-%{release}
Obsoletes: timer-applet <= %{version}-%{release}

%description
Timer Applet is a countdown timer applet for the GNOME panel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-scrollkeeper
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/timer-applet.schemas &>/dev/null
scrollkeeper-update -q -o %{_datadir}/omf/timer-applet/ || :

%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/timer-applet.schemas &>/dev/null

%postun
scrollkeeper-update -q || :

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/timer-applet/
%config %{_sysconfdir}/gconf/schemas/timer-applet.schemas
%{_datadir}/gnome-2.0/ui/GNOME_TimerApplet.xml
%{_datadir}/gnome/help/timer-applet/
%{_datadir}/omf/timer-applet/
%{_datadir}/pixmaps/timer-applet/
%{_libdir}/bonobo/servers/GNOME_TimerApplet.server
%{_libexecdir}/timer-applet

%changelog
* Sat Apr 28 2007 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1

* Fri Mar 23 2007 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Updated to release 1.3.2
- Renamed package to gnome-applet-timer.

* Mon May 08 2006 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
