# $Id$
# Authority: dag
# Upstream: David Boucher <bouda1$wanadoo,fr>

%define desktop_vendor rpmforge

Summary: Graphical Type1 font editor
Name: gribouy
Version: 0.0.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/gribouy/

Source: http://savannah.nongnu.org/download/gribouy/unstable.pkg/0.0/gribouy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0, gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Gribouy is a GNOME Type1 font editor.

%prep
%setup

%{__cat} <<EOF >gribouy.desktop
[Desktop Entry]
Name=Gribouy Font Editor
Comment=Design and edit Type1 fonts
Icon=gribouy.png
Exec=gribouy
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Graphics;Application;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__rm} -rf %{buildroot}%{_datadir}/applications/*.desktop

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gribouy.desktop

%{__install} -Dp -m0755 graphics/gribouy.png %{buildroot}%{_datadir}/pixmaps/gribouy.png

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/gnome-gribouy.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gribouy/
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/gribouy/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.8-1.2
- Rebuild for Fedora Core 5.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.0.8-1
- Add improved desktop file.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 0.0.8-0
- Updated to release 0.0.8.

* Sat Sep 27 2003 Dag Wieers <dag@wieers.com> - 0.0.7-0
- Updated to release 0.0.7.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.0.6-0
- Updated to release 0.0.6.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 0.0.5-0
- Updated to release 0.0.5.

* Wed Jul 02 2003 Dag Wieers <dag@wieers.com> - 0.0.4-0
- Updated to release 0.0.4.

* Sun Jun 14 2003 Dag Wieers <dag@wieers.com> - 0.0.3-0
- Initial package. (using DAR)
