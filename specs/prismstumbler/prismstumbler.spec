# $Id$

# Authority: dag
# Upstream: Jafer <jan.b.fernquist@telia.com>
# Upstream: Florian <florian.boor@unix-ag.org>

Summary: Wireless LAN (WLAN) discovery tool which scans for beaconframes from accesspoints.
Name: prismstumbler
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://prismstumbler.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/prismstumbler/prismstumbler-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel, sqlite-devel

%description
Prismstumbler is a wireless LAN (WLAN) discovery tool which scans for
beaconframes from accesspoints. Prismstumbler operates by constantly
switching channels and monitors any frames recived on the currently
selected channel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gv4l
Comment=%{summary}
Icon=gv4l/gv4l.png
Exec=%{name}
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
