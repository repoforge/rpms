# $Id$
# Authority: dag

%define real_name sensors-applet

Summary: Gnome panel applet for hardware sensors
Name: gnome-applet-sensors
Version: 1.7.10
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://sensors-applet.sourceforge.net/

Source: http://dl.sf.net/sourceforge/sensors-applet/sensors-applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, gnome-doc-utils, intltool, perl-XML-Parser, scrollkeeper
BuildRequires: lm_sensors-devel, libnotify-devel
BuildRequires: glib2-devel >= 2.6, gnome-panel-devel >= 2.8
Requires: scrollkeeper
Requires: scrollkeeper

Provides: %{real_name} = %{version}-%{release}
Obsoletes: %{real_name} <= %{version}-%{release}

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-scrollkeeper \
	--enable-libnotify
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
scrollkeeper-update -q -o %{_datadir}/omf/sensors-applet/ || :

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_datadir}/gnome/help/sensors-applet/
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml
%{_datadir}/icons/hicolor/*/apps/sensors-applet.png
%{_datadir}/icons/hicolor/*/devices/sensors-applet*.png
%{_datadir}/omf/sensors-applet/
%{_datadir}/pixmaps/sensors-applet/
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_libexecdir}/sensors-applet

%changelog
* Thu Mar 22 2007 Dag Wieers <dag@wieers.com> - 1.7.10-1
- Initial package. (using DAR)
