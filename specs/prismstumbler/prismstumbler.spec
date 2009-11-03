# $Id$
# Authority: dag
# Upstream: Florian <florian,boor$unix-ag,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{!?dtag:%define _with_lesstif 1}
%{?el5:%define _with_openmotif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc5:%define _with_openmotif 1}
%{?fc4:%define _with_openmotif 1}
%{?fc3:%define _with_lesstif 1}
%{?el4:%define _with_openmotif 1}
%{?el3:%define _with_openmotif 1}
%{?el2:%define _with_lesstif 1}

Summary: Wireless LAN (WLAN) accesspoint discovery tool
Name: prismstumbler
Version: 0.7.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://prismstumbler.sourceforge.net/

Source: http://dl.sf.net/prismstumbler/prismstumbler-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, sqlite-devel, autoconf, automake, libtool
BuildRequires: libpcap, gcc-c++
%{!?_without_modxorg:BuildRequires: libXt-devel, libXpm-devel, libXaw-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{?_with_openmotif:BuildRequires: openmotif-devel}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Prismstumbler is a wireless LAN (WLAN) discovery tool which scans for
beaconframes from accesspoints. Prismstumbler operates by constantly
switching channels and monitors any frames recived on the currently
selected channel.

%prep
%setup
%{__rm} -f src/gpsd/config.cache
### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\$\(PREFIX\)|\$(prefix)|g;
		s|/etc|\$(sysconfdir)|g;
		s|\$\(prefix\)/bin|\$(bindir)|g;
		s|\$\(prefix\)/share|\$(datadir)|g;
	' src/Makefile.in

### Cleaned up desktop file
%{__cat} <<EOF >src/familiar/prismstumbler.desktop
[Desktop Entry]
Name=Prismstumbler WLAN Scanner
Comment=Discover wireless access points in your vicinity
Exec=pst
Terminal=false
Type=Application
Icon=prism-icon4.png
Categories=GNOME;Application;Network;
StartupNotify=false
SingleInstance=true
EOF

%build
./autogen.sh
%configure
cd src/gpsd/
%configure
cd -

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/prismstumbler/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog doc/help.txt doc/INSTALL doc/README* doc/TODO NEWS README
%config %{_sysconfdir}/manufacturers.dat.gz
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/prismstumbler.desktop

%changelog
* Sat Oct 02 2004 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1.a
- Updated to release 0.7.1a.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
