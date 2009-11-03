# $Id$
# Authority: dag
# Upstream: Alp Toker <alp$atoker,com>


%define desktop_vendor rpmforge

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Tray applet for dynamically changing the XFree86 display mode
Name: switcher
Version: 1.0
Release: 3.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.atoker.com/switcher/

Source0: http://www.atoker.com/switcher/switcher-%{version}.tar.gz
Source1: egg-sharp.dll
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono, gtk-sharp
### Prevent building on systems with older XFree86 without Xrandr
%{?_without_modxorg:BuildRequires: XFree86 >= 4.2.0}
%{!?_without_modxorg:BuildRequires: libXrandr-devel, libX11-devel}
### FIXME: gtk-sharp needs gtk2 *.so files ;(
Requires: mono, gtk-sharp >= 0.17, gtk2-devel

%description
Switcher is a tray applet for dynamically changing the XFree86 display mode.

Switcher makes use of XRandR, The X Resize and Rotate Extension Protocol,
to allow the live manipulation of display properties during an X session.
It presently supports changes to the display resolution.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Display Resolution Switcher
Comment=%{summary}
Icon=switcher.png
Exec=switcher
Terminal=false
Type=Application
EOF

%{__cat} <<'EOF' >switcher.sh
#!/bin/sh
export LD_LIBRARY_PATH="%{_datadir}/switcher"
export MONO_PATH="%{_datadir}/switcher"
exec mono %{_bindir}/switcher.exe $@
EOF

%{__cp} -apv %{SOURCE1} .
%{__perl} -pi.orig -e '
		s|args.Event.button|args.Event.Button|;
		s|args.Event.time|args.Event.Time|;
	' *.cs

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 switcher.exe %{buildroot}%{_bindir}/switcher.exe
%{__install} -Dp -m0755 switcher.sh %{buildroot}%{_bindir}/switcher
%{__install} -Dp -m0644 switcher.png %{buildroot}%{_datadir}/pixmaps/switcher.png
%{__install} -d -m0755 %{buildroot}%{_datadir}/switcher/
%{__install} -p -m0755 *.dll *.so %{buildroot}%{_datadir}/switcher/

desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category System                      \
	--add-category Utility                     \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/switcher/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-3.2
- Rebuild for Fedora Core 5.

* Fri Aug 05 2003 Dag Wieers <dag@wieers.com> - 1.0-2
- Added switcher.sh and moved libegg to %{_datadir}/switcher.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
