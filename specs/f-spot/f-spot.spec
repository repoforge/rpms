# $Id$
# Authority: dag
# Upstream: <f-spot-list$gnome,org>

%define desktop_vendor rpmforge

Summary: Personal photo management application
Name: f-spot
Version: 0.0.8
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://www.gnome.org/projects/f-spot/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/Public/GNOME/sources/f-spot/0.0/f-spot-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-devel, libexif-devel, lcms-devel
Requires: mono, gtk-sharp, libexif

%description
F-Spot is an application designed to provide personal photo management
to the GNOME desktop. Plans include import, export, printing and advanced
sorting of digital images.

%prep
%setup

%{__cat} <<EOF >f-spot.desktop
[Desktop Entry]
Name=F-spot Photo Manager
Comment=Manage your photos
Icon=f-spot.png
Exec=f-spot
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;
StartupNotify=true
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -D -m0644 icons/f-spot-camera.png %{buildroot}%{_datadir}/pixmaps/f-spot.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	f-spot.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL MAINTAINERS NEWS README TODO
%{_bindir}/f-spot
%{_libdir}/f-spot/
%{_datadir}/pixmaps/f-spot.png
%{_datadir}/applications/%{desktop_vendor}-f-spot.desktop
%exclude %{_libdir}/f-spot/*.a
%exclude %{_libdir}/f-spot/*.la

%changelog
* Fri Feb 18 2005 Dag Wieers <dag@wieers.com> - 0.0.8-1
- Updated to release 0.0.8.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.0.7-1
- Updated to release 0.0.7.

* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Updated to release 0.0.6.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Updated to release 0.0.5.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Updated to release 0.0.3.

* Sat Mar 20 2004 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
