# $Id$
# Authority: dag

%define real_name sensors-applet

Summary: Gnome panel applet for hardware sensors
Name: gnome-applet-sensors
Version: 1.5.2
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://sensors-applet.sourceforge.net/

Source: http://dl.sf.net/sourceforge/sensors-applet/sensors-applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gnome-panel-devel >= 2.8

Provides: %{real_name} = %{version}-%{release}
Obsoletes: %{real_name} <= %{version}-%{release}

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml
%{_datadir}/pixmaps/sensors-applet-icon.png
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_libexecdir}/sensors-applet

%changelog
* Thu Mar 22 2007 Dag Wieers <dag@wieers.com> - 1.5.2-1
- Initial package. (using DAR)
