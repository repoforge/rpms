# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

%define desktop_vendor rpmforge

Summary: Tray applet for displaying phonetic alphabets
Name: alphapplet
Version: 0.2
Release: 0.2%{?dist}
Group: Applications/System
License: GPL
URL: http://dag.wieers.com/home-made/gnome-applets/#alphapplet

Source: http://dag.wieers.com/home-made/gnome-applets/alphapplet-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono, gtk-sharp
### FIXME: gtk-sharp needs gtk2/gnome2 *.so files ;(
Requires: mono, gtk-sharp, gtk2-devel, libgnomeui-devel, GConf2-devel, libglade2-devel

%description
Alphapplet is a tray applet for displaying phonetic alphabets.
It is meant for people who often need to spell out passwords or
other things and lack creativity or have too much creativity ;)

%prep
%setup

%{__cat} <<'EOF' >alphapplet.sh
#!/bin/sh
export LD_LIBRARY_PATH="%{_datadir}/alphapplet/"
export MONO_PATH="%{_datadir}/alphapplet/"
exec mono %{_bindir}/alphapplet.exe $@
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

desktop-file-install --vendor %{desktop_vendor}    \
	--delete-original                          \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/alphapplet.desktop
%{__install} -Dp -m0755 alphapplet.sh %{buildroot}%{_bindir}/alphapplet

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT README TODO
%{_bindir}/*
%{_datadir}/applications/%{desktop_vendor}-alphapplet.desktop
%{_datadir}/pixmaps/*
%{_datadir}/alphapplet/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-0.2
- Rebuild for Fedora Core 5.

* Fri Sep 05 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Updated to release 0.2.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
