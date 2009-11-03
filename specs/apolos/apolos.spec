# $Id$
# Authority: dag
# Upstream: Jonathan Gonzalez V. <jonathan$blueplanet,cl>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Small cd player for GNOME
Name: apolos
Version: 0.1.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.nongnu.org/apolos/

Source: http://savannah.nongnu.org/download/apolos/apolos-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2 >= 2.0, cdparanoia-devel, pkgconfig, gtk2-devel
BuildRequires: gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Apolos is a small cd player for GNOME.

%prep
%setup

### FIXME: Add /usr/include/cdda to include dirs. (Please fix upstream)
%{__perl} -pi.orig -e 's|^(CFLAGS =)|$1 -I%{_includedir}/cdda|' src/Makefile.in

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >apolos.desktop
[Desktop Entry]
Name=Apolos CD Player
Comment=Play audio CDs
Icon=gnome-multimedia.png
Exec=apolos
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 apolos.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/apolos.desktop
%else
	desktop-file-install --vendor %{desktop_vendor}       \
		--delete-original                             \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/applications/apolos.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/apolos
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/apolos.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-apolos.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1.2
- Rebuild for Fedora Core 5.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.1.8-1
- Updated to release 0.1.8.

* Mon Jun 07 2004 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Added improved desktop file.
- Updated to release 0.1.7.

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Updated to release 0.1.5.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 0.1.4-0
- Initial package. (using DAR)
