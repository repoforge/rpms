# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: Tray applet for changing network proxy configuration
Name: proxy-applet
Version: 0.2.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://dag.wieers.com/home-made/gnome-applets/

Source: http://dag.wieers.com/home-made/gnome-applets/proxy-applet-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono, gtk-sharp
### FIXME: gtk-sharp needs gtk2/gnome2 *.so files ;(
Requires: mono, gtk-sharp >= 0.17, gtk2-devel, libgnomeui-devel, GConf2-devel, libglade2-devel

%description
Proxy-applet is a tray applet for changing your network proxy configuration.

%prep
%setup

%{__cat} <<'EOF' >proxy-applet.sh
#!/bin/sh
export LD_LIBRARY_PATH="%{_datadir}/proxy-applet"
export MONO_PATH="%{_datadir}/proxy-applet"
exec mono %{_bindir}/proxy-applet.exe $@
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 proxy-applet.sh %{buildroot}%{_bindir}/proxy-applet

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/proxy-applet/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0.2
- Rebuild for Fedora Core 5.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Updated to release 0.2.4.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.2.3-0
- Updated to release 0.2.3.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Updated to release 0.2.2.

* Sun Jun 15 2003 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Updated to release 0.2.1.

* Sat Jun 14 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
