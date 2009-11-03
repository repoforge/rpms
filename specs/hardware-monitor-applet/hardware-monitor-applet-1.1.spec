# $Id$
# Authority: dag
# Upstream: Ole Laursen <olau$hardworking,dk>

%define real_name hardware-monitor

Summary: GNOME Applet for hardware monitoring
Name: hardware-monitor-applet
Version: 1.1
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.cs.auc.dk/~olau/hardware-monitor/

Source: http://www.cs.aau.dk/~olau/hardware-monitor/source/hardware-monitor-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm2 >= 2.0.0, libgnomemm2 >= 1.3.9, libgnomeuimm2 >= 1.3.11
BuildRequires: libglademm2 >= 2.0.0, libgnomecanvasmm2 >= 2.0.0, gconfmm2 >= 2.0.1
BuildRequires: gnome-panel >= 2.0, libgtop2 >= 2.0.0, lm_sensors-devel
BuildRequires: libbonobomm2-devel, libbonobouimm2-devel

%description
The Hardware Monitor applet is an applet for the GNOME panel which tries
to be a beautiful all-round solution to hardware monitoring. It also
tries to be user-friendly and generally nice and sensible, integrating
pleasantly with the rest of your GNOME desktop.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README src/TODO
#%doc %{_datadir}/gnome/help/hardware-monitor/
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/hardware-monitor/
%{_datadir}/pixmaps/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Fri Mar 05 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Updated to release 0.6.

* Mon Jun 02 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Updated to release 0.5.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
