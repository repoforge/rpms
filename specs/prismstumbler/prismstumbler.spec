# $Id$

# Authority: dag
# Upstream: Florian <florian.boor@unix-ag.org>
# Upstream: Jafer <jan.b.fernquist@telia.com>
# Distcc: 0

%define rversion 0.7.1a

Summary: Wireless LAN (WLAN) accesspoint discovery tool.
Name: prismstumbler
Version: 0.7.1
Release: 1.a
License: GPL
Group: Applications/Internet
URL: http://prismstumbler.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/prismstumbler/prismstumbler-%{rversion}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel, sqlite-devel

%description
Prismstumbler is a wireless LAN (WLAN) discovery tool which scans for
beaconframes from accesspoints. Prismstumbler operates by constantly
switching channels and monitors any frames recived on the currently
selected channel.

%prep
%setup -n %{name}-%{rversion}

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
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/INSTALL NEWS README doc/TODO doc/help.txt doc/README*
%config %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_docdir}/prismstumbler/help.txt

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1.a
- Updated to release 0.7.1a.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
