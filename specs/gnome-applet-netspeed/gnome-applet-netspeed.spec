# $Id$
# Authority: dag
# Upstream: Joergen Scheibengruber <mfcn$gmx,de>


%{?el3:%define _without_gnome_panel_devel 1}
%{?rh9:%define _without_gnome_panel_devel 1}

%define real_name netspeed_applet

Summary: GNOME applet that shows traffic on a network device
Name: gnome-applet-netspeed
Version: 0.14
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://mfcn.ilo.de/netspeed_applet/

Source: http://www.wh-hms.uni-ulm.de/~mfcn/shared/netspeed/netspeed_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, intltool, scrollkeeper, gcc-c++, gettext
BuildRequires: libgnomeui-devel >= 2.0, libgtop2-devel >= 2.14.2
%{!?_without_gnome_panel_devel:BuildRequires: gnome-panel-devel}
%{?_without_gnome_panel_devel:BuildRequires: gnome-panel}
Requires: scrollkeeper

Provides: netspeed_applet = %{version}-%{release}
Provides: netspeed-applet = %{version}-%{release}
Obsoletes: netspeed_applet <= %{version}-%{release}
Obsoletes: netspeed-applet <= %{version}-%{release}

%description
netspeed_applet is a little GNOME applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

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

%post
scrollkeeper-update -q -o %{_datadir}/omf/netspeed_applet/ || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/netspeed_applet/
%{_datadir}/pixmaps/netspeed_applet/
%{_datadir}/pixmaps/netspeed_applet.png
%{_datadir}/omf/netspeed_applet/
%{_libdir}/bonobo/servers/GNOME_NetspeedApplet.server
%{_libexecdir}/netspeed_applet2

%changelog
* Fri Mar 23 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.
- Renamed package to gnome-applet-netspeed.

* Sun May 01 2005 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
